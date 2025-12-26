from flask import Flask, render_template, request, jsonify, send_from_directory
from recipe_parser import load_recipes_from_folder
from thefuzz import fuzz, process 

app = Flask(__name__)

# --- CẤU HÌNH ---
DATA_FOLDER = './data'
IMAGE_FOLDER = './images'

# Load recipes
print("Loading recipes from data folder...")
recipes = load_recipes_from_folder(DATA_FOLDER)
print(f"Successfully loaded {len(recipes)} recipes!")

# Map ảnh thủ công (hoặc có thể tự động hóa dựa trên tên file)
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

# Gán ảnh vào recipe
for r in recipes:
    r['image'] = IMAGE_MAP.get(r['name'], 'default.jpg')

class RecipeChatbot:
    def __init__(self, recipes):
        self.recipes = recipes
    
    def find_recipes(self, user_input):
        """Tìm kiếm thông minh hơn với Fuzzy Matching"""
        query = user_input.lower().strip()
        matches = []
        
        for recipe in self.recipes:
            score = 0
            name = recipe['name'].lower()
            
            # 1. So sánh tên (Fuzzy Match) - Xử lý lỗi chính tả
            name_ratio = fuzz.partial_ratio(query, name)
            if name_ratio > 75: 
                score += name_ratio * 1.5 # Ưu tiên tên món
            
            # 2. Tìm trong Tags (MỚI)
            if 'tags' in recipe and any(tag in query for tag in recipe['tags']):
                score += 30

            # 3. Tìm trong Nguyên liệu
            ing_score = 0
            for ing in recipe['ingredients']:
                if fuzz.partial_ratio(query, ing.lower()) > 80:
                    ing_score += 10
            score += min(ing_score, 50) # Max 50 điểm cho nguyên liệu

            # 4. Tìm theo Category/Region
            if query in recipe['category'].lower(): score += 20
            if query in recipe['region'].lower(): score += 20
            
            if score > 40: # Ngưỡng tối thiểu để coi là match
                matches.append({'recipe': recipe, 'score': score})
        
        # Sắp xếp theo điểm số cao nhất
        matches.sort(key=lambda x: x['score'], reverse=True)
        return [m['recipe'] for m in matches[:5]]

    def generate_response(self, user_input):
        query = user_input.lower().strip()
        
        # --- XỬ LÝ INTENT CƠ BẢN ---
        
        # 1. Greeting
        if any(w in query for w in ['hi', 'hello', 'chao', 'xin chao']):
            return {'type': 'greeting', 'text': "Xin chào! Tôi là trợ lý nấu ăn thông minh. Bạn muốn tìm món gì hôm nay?"}
            
        # 2. Help
        if 'help' in query:
            return {'type': 'help', 'text': "Bạn có thể hỏi: 'Cách nấu Phở', 'Món nào dưới 500 calo?', 'Món chay', hoặc tìm bằng nguyên liệu."}

        # 3. [MỚI] Tìm theo Calories (VD: "dưới 500 calo")
        if 'calo' in query or 'calories' in query:
            # Logic đơn giản: tìm số trong câu query
            import re
            nums = re.findall(r'\d+', query)
            if nums:
                limit = int(nums[0])
                matches = [r for r in self.recipes if r.get('calories', 9999) <= limit]
                return {
                    'type': 'multiple', 
                    'text': f"Các món dưới {limit} calo:", 
                    'recipes': matches[:5]
                }

        # 4. List all
        if 'all' in query or 'tất cả' in query:
             return {
                'type': 'list',
                'text': "Danh sách các món ăn hiện có:\n" + ", ".join([r['name'] for r in self.recipes])
             }

        # --- TÌM KIẾM MÓN ĂN ---
        matches = self.find_recipes(user_input)
        
        if not matches:
            return {
                'type': 'not_found',
                'text': f"Xin lỗi, tôi không tìm thấy món nào phù hợp với '{user_input}'. Hãy thử từ khóa khác nhé!"
            }
        
        if len(matches) == 1:
            return {'type': 'recipe', 'text': f"Tìm thấy món {matches[0]['name']}:", 'recipe': matches[0]}
            
        return {'type': 'multiple', 'text': f"Tôi tìm thấy {len(matches)} món liên quan:", 'recipes': matches}

chatbot = RecipeChatbot(recipes)

# --- FLASK ROUTES ---

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

@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    return jsonify(recipes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)