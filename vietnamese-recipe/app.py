from flask import Flask, render_template, request, jsonify, send_from_directory
from recipe_parser import load_recipes_from_folder
from thefuzz import fuzz
import random
import re
import unicodedata
import os
import time

app = Flask(__name__)

# --- CẤU HÌNH ---
DATA_FOLDER = './data'
IMAGE_FOLDER = './images'

# Đảm bảo folder tồn tại
os.makedirs(DATA_FOLDER, exist_ok=True)
os.makedirs(IMAGE_FOLDER, exist_ok=True)

# --- HELPER: Xử lý tiếng Việt ---
def remove_accents(input_str):
    if not input_str: return ""
    s1 = unicodedata.normalize('NFD', input_str)
    s2 = ''.join(c for c in s1 if unicodedata.category(c) != 'Mn')
    return s2.replace('đ', 'd').replace('Đ', 'D')

# --- HELPER: Format (Recipe.g4) ---
def format_recipe_to_antlr(data):
    """
    Chuyển đổi dữ liệu từ form thành text đúng ngữ pháp Recipe.g4
    """
    # 1. Header info
    content = f"RECIPE: {data['name']}\n"
    content += f"IMAGE: {data.get('image', 'default.jpg')}\n"
    content += f"REGION: {data['region']}\n"
    content += f"TIME: {data['time']}\n"
    content += f"SERVINGS: {data['servings']}\n"
    content += f"CALORIES: {data['calories']}\n"
    content += f"DIFFICULTY: {data['difficulty']}\n"
    content += f"CATEGORY: {data['category']}\n"
    content += f"TAGS: {data['tags']}\n"
    
    # 2. Ingredients (Thêm gạch đầu dòng nếu thiếu)
    content += "INGREDIENTS:\n"
    raw_ings = data['ingredients'].split('\n')
    for ing in raw_ings:
        clean_ing = ing.strip()
        if clean_ing:
            if not clean_ing.startswith('-'):
                content += f"- {clean_ing}\n"
            else:
                content += f"{clean_ing}\n"
            
    # 3. Steps (Thêm gạch đầu dòng nếu thiếu)
    content += "STEPS:\n"
    raw_steps = data['steps'].split('\n')
    for step in raw_steps:
        clean_step = step.strip()
        if clean_step:
            if not clean_step.startswith('-'):
                content += f"- {clean_step}\n"
            else:
                content += f"{clean_step}\n"
            
    return content

# --- KHỞI TẠO CHATBOT ---
print("Loading recipes...")
recipes = load_recipes_from_folder(DATA_FOLDER)
print(f"Loaded {len(recipes)} recipes!")

class RecipeChatbot:
    def __init__(self, recipes):
        self.recipes = recipes
    
    def reload_data(self, new_recipes):
        self.recipes = new_recipes

    def find_recipes(self, user_input):
        raw_query = user_input.lower().strip()
        clean_query = remove_accents(raw_query)
        matches = []
        
        is_quick = any(w in clean_query for w in ['nhanh', 'quick', 'fast', '30 mins'])
        is_easy = any(w in clean_query for w in ['de', 'easy', 'simple'])

        for recipe in self.recipes:
            score = 0
            
            # A. Tags Match
            if 'tags' in recipe:
                for tag in recipe['tags']:
                    tag_clean = remove_accents(tag)
                    if fuzz.partial_ratio(clean_query, tag_clean) > 85:
                        score += 30
            
            # B. Ingredients Match
            matched_ingredients_count = 0
            for ing in recipe['ingredients']:
                ing_clean = remove_accents(ing.lower())
                if fuzz.token_set_ratio(ing_clean, clean_query) > 80:
                     matched_ingredients_count += 1
            if matched_ingredients_count > 0:
                score += (matched_ingredients_count * 15)

            # C. Name Match
            name_accent = recipe['name'].lower()
            name_no_accent = remove_accents(name_accent)
            ratio_no_accent = fuzz.partial_ratio(clean_query, name_no_accent)
            ratio_accent = fuzz.partial_ratio(raw_query, name_accent)
            final_name_ratio = max(ratio_no_accent, ratio_accent)
            
            if final_name_ratio > 75: 
                score += final_name_ratio * 1.5
            
            # D. Filters
            if is_quick and recipe.get('time', 999) <= 30: score += 20
            if is_easy and 'easy' in recipe.get('difficulty', '').lower(): score += 20

            if score > 50: 
                matches.append({'recipe': recipe, 'score': score})
        
        matches.sort(key=lambda x: x['score'], reverse=True)
        return [m['recipe'] for m in matches[:5]]

    def generate_response(self, user_input):
        query = remove_accents(user_input.lower().strip())
        
        if any(w in query for w in ['hi', 'hello', 'chao', 'xin chao']):
            return {'type': 'greeting', 'text': "Hello! 👋 What would you like to cook? (You can enter the dish name or ingredients)"}
            
        if any(w in query for w in ['random', 'goi y', 'bat ky']):
            chosen = random.choice(self.recipes)
            return {'type': 'recipe', 'text': "🎉 Today, try this recipe:", 'recipe': chosen}

        if 'calo' in query or 'calories' in query:
            nums = re.findall(r'\d+', query)
            if nums:
                limit = int(nums[0])
                matches = [r for r in self.recipes if r.get('calories', 9999) <= limit]
                matches.sort(key=lambda x: x.get('calories', 0), reverse=True)
                if matches:
                    return {'type': 'multiple', 'text': f"🥗 Recipes under {limit} calories:", 'recipes': matches[:5]}

        matches = self.find_recipes(user_input)
        
        if not matches:
            return {'type': 'not_found', 'text': f"Hmm, I haven't found anything that matches '{user_input}' yet. Can you name the ingredients?"}
        
        if len(matches) == 1:
            return {'type': 'recipe', 'text': f"✨ Found this recipe:", 'recipe': matches[0]}

        return {'type': 'multiple', 'text': f"🔍 Found {len(matches)} matching recipes:", 'recipes': matches}

chatbot = RecipeChatbot(recipes)

# --- ROUTES ---

@app.route('/')
def index():
    return render_template('index.html', recipe_count=len(recipes))

@app.route('/chat')
def chat_page():
    return render_template('chat.html')

@app.route('/images/<path:filename>')
def serve_images(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    response = chatbot.generate_response(data.get('message', ''))
    return jsonify(response)

# --- ROUTE: THÊM CÔNG THỨC (CÓ ẢNH) ---
@app.route('/api/add_recipe', methods=['POST'])
def add_recipe():
    try:
        # 1. Lấy dữ liệu Text (dùng request.form vì gửi multipart)
        data = request.form.to_dict()
        
        # 2. Xử lý File Ảnh
        image_filename = 'default.jpg'
        
        if 'image_file' in request.files:
            file = request.files['image_file']
            if file and file.filename != '':
                # Tạo tên file an toàn: slug_timestamp.ext
                ext = file.filename.rsplit('.', 1)[1].lower() if '.' in file.filename else 'jpg'
                safe_name = remove_accents(data['name']).lower().replace(' ', '_')
                new_filename = f"{safe_name}_{int(time.time())}.{ext}"
                
                # Lưu file
                file_path = os.path.join(IMAGE_FOLDER, new_filename)
                file.save(file_path)
                
                image_filename = new_filename

        # Gán tên ảnh vào data để ghi vào file text
        data['image'] = image_filename
        
        # 3. Tạo nội dung file .txt theo ngữ pháp Recipe.g4
        file_content = format_recipe_to_antlr(data)
        
        # 4. Lưu file .txt
        txt_filename = f"{remove_accents(data['name']).lower().replace(' ', '_')}_{int(time.time())}.txt"
        txt_path = os.path.join(DATA_FOLDER, txt_filename)
        
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(file_content)
            
        # 5. Reload dữ liệu
        global recipes, chatbot
        recipes = load_recipes_from_folder(DATA_FOLDER)
        chatbot.reload_data(recipes)
        
        return jsonify({
            'status': 'success', 
            'message': 'Successfully added the recipe!',
            'image_url': f"/images/{image_filename}"
        })

    except Exception as e:
        print(f"Error saving recipe: {e}")
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)