# Generated from Recipe.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RecipeParser import RecipeParser
else:
    from RecipeParser import RecipeParser

# This class defines a complete listener for a parse tree produced by RecipeParser.
class RecipeListener(ParseTreeListener):

    # Enter a parse tree produced by RecipeParser#recipes.
    def enterRecipes(self, ctx:RecipeParser.RecipesContext):
        pass

    # Exit a parse tree produced by RecipeParser#recipes.
    def exitRecipes(self, ctx:RecipeParser.RecipesContext):
        pass


    # Enter a parse tree produced by RecipeParser#flexibleText.
    def enterFlexibleText(self, ctx:RecipeParser.FlexibleTextContext):
        pass

    # Exit a parse tree produced by RecipeParser#flexibleText.
    def exitFlexibleText(self, ctx:RecipeParser.FlexibleTextContext):
        pass


    # Enter a parse tree produced by RecipeParser#recipe.
    def enterRecipe(self, ctx:RecipeParser.RecipeContext):
        pass

    # Exit a parse tree produced by RecipeParser#recipe.
    def exitRecipe(self, ctx:RecipeParser.RecipeContext):
        pass


    # Enter a parse tree produced by RecipeParser#recipeName.
    def enterRecipeName(self, ctx:RecipeParser.RecipeNameContext):
        pass

    # Exit a parse tree produced by RecipeParser#recipeName.
    def exitRecipeName(self, ctx:RecipeParser.RecipeNameContext):
        pass


    # Enter a parse tree produced by RecipeParser#image.
    def enterImage(self, ctx:RecipeParser.ImageContext):
        pass

    # Exit a parse tree produced by RecipeParser#image.
    def exitImage(self, ctx:RecipeParser.ImageContext):
        pass


    # Enter a parse tree produced by RecipeParser#region.
    def enterRegion(self, ctx:RecipeParser.RegionContext):
        pass

    # Exit a parse tree produced by RecipeParser#region.
    def exitRegion(self, ctx:RecipeParser.RegionContext):
        pass


    # Enter a parse tree produced by RecipeParser#time.
    def enterTime(self, ctx:RecipeParser.TimeContext):
        pass

    # Exit a parse tree produced by RecipeParser#time.
    def exitTime(self, ctx:RecipeParser.TimeContext):
        pass


    # Enter a parse tree produced by RecipeParser#servings.
    def enterServings(self, ctx:RecipeParser.ServingsContext):
        pass

    # Exit a parse tree produced by RecipeParser#servings.
    def exitServings(self, ctx:RecipeParser.ServingsContext):
        pass


    # Enter a parse tree produced by RecipeParser#calories.
    def enterCalories(self, ctx:RecipeParser.CaloriesContext):
        pass

    # Exit a parse tree produced by RecipeParser#calories.
    def exitCalories(self, ctx:RecipeParser.CaloriesContext):
        pass


    # Enter a parse tree produced by RecipeParser#difficulty.
    def enterDifficulty(self, ctx:RecipeParser.DifficultyContext):
        pass

    # Exit a parse tree produced by RecipeParser#difficulty.
    def exitDifficulty(self, ctx:RecipeParser.DifficultyContext):
        pass


    # Enter a parse tree produced by RecipeParser#category.
    def enterCategory(self, ctx:RecipeParser.CategoryContext):
        pass

    # Exit a parse tree produced by RecipeParser#category.
    def exitCategory(self, ctx:RecipeParser.CategoryContext):
        pass


    # Enter a parse tree produced by RecipeParser#tags.
    def enterTags(self, ctx:RecipeParser.TagsContext):
        pass

    # Exit a parse tree produced by RecipeParser#tags.
    def exitTags(self, ctx:RecipeParser.TagsContext):
        pass


    # Enter a parse tree produced by RecipeParser#ingredients.
    def enterIngredients(self, ctx:RecipeParser.IngredientsContext):
        pass

    # Exit a parse tree produced by RecipeParser#ingredients.
    def exitIngredients(self, ctx:RecipeParser.IngredientsContext):
        pass


    # Enter a parse tree produced by RecipeParser#ingredient.
    def enterIngredient(self, ctx:RecipeParser.IngredientContext):
        pass

    # Exit a parse tree produced by RecipeParser#ingredient.
    def exitIngredient(self, ctx:RecipeParser.IngredientContext):
        pass


    # Enter a parse tree produced by RecipeParser#steps.
    def enterSteps(self, ctx:RecipeParser.StepsContext):
        pass

    # Exit a parse tree produced by RecipeParser#steps.
    def exitSteps(self, ctx:RecipeParser.StepsContext):
        pass


    # Enter a parse tree produced by RecipeParser#step.
    def enterStep(self, ctx:RecipeParser.StepContext):
        pass

    # Exit a parse tree produced by RecipeParser#step.
    def exitStep(self, ctx:RecipeParser.StepContext):
        pass



del RecipeParser