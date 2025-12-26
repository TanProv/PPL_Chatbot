# Generated from Recipe.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("t\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\7\2\35\n\2\f\2\16\2 \13\2\7\2\"\n\2\f\2\16\2%\13\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write("\3\7\3\7\3\b\3\b\3\t\3\t\3\n\6\nW\n\n\r\n\16\nX\3\13\3")
        buf.write("\13\7\13]\n\13\f\13\16\13`\13\13\3\13\3\13\3\13\3\f\6")
        buf.write("\ff\n\f\r\f\16\fg\3\r\3\r\7\rl\n\r\f\r\16\ro\13\r\3\r")
        buf.write("\3\r\3\r\3\r\2\2\16\2\4\6\b\n\f\16\20\22\24\26\30\2\4")
        buf.write("\3\2\13\r\3\2\16\20\2m\2#\3\2\2\2\4(\3\2\2\2\6I\3\2\2")
        buf.write("\2\bK\3\2\2\2\nM\3\2\2\2\fO\3\2\2\2\16Q\3\2\2\2\20S\3")
        buf.write("\2\2\2\22V\3\2\2\2\24Z\3\2\2\2\26e\3\2\2\2\30i\3\2\2\2")
        buf.write("\32\36\5\4\3\2\33\35\7\23\2\2\34\33\3\2\2\2\35 \3\2\2")
        buf.write("\2\36\34\3\2\2\2\36\37\3\2\2\2\37\"\3\2\2\2 \36\3\2\2")
        buf.write("\2!\32\3\2\2\2\"%\3\2\2\2#!\3\2\2\2#$\3\2\2\2$&\3\2\2")
        buf.write("\2%#\3\2\2\2&\'\7\2\2\3\'\3\3\2\2\2()\7\3\2\2)*\7\22\2")
        buf.write("\2*+\5\6\4\2+,\7\23\2\2,-\7\4\2\2-.\7\22\2\2./\5\b\5\2")
        buf.write("/\60\7\23\2\2\60\61\7\5\2\2\61\62\7\22\2\2\62\63\5\n\6")
        buf.write("\2\63\64\7\23\2\2\64\65\7\6\2\2\65\66\7\22\2\2\66\67\5")
        buf.write("\f\7\2\678\7\23\2\289\7\7\2\29:\7\22\2\2:;\5\16\b\2;<")
        buf.write("\7\23\2\2<=\7\b\2\2=>\7\22\2\2>?\5\20\t\2?@\7\23\2\2@")
        buf.write("A\7\t\2\2AB\7\22\2\2BC\7\23\2\2CD\5\22\n\2DE\7\n\2\2E")
        buf.write("F\7\22\2\2FG\7\23\2\2GH\5\26\f\2H\5\3\2\2\2IJ\7\26\2\2")
        buf.write("J\7\3\2\2\2KL\t\2\2\2L\t\3\2\2\2MN\7\24\2\2N\13\3\2\2")
        buf.write("\2OP\7\24\2\2P\r\3\2\2\2QR\t\3\2\2R\17\3\2\2\2ST\7\26")
        buf.write("\2\2T\21\3\2\2\2UW\5\24\13\2VU\3\2\2\2WX\3\2\2\2XV\3\2")
        buf.write("\2\2XY\3\2\2\2Y\23\3\2\2\2Z^\7\21\2\2[]\7\25\2\2\\[\3")
        buf.write("\2\2\2]`\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_a\3\2\2\2`^\3\2")
        buf.write("\2\2ab\7\26\2\2bc\7\23\2\2c\25\3\2\2\2df\5\30\r\2ed\3")
        buf.write("\2\2\2fg\3\2\2\2ge\3\2\2\2gh\3\2\2\2h\27\3\2\2\2im\7\21")
        buf.write("\2\2jl\7\25\2\2kj\3\2\2\2lo\3\2\2\2mk\3\2\2\2mn\3\2\2")
        buf.write("\2np\3\2\2\2om\3\2\2\2pq\7\26\2\2qr\7\23\2\2r\31\3\2\2")
        buf.write("\2\b\36#X^gm")
        return buf.getvalue()


class RecipeParser ( Parser ):

    grammarFileName = "Recipe.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'RECIPE'", "'REGION'", "'TIME'", "'SERVINGS'", 
                     "'DIFFICULTY'", "'CATEGORY'", "'INGREDIENTS'", "'STEPS'", 
                     "'Northern'", "'Central'", "'Southern'", "'Easy'", 
                     "'Medium'", "'Hard'", "'-'" ]

    symbolicNames = [ "<INVALID>", "RECIPE_KEYWORD", "REGION_KEYWORD", "TIME_KEYWORD", 
                      "SERVINGS_KEYWORD", "DIFFICULTY_KEYWORD", "CATEGORY_KEYWORD", 
                      "INGREDIENTS_KEYWORD", "STEPS_KEYWORD", "NORTHERN", 
                      "CENTRAL", "SOUTHERN", "EASY", "MEDIUM", "HARD", "DASH", 
                      "SEP", "NEWLINE", "NUMBER", "WS", "TEXT" ]

    RULE_recipes = 0
    RULE_recipe = 1
    RULE_recipeName = 2
    RULE_region = 3
    RULE_time = 4
    RULE_servings = 5
    RULE_difficulty = 6
    RULE_category = 7
    RULE_ingredients = 8
    RULE_ingredient = 9
    RULE_steps = 10
    RULE_step = 11

    ruleNames =  [ "recipes", "recipe", "recipeName", "region", "time", 
                   "servings", "difficulty", "category", "ingredients", 
                   "ingredient", "steps", "step" ]

    EOF = Token.EOF
    RECIPE_KEYWORD=1
    REGION_KEYWORD=2
    TIME_KEYWORD=3
    SERVINGS_KEYWORD=4
    DIFFICULTY_KEYWORD=5
    CATEGORY_KEYWORD=6
    INGREDIENTS_KEYWORD=7
    STEPS_KEYWORD=8
    NORTHERN=9
    CENTRAL=10
    SOUTHERN=11
    EASY=12
    MEDIUM=13
    HARD=14
    DASH=15
    SEP=16
    NEWLINE=17
    NUMBER=18
    WS=19
    TEXT=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RecipesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(RecipeParser.EOF, 0)

        def recipe(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RecipeParser.RecipeContext)
            else:
                return self.getTypedRuleContext(RecipeParser.RecipeContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(RecipeParser.NEWLINE)
            else:
                return self.getToken(RecipeParser.NEWLINE, i)

        def getRuleIndex(self):
            return RecipeParser.RULE_recipes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecipes" ):
                listener.enterRecipes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecipes" ):
                listener.exitRecipes(self)




    def recipes(self):

        localctx = RecipeParser.RecipesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_recipes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RecipeParser.RECIPE_KEYWORD:
                self.state = 24
                self.recipe()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RecipeParser.NEWLINE:
                    self.state = 25
                    self.match(RecipeParser.NEWLINE)
                    self.state = 30
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 36
            self.match(RecipeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RECIPE_KEYWORD(self):
            return self.getToken(RecipeParser.RECIPE_KEYWORD, 0)

        def SEP(self, i:int=None):
            if i is None:
                return self.getTokens(RecipeParser.SEP)
            else:
                return self.getToken(RecipeParser.SEP, i)

        def recipeName(self):
            return self.getTypedRuleContext(RecipeParser.RecipeNameContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(RecipeParser.NEWLINE)
            else:
                return self.getToken(RecipeParser.NEWLINE, i)

        def REGION_KEYWORD(self):
            return self.getToken(RecipeParser.REGION_KEYWORD, 0)

        def region(self):
            return self.getTypedRuleContext(RecipeParser.RegionContext,0)


        def TIME_KEYWORD(self):
            return self.getToken(RecipeParser.TIME_KEYWORD, 0)

        def time(self):
            return self.getTypedRuleContext(RecipeParser.TimeContext,0)


        def SERVINGS_KEYWORD(self):
            return self.getToken(RecipeParser.SERVINGS_KEYWORD, 0)

        def servings(self):
            return self.getTypedRuleContext(RecipeParser.ServingsContext,0)


        def DIFFICULTY_KEYWORD(self):
            return self.getToken(RecipeParser.DIFFICULTY_KEYWORD, 0)

        def difficulty(self):
            return self.getTypedRuleContext(RecipeParser.DifficultyContext,0)


        def CATEGORY_KEYWORD(self):
            return self.getToken(RecipeParser.CATEGORY_KEYWORD, 0)

        def category(self):
            return self.getTypedRuleContext(RecipeParser.CategoryContext,0)


        def INGREDIENTS_KEYWORD(self):
            return self.getToken(RecipeParser.INGREDIENTS_KEYWORD, 0)

        def ingredients(self):
            return self.getTypedRuleContext(RecipeParser.IngredientsContext,0)


        def STEPS_KEYWORD(self):
            return self.getToken(RecipeParser.STEPS_KEYWORD, 0)

        def steps(self):
            return self.getTypedRuleContext(RecipeParser.StepsContext,0)


        def getRuleIndex(self):
            return RecipeParser.RULE_recipe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecipe" ):
                listener.enterRecipe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecipe" ):
                listener.exitRecipe(self)




    def recipe(self):

        localctx = RecipeParser.RecipeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_recipe)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(RecipeParser.RECIPE_KEYWORD)
            self.state = 39
            self.match(RecipeParser.SEP)
            self.state = 40
            self.recipeName()
            self.state = 41
            self.match(RecipeParser.NEWLINE)
            self.state = 42
            self.match(RecipeParser.REGION_KEYWORD)
            self.state = 43
            self.match(RecipeParser.SEP)
            self.state = 44
            self.region()
            self.state = 45
            self.match(RecipeParser.NEWLINE)
            self.state = 46
            self.match(RecipeParser.TIME_KEYWORD)
            self.state = 47
            self.match(RecipeParser.SEP)
            self.state = 48
            self.time()
            self.state = 49
            self.match(RecipeParser.NEWLINE)
            self.state = 50
            self.match(RecipeParser.SERVINGS_KEYWORD)
            self.state = 51
            self.match(RecipeParser.SEP)
            self.state = 52
            self.servings()
            self.state = 53
            self.match(RecipeParser.NEWLINE)
            self.state = 54
            self.match(RecipeParser.DIFFICULTY_KEYWORD)
            self.state = 55
            self.match(RecipeParser.SEP)
            self.state = 56
            self.difficulty()
            self.state = 57
            self.match(RecipeParser.NEWLINE)
            self.state = 58
            self.match(RecipeParser.CATEGORY_KEYWORD)
            self.state = 59
            self.match(RecipeParser.SEP)
            self.state = 60
            self.category()
            self.state = 61
            self.match(RecipeParser.NEWLINE)
            self.state = 62
            self.match(RecipeParser.INGREDIENTS_KEYWORD)
            self.state = 63
            self.match(RecipeParser.SEP)
            self.state = 64
            self.match(RecipeParser.NEWLINE)
            self.state = 65
            self.ingredients()
            self.state = 66
            self.match(RecipeParser.STEPS_KEYWORD)
            self.state = 67
            self.match(RecipeParser.SEP)
            self.state = 68
            self.match(RecipeParser.NEWLINE)
            self.state = 69
            self.steps()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecipeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(RecipeParser.TEXT, 0)

        def getRuleIndex(self):
            return RecipeParser.RULE_recipeName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecipeName" ):
                listener.enterRecipeName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecipeName" ):
                listener.exitRecipeName(self)




    def recipeName(self):

        localctx = RecipeParser.RecipeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_recipeName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(RecipeParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORTHERN(self):
            return self.getToken(RecipeParser.NORTHERN, 0)

        def CENTRAL(self):
            return self.getToken(RecipeParser.CENTRAL, 0)

        def SOUTHERN(self):
            return self.getToken(RecipeParser.SOUTHERN, 0)

        def getRuleIndex(self):
            return RecipeParser.RULE_region

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegion" ):
                listener.enterRegion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegion" ):
                listener.exitRegion(self)




    def region(self):

        localctx = RecipeParser.RegionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_region)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RecipeParser.NORTHERN) | (1 << RecipeParser.CENTRAL) | (1 << RecipeParser.SOUTHERN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(RecipeParser.NUMBER, 0)

        def getRuleIndex(self):
            return RecipeParser.RULE_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime" ):
                listener.enterTime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime" ):
                listener.exitTime(self)




    def time(self):

        localctx = RecipeParser.TimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(RecipeParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ServingsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(RecipeParser.NUMBER, 0)

        def getRuleIndex(self):
            return RecipeParser.RULE_servings

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterServings" ):
                listener.enterServings(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitServings" ):
                listener.exitServings(self)




    def servings(self):

        localctx = RecipeParser.ServingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_servings)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(RecipeParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DifficultyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EASY(self):
            return self.getToken(RecipeParser.EASY, 0)

        def MEDIUM(self):
            return self.getToken(RecipeParser.MEDIUM, 0)

        def HARD(self):
            return self.getToken(RecipeParser.HARD, 0)

        def getRuleIndex(self):
            return RecipeParser.RULE_difficulty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDifficulty" ):
                listener.enterDifficulty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDifficulty" ):
                listener.exitDifficulty(self)




    def difficulty(self):

        localctx = RecipeParser.DifficultyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_difficulty)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RecipeParser.EASY) | (1 << RecipeParser.MEDIUM) | (1 << RecipeParser.HARD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CategoryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(RecipeParser.TEXT, 0)

        def getRuleIndex(self):
            return RecipeParser.RULE_category

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCategory" ):
                listener.enterCategory(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCategory" ):
                listener.exitCategory(self)




    def category(self):

        localctx = RecipeParser.CategoryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_category)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(RecipeParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IngredientsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ingredient(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RecipeParser.IngredientContext)
            else:
                return self.getTypedRuleContext(RecipeParser.IngredientContext,i)


        def getRuleIndex(self):
            return RecipeParser.RULE_ingredients

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIngredients" ):
                listener.enterIngredients(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIngredients" ):
                listener.exitIngredients(self)




    def ingredients(self):

        localctx = RecipeParser.IngredientsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ingredients)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 83
                self.ingredient()
                self.state = 86 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==RecipeParser.DASH):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IngredientContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DASH(self):
            return self.getToken(RecipeParser.DASH, 0)

        def TEXT(self):
            return self.getToken(RecipeParser.TEXT, 0)

        def NEWLINE(self):
            return self.getToken(RecipeParser.NEWLINE, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(RecipeParser.WS)
            else:
                return self.getToken(RecipeParser.WS, i)

        def getRuleIndex(self):
            return RecipeParser.RULE_ingredient

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIngredient" ):
                listener.enterIngredient(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIngredient" ):
                listener.exitIngredient(self)




    def ingredient(self):

        localctx = RecipeParser.IngredientContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ingredient)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(RecipeParser.DASH)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RecipeParser.WS:
                self.state = 89
                self.match(RecipeParser.WS)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
            self.match(RecipeParser.TEXT)
            self.state = 96
            self.match(RecipeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StepsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def step(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RecipeParser.StepContext)
            else:
                return self.getTypedRuleContext(RecipeParser.StepContext,i)


        def getRuleIndex(self):
            return RecipeParser.RULE_steps

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSteps" ):
                listener.enterSteps(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSteps" ):
                listener.exitSteps(self)




    def steps(self):

        localctx = RecipeParser.StepsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_steps)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 98
                self.step()
                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==RecipeParser.DASH):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DASH(self):
            return self.getToken(RecipeParser.DASH, 0)

        def TEXT(self):
            return self.getToken(RecipeParser.TEXT, 0)

        def NEWLINE(self):
            return self.getToken(RecipeParser.NEWLINE, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(RecipeParser.WS)
            else:
                return self.getToken(RecipeParser.WS, i)

        def getRuleIndex(self):
            return RecipeParser.RULE_step

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStep" ):
                listener.enterStep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStep" ):
                listener.exitStep(self)




    def step(self):

        localctx = RecipeParser.StepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_step)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(RecipeParser.DASH)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RecipeParser.WS:
                self.state = 104
                self.match(RecipeParser.WS)
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
            self.match(RecipeParser.TEXT)
            self.state = 111
            self.match(RecipeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





