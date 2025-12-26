// Generated from c:/Users/Chien/Downloads/vietnamese-recipe/Recipe.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class RecipeParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		RECIPE_KEYWORD=1, REGION_KEYWORD=2, TIME_KEYWORD=3, SERVINGS_KEYWORD=4, 
		DIFFICULTY_KEYWORD=5, CATEGORY_KEYWORD=6, INGREDIENTS_KEYWORD=7, STEPS_KEYWORD=8, 
		NORTHERN=9, CENTRAL=10, SOUTHERN=11, EASY=12, MEDIUM=13, HARD=14, DASH=15, 
		SEP=16, NEWLINE=17, NUMBER=18, WS=19, TEXT=20;
	public static final int
		RULE_recipes = 0, RULE_recipe = 1, RULE_recipeName = 2, RULE_region = 3, 
		RULE_time = 4, RULE_servings = 5, RULE_difficulty = 6, RULE_category = 7, 
		RULE_ingredients = 8, RULE_ingredient = 9, RULE_steps = 10, RULE_step = 11;
	private static String[] makeRuleNames() {
		return new String[] {
			"recipes", "recipe", "recipeName", "region", "time", "servings", "difficulty", 
			"category", "ingredients", "ingredient", "steps", "step"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'RECIPE'", "'REGION'", "'TIME'", "'SERVINGS'", "'DIFFICULTY'", 
			"'CATEGORY'", "'INGREDIENTS'", "'STEPS'", "'Northern'", "'Central'", 
			"'Southern'", "'Easy'", "'Medium'", "'Hard'", "'-'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "RECIPE_KEYWORD", "REGION_KEYWORD", "TIME_KEYWORD", "SERVINGS_KEYWORD", 
			"DIFFICULTY_KEYWORD", "CATEGORY_KEYWORD", "INGREDIENTS_KEYWORD", "STEPS_KEYWORD", 
			"NORTHERN", "CENTRAL", "SOUTHERN", "EASY", "MEDIUM", "HARD", "DASH", 
			"SEP", "NEWLINE", "NUMBER", "WS", "TEXT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Recipe.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public RecipeParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RecipesContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(RecipeParser.EOF, 0); }
		public List<RecipeContext> recipe() {
			return getRuleContexts(RecipeContext.class);
		}
		public RecipeContext recipe(int i) {
			return getRuleContext(RecipeContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(RecipeParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(RecipeParser.NEWLINE, i);
		}
		public RecipesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_recipes; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).enterRecipes(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).exitRecipes(this);
		}
	}

	public final RecipesContext recipes() throws RecognitionException {
		RecipesContext _localctx = new RecipesContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_recipes);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==RECIPE_KEYWORD) {
				{
				{
				setState(24);
				recipe();
				setState(28);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==NEWLINE) {
					{
					{
					setState(25);
					match(NEWLINE);
					}
					}
					setState(30);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				}
				setState(35);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(36);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RecipeContext extends ParserRuleContext {
		public TerminalNode RECIPE_KEYWORD() { return getToken(RecipeParser.RECIPE_KEYWORD, 0); }
		public List<TerminalNode> SEP() { return getTokens(RecipeParser.SEP); }
		public TerminalNode SEP(int i) {
			return getToken(RecipeParser.SEP, i);
		}
		public RecipeNameContext recipeName() {
			return getRuleContext(RecipeNameContext.class,0);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(RecipeParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(RecipeParser.NEWLINE, i);
		}
		public TerminalNode REGION_KEYWORD() { return getToken(RecipeParser.REGION_KEYWORD, 0); }
		public RegionContext region() {
			return getRuleContext(RegionContext.class,0);
		}
		public TerminalNode TIME_KEYWORD() { return getToken(RecipeParser.TIME_KEYWORD, 0); }
		public TimeContext time() {
			return getRuleContext(TimeContext.class,0);
		}
		public TerminalNode SERVINGS_KEYWORD() { return getToken(RecipeParser.SERVINGS_KEYWORD, 0); }
		public ServingsContext servings() {
			return getRuleContext(ServingsContext.class,0);
		}
		public TerminalNode DIFFICULTY_KEYWORD() { return getToken(RecipeParser.DIFFICULTY_KEYWORD, 0); }
		public DifficultyContext difficulty() {
			return getRuleContext(DifficultyContext.class,0);
		}
		public TerminalNode CATEGORY_KEYWORD() { return getToken(RecipeParser.CATEGORY_KEYWORD, 0); }
		public CategoryContext category() {
			return getRuleContext(CategoryContext.class,0);
		}
		public TerminalNode INGREDIENTS_KEYWORD() { return getToken(RecipeParser.INGREDIENTS_KEYWORD, 0); }
		public IngredientsContext ingredients() {
			return getRuleContext(IngredientsContext.class,0);
		}
		public TerminalNode STEPS_KEYWORD() { return getToken(RecipeParser.STEPS_KEYWORD, 0); }
		public StepsContext steps() {
			return getRuleContext(StepsContext.class,0);
		}
		public RecipeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_recipe; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).enterRecipe(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).exitRecipe(this);
		}
	}

	public final RecipeContext recipe() throws RecognitionException {
		RecipeContext _localctx = new RecipeContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_recipe);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			match(RECIPE_KEYWORD);
			setState(39);
			match(SEP);
			setState(40);
			recipeName();
			setState(41);
			match(NEWLINE);
			setState(42);
			match(REGION_KEYWORD);
			setState(43);
			match(SEP);
			setState(44);
			region();
			setState(45);
			match(NEWLINE);
			setState(46);
			match(TIME_KEYWORD);
			setState(47);
			match(SEP);
			setState(48);
			time();
			setState(49);
			match(NEWLINE);
			setState(50);
			match(SERVINGS_KEYWORD);
			setState(51);
			match(SEP);
			setState(52);
			servings();
			setState(53);
			match(NEWLINE);
			setState(54);
			match(DIFFICULTY_KEYWORD);
			setState(55);
			match(SEP);
			setState(56);
			difficulty();
			setState(57);
			match(NEWLINE);
			setState(58);
			match(CATEGORY_KEYWORD);
			setState(59);
			match(SEP);
			setState(60);
			category();
			setState(61);
			match(NEWLINE);
			setState(62);
			match(INGREDIENTS_KEYWORD);
			setState(63);
			match(SEP);
			setState(64);
			match(NEWLINE);
			setState(65);
			ingredients();
			setState(66);
			match(STEPS_KEYWORD);
			setState(67);
			match(SEP);
			setState(68);
			match(NEWLINE);
			setState(69);
			steps();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RecipeNameContext extends ParserRuleContext {
		public TerminalNode TEXT() { return getToken(RecipeParser.TEXT, 0); }
		public RecipeNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_recipeName; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).enterRecipeName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).exitRecipeName(this);
		}
	}

	public final RecipeNameContext recipeName() throws RecognitionException {
		RecipeNameContext _localctx = new RecipeNameContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_recipeName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			match(TEXT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RegionContext extends ParserRuleContext {
		public TerminalNode NORTHERN() { return getToken(RecipeParser.NORTHERN, 0); }
		public TerminalNode CENTRAL() { return getToken(RecipeParser.CENTRAL, 0); }
		public TerminalNode SOUTHERN() { return getToken(RecipeParser.SOUTHERN, 0); }
		public RegionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_region; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).enterRegion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).exitRegion(this);
		}
	}

	public final RegionContext region() throws RecognitionException {
		RegionContext _localctx = new RegionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_region);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(73);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3584L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TimeContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(RecipeParser.NUMBER, 0); }
		public TimeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_time; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).enterTime(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).exitTime(this);
		}
	}

	public final TimeContext time() throws RecognitionException {
		TimeContext _localctx = new TimeContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_time);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(NUMBER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ServingsContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(RecipeParser.NUMBER, 0); }
		public ServingsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_servings; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).enterServings(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).exitServings(this);
		}
	}

	public final ServingsContext servings() throws RecognitionException {
		ServingsContext _localctx = new ServingsContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_servings);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			match(NUMBER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DifficultyContext extends ParserRuleContext {
		public TerminalNode EASY() { return getToken(RecipeParser.EASY, 0); }
		public TerminalNode MEDIUM() { return getToken(RecipeParser.MEDIUM, 0); }
		public TerminalNode HARD() { return getToken(RecipeParser.HARD, 0); }
		public DifficultyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_difficulty; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).enterDifficulty(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).exitDifficulty(this);
		}
	}

	public final DifficultyContext difficulty() throws RecognitionException {
		DifficultyContext _localctx = new DifficultyContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_difficulty);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 28672L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CategoryContext extends ParserRuleContext {
		public TerminalNode TEXT() { return getToken(RecipeParser.TEXT, 0); }
		public CategoryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_category; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).enterCategory(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).exitCategory(this);
		}
	}

	public final CategoryContext category() throws RecognitionException {
		CategoryContext _localctx = new CategoryContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_category);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			match(TEXT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IngredientsContext extends ParserRuleContext {
		public List<IngredientContext> ingredient() {
			return getRuleContexts(IngredientContext.class);
		}
		public IngredientContext ingredient(int i) {
			return getRuleContext(IngredientContext.class,i);
		}
		public IngredientsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ingredients; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).enterIngredients(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).exitIngredients(this);
		}
	}

	public final IngredientsContext ingredients() throws RecognitionException {
		IngredientsContext _localctx = new IngredientsContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_ingredients);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(83);
				ingredient();
				}
				}
				setState(86); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==DASH );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IngredientContext extends ParserRuleContext {
		public TerminalNode DASH() { return getToken(RecipeParser.DASH, 0); }
		public TerminalNode TEXT() { return getToken(RecipeParser.TEXT, 0); }
		public TerminalNode NEWLINE() { return getToken(RecipeParser.NEWLINE, 0); }
		public List<TerminalNode> WS() { return getTokens(RecipeParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(RecipeParser.WS, i);
		}
		public IngredientContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ingredient; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).enterIngredient(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).exitIngredient(this);
		}
	}

	public final IngredientContext ingredient() throws RecognitionException {
		IngredientContext _localctx = new IngredientContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_ingredient);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			match(DASH);
			setState(92);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==WS) {
				{
				{
				setState(89);
				match(WS);
				}
				}
				setState(94);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(95);
			match(TEXT);
			setState(96);
			match(NEWLINE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StepsContext extends ParserRuleContext {
		public List<StepContext> step() {
			return getRuleContexts(StepContext.class);
		}
		public StepContext step(int i) {
			return getRuleContext(StepContext.class,i);
		}
		public StepsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_steps; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).enterSteps(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).exitSteps(this);
		}
	}

	public final StepsContext steps() throws RecognitionException {
		StepsContext _localctx = new StepsContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_steps);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(98);
				step();
				}
				}
				setState(101); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==DASH );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StepContext extends ParserRuleContext {
		public TerminalNode DASH() { return getToken(RecipeParser.DASH, 0); }
		public TerminalNode TEXT() { return getToken(RecipeParser.TEXT, 0); }
		public TerminalNode NEWLINE() { return getToken(RecipeParser.NEWLINE, 0); }
		public List<TerminalNode> WS() { return getTokens(RecipeParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(RecipeParser.WS, i);
		}
		public StepContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_step; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).enterStep(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RecipeListener ) ((RecipeListener)listener).exitStep(this);
		}
	}

	public final StepContext step() throws RecognitionException {
		StepContext _localctx = new StepContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_step);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			match(DASH);
			setState(107);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==WS) {
				{
				{
				setState(104);
				match(WS);
				}
				}
				setState(109);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(110);
			match(TEXT);
			setState(111);
			match(NEWLINE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0014r\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0001"+
		"\u0000\u0001\u0000\u0005\u0000\u001b\b\u0000\n\u0000\f\u0000\u001e\t\u0000"+
		"\u0005\u0000 \b\u0000\n\u0000\f\u0000#\t\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0004\bU\b\b\u000b\b\f\b"+
		"V\u0001\t\u0001\t\u0005\t[\b\t\n\t\f\t^\t\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\n\u0004\nd\b\n\u000b\n\f\ne\u0001\u000b\u0001\u000b\u0005\u000bj\b\u000b"+
		"\n\u000b\f\u000bm\t\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0000\u0000\f\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016"+
		"\u0000\u0002\u0001\u0000\t\u000b\u0001\u0000\f\u000ek\u0000!\u0001\u0000"+
		"\u0000\u0000\u0002&\u0001\u0000\u0000\u0000\u0004G\u0001\u0000\u0000\u0000"+
		"\u0006I\u0001\u0000\u0000\u0000\bK\u0001\u0000\u0000\u0000\nM\u0001\u0000"+
		"\u0000\u0000\fO\u0001\u0000\u0000\u0000\u000eQ\u0001\u0000\u0000\u0000"+
		"\u0010T\u0001\u0000\u0000\u0000\u0012X\u0001\u0000\u0000\u0000\u0014c"+
		"\u0001\u0000\u0000\u0000\u0016g\u0001\u0000\u0000\u0000\u0018\u001c\u0003"+
		"\u0002\u0001\u0000\u0019\u001b\u0005\u0011\u0000\u0000\u001a\u0019\u0001"+
		"\u0000\u0000\u0000\u001b\u001e\u0001\u0000\u0000\u0000\u001c\u001a\u0001"+
		"\u0000\u0000\u0000\u001c\u001d\u0001\u0000\u0000\u0000\u001d \u0001\u0000"+
		"\u0000\u0000\u001e\u001c\u0001\u0000\u0000\u0000\u001f\u0018\u0001\u0000"+
		"\u0000\u0000 #\u0001\u0000\u0000\u0000!\u001f\u0001\u0000\u0000\u0000"+
		"!\"\u0001\u0000\u0000\u0000\"$\u0001\u0000\u0000\u0000#!\u0001\u0000\u0000"+
		"\u0000$%\u0005\u0000\u0000\u0001%\u0001\u0001\u0000\u0000\u0000&\'\u0005"+
		"\u0001\u0000\u0000\'(\u0005\u0010\u0000\u0000()\u0003\u0004\u0002\u0000"+
		")*\u0005\u0011\u0000\u0000*+\u0005\u0002\u0000\u0000+,\u0005\u0010\u0000"+
		"\u0000,-\u0003\u0006\u0003\u0000-.\u0005\u0011\u0000\u0000./\u0005\u0003"+
		"\u0000\u0000/0\u0005\u0010\u0000\u000001\u0003\b\u0004\u000012\u0005\u0011"+
		"\u0000\u000023\u0005\u0004\u0000\u000034\u0005\u0010\u0000\u000045\u0003"+
		"\n\u0005\u000056\u0005\u0011\u0000\u000067\u0005\u0005\u0000\u000078\u0005"+
		"\u0010\u0000\u000089\u0003\f\u0006\u00009:\u0005\u0011\u0000\u0000:;\u0005"+
		"\u0006\u0000\u0000;<\u0005\u0010\u0000\u0000<=\u0003\u000e\u0007\u0000"+
		"=>\u0005\u0011\u0000\u0000>?\u0005\u0007\u0000\u0000?@\u0005\u0010\u0000"+
		"\u0000@A\u0005\u0011\u0000\u0000AB\u0003\u0010\b\u0000BC\u0005\b\u0000"+
		"\u0000CD\u0005\u0010\u0000\u0000DE\u0005\u0011\u0000\u0000EF\u0003\u0014"+
		"\n\u0000F\u0003\u0001\u0000\u0000\u0000GH\u0005\u0014\u0000\u0000H\u0005"+
		"\u0001\u0000\u0000\u0000IJ\u0007\u0000\u0000\u0000J\u0007\u0001\u0000"+
		"\u0000\u0000KL\u0005\u0012\u0000\u0000L\t\u0001\u0000\u0000\u0000MN\u0005"+
		"\u0012\u0000\u0000N\u000b\u0001\u0000\u0000\u0000OP\u0007\u0001\u0000"+
		"\u0000P\r\u0001\u0000\u0000\u0000QR\u0005\u0014\u0000\u0000R\u000f\u0001"+
		"\u0000\u0000\u0000SU\u0003\u0012\t\u0000TS\u0001\u0000\u0000\u0000UV\u0001"+
		"\u0000\u0000\u0000VT\u0001\u0000\u0000\u0000VW\u0001\u0000\u0000\u0000"+
		"W\u0011\u0001\u0000\u0000\u0000X\\\u0005\u000f\u0000\u0000Y[\u0005\u0013"+
		"\u0000\u0000ZY\u0001\u0000\u0000\u0000[^\u0001\u0000\u0000\u0000\\Z\u0001"+
		"\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000]_\u0001\u0000\u0000\u0000"+
		"^\\\u0001\u0000\u0000\u0000_`\u0005\u0014\u0000\u0000`a\u0005\u0011\u0000"+
		"\u0000a\u0013\u0001\u0000\u0000\u0000bd\u0003\u0016\u000b\u0000cb\u0001"+
		"\u0000\u0000\u0000de\u0001\u0000\u0000\u0000ec\u0001\u0000\u0000\u0000"+
		"ef\u0001\u0000\u0000\u0000f\u0015\u0001\u0000\u0000\u0000gk\u0005\u000f"+
		"\u0000\u0000hj\u0005\u0013\u0000\u0000ih\u0001\u0000\u0000\u0000jm\u0001"+
		"\u0000\u0000\u0000ki\u0001\u0000\u0000\u0000kl\u0001\u0000\u0000\u0000"+
		"ln\u0001\u0000\u0000\u0000mk\u0001\u0000\u0000\u0000no\u0005\u0014\u0000"+
		"\u0000op\u0005\u0011\u0000\u0000p\u0017\u0001\u0000\u0000\u0000\u0006"+
		"\u001c!V\\ek";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}