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
        self.current_recipe = {}

    def exitRecipeName(self, ctx):
        self.current_recipe['name'] = ctx.getText().strip()

    def exitRegion(self, ctx):
        self.current_recipe['region'] = ctx.getText().strip()

    def exitTime(self, ctx):
        self.current_recipe['time'] = int(ctx.getText().strip())

    def exitServings(self, ctx):
        self.current_recipe['servings'] = int(ctx.getText().strip())
        
    def exitCalories(self, ctx): # [MỚI]
        self.current_recipe['calories'] = int(ctx.getText().strip())

    def exitDifficulty(self, ctx):
        self.current_recipe['difficulty'] = ctx.getText().strip()

    def exitCategory(self, ctx):
        self.current_recipe['category'] = ctx.getText().strip()
        
    def exitTags(self, ctx): # [MỚI]
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
        # Loại bỏ dấu gạch ngang đầu dòng
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
        self.recipes.append(self.current_recipe)

def load_recipes_from_folder(folder_path):
    """Đọc tất cả file .txt trong folder và parse"""
    combined_text = ""
    
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found!")
        return []

    # Ghép nội dung tất cả file lại
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            path = os.path.join(folder_path, filename)
            with open(path, 'r', encoding='utf-8') as f:
                combined_text += f.read() + "\n"

    if not combined_text:
        return []

    # ANTLR setup
    input_stream = InputStream(combined_text)
    lexer = RecipeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = RecipeParser(stream)
    tree = parser.recipes()

    # Walk the tree
    loader = RecipeLoader()
    walker = ParseTreeWalker()
    walker.walk(loader, tree)
    
    return loader.recipes