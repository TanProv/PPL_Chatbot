// Generated from c:/Users/Chien/Downloads/vietnamese-recipe/Recipe.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link RecipeParser}.
 */
public interface RecipeListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link RecipeParser#recipes}.
	 * @param ctx the parse tree
	 */
	void enterRecipes(RecipeParser.RecipesContext ctx);
	/**
	 * Exit a parse tree produced by {@link RecipeParser#recipes}.
	 * @param ctx the parse tree
	 */
	void exitRecipes(RecipeParser.RecipesContext ctx);
	/**
	 * Enter a parse tree produced by {@link RecipeParser#recipe}.
	 * @param ctx the parse tree
	 */
	void enterRecipe(RecipeParser.RecipeContext ctx);
	/**
	 * Exit a parse tree produced by {@link RecipeParser#recipe}.
	 * @param ctx the parse tree
	 */
	void exitRecipe(RecipeParser.RecipeContext ctx);
	/**
	 * Enter a parse tree produced by {@link RecipeParser#recipeName}.
	 * @param ctx the parse tree
	 */
	void enterRecipeName(RecipeParser.RecipeNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link RecipeParser#recipeName}.
	 * @param ctx the parse tree
	 */
	void exitRecipeName(RecipeParser.RecipeNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link RecipeParser#region}.
	 * @param ctx the parse tree
	 */
	void enterRegion(RecipeParser.RegionContext ctx);
	/**
	 * Exit a parse tree produced by {@link RecipeParser#region}.
	 * @param ctx the parse tree
	 */
	void exitRegion(RecipeParser.RegionContext ctx);
	/**
	 * Enter a parse tree produced by {@link RecipeParser#time}.
	 * @param ctx the parse tree
	 */
	void enterTime(RecipeParser.TimeContext ctx);
	/**
	 * Exit a parse tree produced by {@link RecipeParser#time}.
	 * @param ctx the parse tree
	 */
	void exitTime(RecipeParser.TimeContext ctx);
	/**
	 * Enter a parse tree produced by {@link RecipeParser#servings}.
	 * @param ctx the parse tree
	 */
	void enterServings(RecipeParser.ServingsContext ctx);
	/**
	 * Exit a parse tree produced by {@link RecipeParser#servings}.
	 * @param ctx the parse tree
	 */
	void exitServings(RecipeParser.ServingsContext ctx);
	/**
	 * Enter a parse tree produced by {@link RecipeParser#difficulty}.
	 * @param ctx the parse tree
	 */
	void enterDifficulty(RecipeParser.DifficultyContext ctx);
	/**
	 * Exit a parse tree produced by {@link RecipeParser#difficulty}.
	 * @param ctx the parse tree
	 */
	void exitDifficulty(RecipeParser.DifficultyContext ctx);
	/**
	 * Enter a parse tree produced by {@link RecipeParser#category}.
	 * @param ctx the parse tree
	 */
	void enterCategory(RecipeParser.CategoryContext ctx);
	/**
	 * Exit a parse tree produced by {@link RecipeParser#category}.
	 * @param ctx the parse tree
	 */
	void exitCategory(RecipeParser.CategoryContext ctx);
	/**
	 * Enter a parse tree produced by {@link RecipeParser#ingredients}.
	 * @param ctx the parse tree
	 */
	void enterIngredients(RecipeParser.IngredientsContext ctx);
	/**
	 * Exit a parse tree produced by {@link RecipeParser#ingredients}.
	 * @param ctx the parse tree
	 */
	void exitIngredients(RecipeParser.IngredientsContext ctx);
	/**
	 * Enter a parse tree produced by {@link RecipeParser#ingredient}.
	 * @param ctx the parse tree
	 */
	void enterIngredient(RecipeParser.IngredientContext ctx);
	/**
	 * Exit a parse tree produced by {@link RecipeParser#ingredient}.
	 * @param ctx the parse tree
	 */
	void exitIngredient(RecipeParser.IngredientContext ctx);
	/**
	 * Enter a parse tree produced by {@link RecipeParser#steps}.
	 * @param ctx the parse tree
	 */
	void enterSteps(RecipeParser.StepsContext ctx);
	/**
	 * Exit a parse tree produced by {@link RecipeParser#steps}.
	 * @param ctx the parse tree
	 */
	void exitSteps(RecipeParser.StepsContext ctx);
	/**
	 * Enter a parse tree produced by {@link RecipeParser#step}.
	 * @param ctx the parse tree
	 */
	void enterStep(RecipeParser.StepContext ctx);
	/**
	 * Exit a parse tree produced by {@link RecipeParser#step}.
	 * @param ctx the parse tree
	 */
	void exitStep(RecipeParser.StepContext ctx);
}