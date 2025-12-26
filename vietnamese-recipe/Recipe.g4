grammar Recipe;

// Root rule
recipes
    : (recipe (NEWLINE)*)* EOF
    ;

// ==================== PARSER RULES ====================

recipe
    : RECIPE_KEYWORD SEP recipeName NEWLINE
      REGION_KEYWORD  SEP region NEWLINE
      TIME_KEYWORD    SEP time NEWLINE
      SERVINGS_KEYWORD SEP servings NEWLINE
      CALORIES_KEYWORD SEP calories NEWLINE   // [MỚI]
      DIFFICULTY_KEYWORD SEP difficulty NEWLINE
      CATEGORY_KEYWORD SEP category NEWLINE
      TAGS_KEYWORD     SEP tags NEWLINE       // [MỚI]
      INGREDIENTS_KEYWORD SEP NEWLINE
      ingredients
      STEPS_KEYWORD SEP NEWLINE
      steps
    ;

recipeName : TEXT ;
region     : NORTHERN | CENTRAL | SOUTHERN ;
time       : NUMBER ;
servings   : NUMBER ;
calories   : NUMBER ;     // [MỚI]
difficulty : EASY | MEDIUM | HARD ;
category   : TEXT ;
tags       : TEXT ;       // [MỚI]

ingredients : ingredient+ ;
ingredient  : DASH WS* TEXT NEWLINE ;

steps : step+ ;
step  : DASH WS* TEXT NEWLINE ;

// ==================== LEXER RULES ====================

RECIPE_KEYWORD      : 'RECIPE' ;
REGION_KEYWORD      : 'REGION' ;
TIME_KEYWORD        : 'TIME' ;
SERVINGS_KEYWORD    : 'SERVINGS' ;
CALORIES_KEYWORD    : 'CALORIES' ; 
DIFFICULTY_KEYWORD  : 'DIFFICULTY' ;
CATEGORY_KEYWORD    : 'CATEGORY' ;
TAGS_KEYWORD        : 'TAGS' ;     
INGREDIENTS_KEYWORD : 'INGREDIENTS' ;
STEPS_KEYWORD       : 'STEPS' ;

NORTHERN : 'Northern' ;
CENTRAL  : 'Central' ;
SOUTHERN : 'Southern' ;

EASY   : 'Easy' ;
MEDIUM : 'Medium' ;
HARD   : 'Hard' ;

DASH    : '-' ;
SEP     : ':' [ \t\u00A0\uFEFF]* ;
NEWLINE : '\r'? '\n' | '\r' ;
NUMBER  : [0-9]+ ;
WS      : [ \t\u00A0\uFEFF]+ -> skip ;
TEXT    : ~[\r\n:-]+ ;