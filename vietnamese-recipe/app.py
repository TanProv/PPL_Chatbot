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

# Map ảnh 
IMAGE_MAP = {
    'Pho Bo (Beef Noodle Soup)': 'phobo.jpg',
    'Banh Mi (Vietnamese Sandwich)': 'banh-mi.jpg',
    'Bun Cha (Grilled Pork with Noodles)': 'bun-cha.jpg',
    'Goi Cuon (Fresh Spring Rolls)': 'goi-cuon.jpg',
    'Com Tam (Broken Rice with Grilled Pork)': 'com-tam.jpg',
    'Cha Gio (Fried Spring Rolls)': 'cha-gio.jpg',
    'Bun Bo Hue (Spicy Beef Noodle Soup)': 'bun-bo-hue.jpg',
    'Banh Xeo (Crispy Vietnamese Crepes)': 'banh-xeo.jpg',
    'Ca Kho To (Caramelized Fish in Clay Pot)': 'ca-kho-to.jpg',
    'Thit Kho (Caramelized Pork and Eggs)': 'thit-kho.jpg',
    'Canh Chua (Sour Soup)': 'canh-chua.jpg',
    'Bo Luc Lac (Shaking Beef)': 'bo-luc-lac.jpg',
}

for r in recipes:
    r['image'] = IMAGE_MAP.get(r['name'], 'default.jpg')

class RecipeChatbot:
    def __init__(self, recipes):
        self.recipes = recipes
    
    def find_recipes(self, user_input):
        # 1. Normalize query: Lowercase + Remove accents
        raw_query = user_input.lower().strip()
        clean_query = remove_accents(raw_query)  # e.g., "phở bò" -> "pho bo"
        
        matches = []
        
        # Logic filters
        is_quick = any(w in clean_query for w in ['nhanh', 'quick', 'fast', '30 mins'])
        is_easy = any(w in clean_query for w in ['de', 'easy', 'simple']) # 'dễ' -> 'de'

        for recipe in self.recipes:
            score = 0
            
            # Prepare data for comparison
            name_accent = recipe['name'].lower()               # Original Name
            name_no_accent = remove_accents(name_accent)       # Unaccented Name
            
            # --- COMPARISON LOGIC ---
            
            # 1. Compare with Unaccented Name (Primary)
            # This helps "phở bò" match "Pho Bo" perfectly
            ratio_no_accent = fuzz.partial_ratio(clean_query, name_no_accent)
            
            # 2. Compare with Original Name (Secondary)
            # This helps if data actually has accents
            ratio_accent = fuzz.partial_ratio(raw_query, name_accent)
            
            # Take the higher score
            final_ratio = max(ratio_no_accent, ratio_accent)
            
            if final_ratio > 75: 
                score += final_ratio * 1.5
            
            # 3. Search in Ingredients (Normalize)
            ing_score = 0
            for ing in recipe['ingredients']:
                ing_clean = remove_accents(ing.lower())
                if fuzz.partial_ratio(clean_query, ing_clean) > 80:
                    ing_score += 15
            score += min(ing_score, 60)

            # 4. Filters
            if is_quick and recipe.get('time', 999) <= 30: score += 25
            if is_easy and 'easy' in recipe.get('difficulty', '').lower(): score += 25

            if score > 50: # Slightly higher threshold now that matching is better
                matches.append({'recipe': recipe, 'score': score})
        
        matches.sort(key=lambda x: x['score'], reverse=True)
        return [m['recipe'] for m in matches[:5]]

    def generate_response(self, user_input):
        # Normalize input for keyword checks
        query = remove_accents(user_input.lower().strip())
        
        # 1. Greeting
        if any(w in query for w in ['hi', 'hello', 'chao', 'xin chao']):
            return {'type': 'greeting', 'text': "Xin chào! 👋 Bạn muốn nấu món gì hôm nay? (Phở, Bánh mì...)"}
            
        # 2. Random
        if any(w in query for w in ['random', 'goi y', 'bat ky']):
            chosen = random.choice(self.recipes)
            return {'type': 'recipe', 'text': "🎉 Hôm nay hãy thử món này nhé:", 'recipe': chosen}

        # 3. Calories
        if 'calo' in query or 'calories' in query:
            import re
            nums = re.findall(r'\d+', query)
            if nums:
                limit = int(nums[0])
                matches = [r for r in self.recipes if r.get('calories', 9999) <= limit]
                if matches:
                    return {'type': 'multiple', 'text': f"🥗 Các món dưới {limit} calo:", 'recipes': matches[:5]}

        # 4. Search
        matches = self.find_recipes(user_input) # Pass original input
        
        if not matches:
            return {
                'type': 'not_found',
                'text': f"Hmm, tôi chưa tìm thấy món '{user_input}'. Hãy thử tên khác hoặc kiểm tra chính tả xem sao?"
            }
        
        if len(matches) == 1:
            return {'type': 'recipe', 'text': f"✨ Tìm thấy món này:", 'recipe': matches[0]}
            
        return {'type': 'multiple', 'text': f"🔍 Tìm thấy {len(matches)} món liên quan:", 'recipes': matches}

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