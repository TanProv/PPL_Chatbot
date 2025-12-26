from flask import Flask, render_template, request, jsonify, send_from_directory
from recipe_parser import parse_recipes
from recipes_data import RECIPES_DSL

app = Flask(__name__)

#how to run first  java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 Recipe.g4
#next run python app.py

# Parse all recipes on startup
print(" Parsing recipes with ANTLR4...")
recipes = parse_recipes(RECIPES_DSL)
print(f" Successfully parsed {len(recipes)} recipes!")

# Provide image filenames for each recipe name; place files under /images
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

# Attach images to parsed recipes
for r in recipes:
    r['image'] = IMAGE_MAP.get(r['name'], r.get('image', ''))

# Chatbot class
class RecipeChatbot:
    def __init__(self, recipes):
        self.recipes = recipes
    
    def find_recipes(self, user_input):
        """Find recipes matching user input"""
        query = user_input.lower().strip()
        matches = []
        
        for recipe in self.recipes:
            score = 0
            recipe_name = recipe['name'].lower()
            
            # Exact match
            if query in recipe_name:
                score += 100
            
            # Word matches
            words = query.split()
            for word in words:
                if len(word) > 2:
                    if word in recipe_name:
                        score += 10
                    # Check ingredients
                    for ing in recipe['ingredients']:
                        if word in ing.lower():
                            score += 5
            
            # Category/region/difficulty matches
            if query in recipe['category'].lower():
                score += 20
            if query in recipe['region'].lower():
                score += 20
            if query in recipe['difficulty'].lower():
                score += 15
            
            if score > 0:
                matches.append({'recipe': recipe, 'score': score})
        
        # Sort by score and return top 5
        matches.sort(key=lambda x: x['score'], reverse=True)
        return [m['recipe'] for m in matches[:5]]
    
    def generate_response(self, user_input):
        """Generate chatbot response"""
        query = user_input.lower().strip()
        
        # Greetings
        if any(word in query for word in ['hi', 'hello', 'hey', 'chao', 'xin chao']):
            return {
                'type': 'greeting',
                'text': "Xin chào!  I'm your Vietnamese Recipe Assistant powered by ANTLR4!\n\nI can help you find recipes, search by ingredients, filter by difficulty, and more!\n\nTry asking: 'How to make Pho?' or 'What can I make with shrimp?'"
            }
        
        # Help
        if 'help' in query or 'what can you' in query:
            return {
                'type': 'help',
                'text': " I can help you with:\n\n• Find recipes by name\n• Search by ingredients\n• Filter by difficulty (easy, medium, hard)\n• Filter by region (northern, central, southern)\n• Find quick meals\n\nJust ask me anything!"
            }
        
        # Search by ingredient
        if any(phrase in query for phrase in ['what can i make with', 'recipes with', 'using']):
            ingredient = query.replace('what can i make with', '').replace('recipes with', '').replace('using', '').strip()
            matches = [r for r in self.recipes if any(ingredient in ing.lower() for ing in r['ingredients'])]
            if matches:
                return {
                    'type': 'multiple',
                    'text': f"I found {len(matches)} recipe(s) using {ingredient}:",
                    'recipes': matches[:5]
                }
            else:
                return {
                    'type': 'not_found',
                    'text': f"I couldn't find recipes with '{ingredient}'. Try: shrimp, pork, chicken, beef, or rice."
                }
        
        # Filter by difficulty
        if any(word in query for word in ['easy', 'medium', 'hard', 'simple', 'quick']):
            difficulty = 'Easy'
            if 'medium' in query:
                difficulty = 'Medium'
            elif 'hard' in query or 'difficult' in query:
                difficulty = 'Hard'
            
            matches = [r for r in self.recipes if r['difficulty'] == difficulty]
            return {
                'type': 'multiple',
                'text': f"Here are {difficulty} recipes:",
                'recipes': matches[:5]
            }
        
        # Filter by time
        if 'quick' in query or 'fast' in query or 'minutes' in query:
            matches = [r for r in self.recipes if r['time'] <= 30]
            return {
                'type': 'multiple',
                'text': "Quick recipes (30 minutes or less):",
                'recipes': matches[:5]
            }
        
        # Filter by region
        if any(region in query for region in ['northern', 'central', 'southern']):
            region = 'Northern'
            if 'central' in query:
                region = 'Central'
            elif 'southern' in query:
                region = 'Southern'
            
            matches = [r for r in self.recipes if r['region'] == region]
            return {
                'type': 'multiple',
                'text': f"{region} Vietnamese dishes:",
                'recipes': matches[:5]
            }
        
        # List all
        if 'show all' in query or 'list' in query:
            categories = {}
            for r in self.recipes:
                cat = r['category']
                if cat not in categories:
                    categories[cat] = []
                categories[cat].append(r['name'])
            
            text = " Available Vietnamese Dishes:\n\n"
            for cat, names in categories.items():
                text += f"**{cat}:** {', '.join(names[:3])}...\n"
            
            return {'type': 'list', 'text': text}
        
        # Search for recipes
        matches = self.find_recipes(user_input)
        
        if not matches:
            return {
                'type': 'not_found',
                'text': " I couldn't find that recipe.\n\nTry: 'Pho', 'Banh Mi', 'Spring Rolls', 'Bun Cha', or 'Com Tam'"
            }
        
        if len(matches) == 1:
            return {
                'type': 'recipe',
                'text': f"Here's the recipe for {matches[0]['name']}:",
                'recipe': matches[0]
            }
        
        return {
            'type': 'multiple',
            'text': f"I found {len(matches)} matching recipes:",
            'recipes': matches
        }

# Initialize chatbot
chatbot = RecipeChatbot(recipes)

@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html', recipe_count=len(recipes))


@app.route('/chat')
def chat_page():
    """Render chat page"""
    return render_template('chat.html', recipe_count=len(recipes))


@app.route('/images/<path:filename>')
def serve_images(filename):
    """Serve images stored in the local images/ folder"""
    return send_from_directory('images', filename)

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    data = request.json
    user_message = data.get('message', '')
    
    response = chatbot.generate_response(user_message)
    return jsonify(response)

@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    """Get all recipes"""
    return jsonify(recipes)

if __name__ == '__main__':
    print("\n" + "="*50)
    print(" Vietnamese Recipe Chatbot")
    print("="*50)
    print(f" Loaded {len(recipes)} recipes")
    print(" Starting server...")
    print(" Open http://127.0.0.1:5000 in your browser")
    print("="*50 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)