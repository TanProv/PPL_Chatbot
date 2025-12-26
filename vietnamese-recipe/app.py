from flask import Flask, render_template, request, jsonify, send_from_directory
from recipe_parser import load_recipes_from_folder
from thefuzz import fuzz
import random
import re
import unicodedata

app = Flask(__name__)

# --- CẤU HÌNH ---
DATA_FOLDER = './data'
IMAGE_FOLDER = './images'

# --- Function to remove Vietnamese accents ---
def remove_accents(input_str):
    if not input_str: return ""
    s1 = unicodedata.normalize('NFD', input_str)
    s2 = ''.join(c for c in s1 if unicodedata.category(c) != 'Mn')
    return s2.replace('đ', 'd').replace('Đ', 'D')

print("Loading recipes...")
recipes = load_recipes_from_folder(DATA_FOLDER)
print(f"Loaded {len(recipes)} recipes!")


class RecipeChatbot:
    def __init__(self, recipes):
        self.recipes = recipes
    
    def find_recipes(self, user_input):
        # 1. Normalize query
        raw_query = user_input.lower().strip()
        clean_query = remove_accents(raw_query)
        
        matches = []
        
        # Logic filters cơ bản
        is_quick = any(w in clean_query for w in ['nhanh', 'quick', 'fast', '30 mins'])
        is_easy = any(w in clean_query for w in ['de', 'easy', 'simple'])

        for recipe in self.recipes:
            score = 0
            
            # --- A. TAGS MATCHING ---
            # Nếu người dùng tìm "món nước", "ăn sáng", "truyền thống"...
            if 'tags' in recipe:
                for tag in recipe['tags']:
                    tag_clean = remove_accents(tag)
                    if fuzz.partial_ratio(clean_query, tag_clean) > 85:
                        score += 30 # Cộng điểm lớn nếu khớp tag
            
            # --- B. FRIDGE SEARCH / INGREDIENTS CHECK ---
            # Tìm xem có bao nhiêu nguyên liệu trong input khớp với recipe
            matched_ingredients_count = 0
            for ing in recipe['ingredients']:
                ing_clean = remove_accents(ing.lower())
                # Kiểm tra nếu tên nguyên liệu xuất hiện trong query
                if fuzz.token_set_ratio(ing_clean, clean_query) > 80:
                     matched_ingredients_count += 1
            
            if matched_ingredients_count > 0:
                # Cộng điểm dựa trên số lượng nguyên liệu khớp
                # Khớp càng nhiều nguyên liệu, khả năng cao là món user muốn nấu
                score += (matched_ingredients_count * 15)

            # --- C. NAME MATCHING (Core logic cũ) ---
            name_accent = recipe['name'].lower()
            name_no_accent = remove_accents(name_accent)
            
            ratio_no_accent = fuzz.partial_ratio(clean_query, name_no_accent)
            ratio_accent = fuzz.partial_ratio(raw_query, name_accent)
            final_name_ratio = max(ratio_no_accent, ratio_accent)
            
            if final_name_ratio > 75: 
                score += final_name_ratio * 1.5
            
            # --- D. FILTERS ---
            if is_quick and recipe.get('time', 999) <= 30: score += 20
            if is_easy and 'easy' in recipe.get('difficulty', '').lower(): score += 20

            # Ngưỡng score để hiển thị
            if score > 50: 
                matches.append({'recipe': recipe, 'score': score})
        
        # Sắp xếp theo điểm giảm dần
        matches.sort(key=lambda x: x['score'], reverse=True)
        return [m['recipe'] for m in matches[:5]]

    def generate_response(self, user_input):
        query = remove_accents(user_input.lower().strip())
        
        # 1. Greeting
        if any(w in query for w in ['hi', 'hello', 'chao', 'xin chao']):
            return {'type': 'greeting', 'text': "Xin chào! 👋 Bạn muốn nấu món gì? (Có thể nhập tên món hoặc nguyên liệu bạn đang có)"}
            
        # 2. Random
        if any(w in query for w in ['random', 'goi y', 'bat ky', 'hom nay an gi']):
            chosen = random.choice(self.recipes)
            return {'type': 'recipe', 'text': "🎉 Hôm nay hãy thử món này nhé:", 'recipe': chosen}

        # 3. Calories Search
        if 'calo' in query or 'calories' in query:
            nums = re.findall(r'\d+', query)
            if nums:
                limit = int(nums[0])
                matches = [r for r in self.recipes if r.get('calories', 9999) <= limit]
                matches.sort(key=lambda x: x.get('calories', 0), reverse=True)
                if matches:
                    return {'type': 'multiple', 'text': f"🥗 Các món dưới {limit} calo:", 'recipes': matches[:5]}

        # 4. Main Search
        matches = self.find_recipes(user_input)
        
        if not matches:
            return {
                'type': 'not_found',
                'text': f"Hmm, tôi chưa tìm thấy món nào khớp với '{user_input}'. Bạn thử kể tên nguyên liệu xem sao?"
            }
        
        if len(matches) == 1:
            return {'type': 'recipe', 'text': f"✨ Tìm thấy món này hợp nhất:", 'recipe': matches[0]}
            
        return {'type': 'multiple', 'text': f"🔍 Tìm thấy {len(matches)} món phù hợp:", 'recipes': matches}

chatbot = RecipeChatbot(recipes)

@app.route('/')
def index():
    return render_template('index.html', recipe_count=len(recipes))

@app.route('/chat')
def chat_page():
    return render_template('chat.html', recipe_count=len(recipes))

@app.route('/images/<path:filename>')
def serve_images(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    response = chatbot.generate_response(data.get('message', ''))
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)