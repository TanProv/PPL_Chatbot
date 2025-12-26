Based on the source code and project structure provided, here is the **English version** of the `README.md` for your project.

---

# 🍜 Vietnamese Recipe Chatbot

This project is a web-based Chatbot application designed to help users find and explore Vietnamese recipes. The system utilizes **ANTLR4** to define and parse recipe data from text files, combines with **Flask** for the backend, and uses **TheFuzz** for intelligent fuzzy search capabilities.

## ✨ Key Features

* **💬 Natural Conversation:** Search for dishes by name or ingredients (supports Vietnamese input with or without accents).
* **🔍 Smart Search:** Uses Fuzzy Matching algorithms to provide suggestions even when there are typos or abbreviations in the query.
* **🥗 Versatile Filters:**
* Quick recipes (under 30 minutes).
* Easy-to-cook recipes.
* Calorie filtering (e.g., "under 500 calories").


* **➕ Add New Recipes:** Interface to add new dishes with images directly into the database.
* **🎲 Random Suggestion:** Suggests a random dish when the user doesn't know what to cook.

## 🛠️ Tech Stack

* **Language:** Python 3
* **Web Framework:** Flask
* **Parser & Grammar:** ANTLR4 (for defining the structure of `.txt` data files).
* **Search Engine:** TheFuzz (string matching).
* **Frontend:** HTML/CSS/JavaScript (Templates).

## 📂 Project Structure

```text
.
├── app.py                  # Main entry point for the Flask server
├── Recipe.g4               # ANTLR Grammar definition for recipe data files
├── recipe_parser.py        # Logic for parsing data from .txt files
├── data/                   # Directory containing recipe text files
│   ├── pho_bo.txt
│   └── ...
├── images/                 # Directory containing food images
├── templates/              # Web templates
│   ├── index.html
│   └── chat.html
└── .antlr/                 # ANTLR generated files (Lexer, Parser, Tokens)

```

## 🚀 Installation and Usage

### 1. Prerequisites

Ensure you have Python 3.x installed.

### 2. Install Dependencies

Install the required libraries using pip:

```bash
pip install flask antlr4-python3-runtime thefuzz

```

### 3. Run the Application

From the project root directory, run:

```bash
python app.py

```

Once running, open your browser and go to: `http://localhost:5000`.

## 📝 Data Format

Recipe data is stored in the `data/` directory as `.txt` files, adhering to the grammar defined in `Recipe.g4`. Below is the template structure:

```text
RECIPE: Dish Name
IMAGE: image_filename.jpg
REGION: Northern/Central/Southern
TIME: [minutes]
SERVINGS: [number of people]
CALORIES: [number of calories]
DIFFICULTY: Easy/Medium/Hard
CATEGORY: [Category Name]
TAGS: [tag1, tag2, tag3]
INGREDIENTS:
- [Ingredient 1]
- [Ingredient 2]
STEPS:
- [Step 1]
- [Step 2]

```

**

*Note: Keywords must be uppercase as shown above.*

## 🔧 Development

If you modify the `Recipe.g4` grammar file, you need to regenerate the ANTLR Lexer and Parser files. You can use the following command (requires Java and ANTLR tool):

```bash
antlr4 -Dlanguage=Python3 Recipe.g4

```

*(If you are only running the application, you do not need this step as `RecipeLexer.py` and `RecipeParser.py` are already provided).*

## 🤝 Contribution

Contributions are welcome. Please create a Pull Request or open an Issue if you find any bugs.

## 📄 License

This project is developed for educational purposes (Principles of Programming Languages course).
