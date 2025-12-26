from antlr4 import *
from RecipeLexer import RecipeLexer
from RecipeParser import RecipeParser
from RecipeListener import RecipeListener

class RecipeExtractor(RecipeListener):
    """Custom listener to extract recipe data from parse tree"""

    def __init__(self):
        self.recipe = {
            'name': '',
            'region': '',
            'time': 0,
            'servings': 0,
            'difficulty': '',
            'category': '',
            'image': '',
            'ingredients': [],
            'steps': []
        }

    def exitRecipeName(self, ctx):
        self.recipe['name'] = ctx.getText().strip()

    def exitRegion(self, ctx):
        self.recipe['region'] = ctx.getText()

    def exitTime(self, ctx):
        self.recipe['time'] = int(ctx.getText())

    def exitServings(self, ctx):
        self.recipe['servings'] = int(ctx.getText())

    def exitDifficulty(self, ctx):
        self.recipe['difficulty'] = ctx.getText()

    def exitCategory(self, ctx):
        self.recipe['category'] = ctx.getText().strip()

    def exitImage(self, ctx):
        self.recipe['image'] = ctx.getText().strip()

    def exitIngredient(self, ctx):
        ingredient_text = ctx.getText()[1:].strip()
        if ingredient_text:
            self.recipe['ingredients'].append(ingredient_text)

    def exitStep(self, ctx):
        step_text = ctx.getText()[1:].strip()
        if step_text:
            self.recipe['steps'].append(step_text)

    def get_recipe(self):
        return self.recipe


def parse_recipe(dsl_text):
    input_stream = InputStream(dsl_text)
    lexer = RecipeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = RecipeParser(token_stream)

    tree = parser.recipe()

    extractor = RecipeExtractor()
    walker = ParseTreeWalker()
    walker.walk(extractor, tree)

    return extractor.get_recipe()


def parse_recipes(dsl_list):
    recipes = []
    for dsl in dsl_list:
        try:
            recipes.append(parse_recipe(dsl))
        except Exception as e:
            print("Error parsing recipe:", e)
    return recipes
