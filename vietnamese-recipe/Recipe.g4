grammar Recipe;

// Root rule for multiple recipes
recipes
    : (recipe (NEWLINE)*)* EOF
    ;

// ==================== PARSER RULES ====================

recipe
    : RECIPE_KEYWORD SEP recipeName NEWLINE
      REGION_KEYWORD  SEP region NEWLINE
      TIME_KEYWORD    SEP time NEWLINE
      SERVINGS_KEYWORD SEP servings NEWLINE
      DIFFICULTY_KEYWORD SEP difficulty NEWLINE
      CATEGORY_KEYWORD SEP category NEWLINE
      INGREDIENTS_KEYWORD SEP NEWLINE
      ingredients
      STEPS_KEYWORD SEP NEWLINE
      steps
    ;

recipeName : TEXT ;
region     : NORTHERN | CENTRAL | SOUTHERN ;
time       : NUMBER ;
servings   : NUMBER ;
difficulty : EASY | MEDIUM | HARD ;
category   : TEXT ;

ingredients : ingredient+ ;
ingredient  : DASH WS* TEXT NEWLINE ;

steps : step+ ;
step  : DASH WS* TEXT NEWLINE ;

// ==================== LEXER RULES ====================

RECIPE_KEYWORD      : 'RECIPE' ;
REGION_KEYWORD      : 'REGION' ;
TIME_KEYWORD        : 'TIME' ;
SERVINGS_KEYWORD    : 'SERVINGS' ;
DIFFICULTY_KEYWORD  : 'DIFFICULTY' ;
CATEGORY_KEYWORD    : 'CATEGORY' ;
INGREDIENTS_KEYWORD : 'INGREDIENTS' ;
STEPS_KEYWORD       : 'STEPS' ;

NORTHERN : 'Northern' ;
CENTRAL  : 'Central' ;
SOUTHERN : 'Southern' ;

EASY   : 'Easy' ;
MEDIUM : 'Medium' ;
HARD   : 'Hard' ;

/*
  SEP eats ':' plus any following horizontal space
  including NBSP (\u00A0) and BOM (\uFEFF)
*/
DASH    : '-' ;
SEP     : ':' [ \t\u00A0\uFEFF]* ;
NEWLINE : '\r'? '\n' | '\r' ;
NUMBER  : [0-9]+ ;
WS      : [ \t\u00A0\uFEFF]+ -> skip ;
TEXT : ~[\r\n:-]+ ;

