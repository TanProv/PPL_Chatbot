import os
import sys
from antlr4 import *
from RecipeLexer import RecipeLexer
from RecipeParser import RecipeParser
from RecipeListener import RecipeListener

class RecipeLoader(RecipeListener):
    def __init__(self):
        self.recipes = []
        self.current_recipe = {}
        self.current_list = []

    def enterRecipe(self, ctx):
        self.current_recipe = {
            'ingredients': [],
            'steps': [],
            'tags': [],
            'image': 'default.jpg' # Ảnh mặc định
        }

    def exitRecipeName(self, ctx):
        self.current_recipe['name'] = ctx.getText().strip()

    def exitImage(self, ctx):
        self.current_recipe['image'] = ctx.getText().strip()

    def exitRegion(self, ctx):
        self.current_recipe['region'] = ctx.getText().strip()

    def exitTime(self, ctx):
        try:
            self.current_recipe['time'] = int(ctx.getText().strip())
        except ValueError:
            self.current_recipe['time'] = 0

    def exitServings(self, ctx):
        try:
            self.current_recipe['servings'] = int(ctx.getText().strip())
        except ValueError:
            self.current_recipe['servings'] = 0
        
    def exitCalories(self, ctx):
        try:
            self.current_recipe['calories'] = int(ctx.getText().strip())
        except ValueError:
            self.current_recipe['calories'] = 0

    def exitDifficulty(self, ctx):
        self.current_recipe['difficulty'] = ctx.getText().strip()

    def exitCategory(self, ctx):
        self.current_recipe['category'] = ctx.getText().strip()
        
    def exitTags(self, ctx):
        raw_tags = ctx.getText().strip()
        self.current_recipe['tags'] = [t.strip().lower() for t in raw_tags.split(',')]

    def enterIngredients(self, ctx):
        self.current_list = []

    def exitIngredients(self, ctx):
        self.current_recipe['ingredients'] = self.current_list[:]

    def enterSteps(self, ctx):
        self.current_list = []

    def exitSteps(self, ctx):
        self.current_recipe['steps'] = self.current_list[:]

    def exitIngredient(self, ctx):
        text = ctx.getText().strip()
        if text.startswith('-'):
            text = text[1:].strip()
        self.current_list.append(text)

    def exitStep(self, ctx):
        text = ctx.getText().strip()
        if text.startswith('-'):
            text = text[1:].strip()
        self.current_list.append(text)

    def exitRecipe(self, ctx):
        if 'name' in self.current_recipe:
            self.recipes.append(self.current_recipe)

def load_recipes_from_folder(folder_path):
    """Đọc tất cả file .txt trong folder và parse"""
    combined_text = ""
    
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found!")
        return []

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            path = os.path.join(folder_path, filename)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    combined_text += f.read() + "\n"
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    if not combined_text:
        return []

    # ANTLR setup
    input_stream = InputStream(combined_text)
    lexer = RecipeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = RecipeParser(stream)
    
    
    # parser.removeErrorListeners()
    
    tree = parser.recipes()

    # Walk the tree
    loader = RecipeLoader()
    walker = ParseTreeWalker()
    walker.walk(loader, tree)
    
    return loader.recipes