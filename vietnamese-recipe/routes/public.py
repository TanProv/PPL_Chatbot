from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from config import DATA_FOLDER, PENDING_FOLDER
from utils import create_filename
from data_manager import data_store
import os

public_bp = Blueprint('public', __name__)

@public_bp.route('/')
def index():
    return render_template('index.html', recipe_count=len(data_store.recipes))

@public_bp.route('/chat')
def chat_page():
    return render_template('chat.html', recipe_count=len(data_store.recipes))

@public_bp.route('/add-recipe', methods=['GET', 'POST'])
def add_recipe():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        name = request.form.get('name')
        
        # Tạo nội dung file .txt chuẩn Grammar
        content = f"Name: {name}\nRegion: {request.form.get('region')}\n"
        content += f"Category: {request.form.get('category')}\nTime: {request.form.get('time')} mins\n"
        content += f"Servings: {request.form.get('servings')}\nCalories: {request.form.get('calories')}\n"
        content += f"Difficulty: {request.form.get('difficulty')}\nTags: {request.form.get('tags')}\n\nIngredients:\n"
        
        for ing in request.form.getlist('ingredients[]'):
            if ing.strip(): content += f"- {ing.strip()}\n"
        
        content += "\nSteps:\n"
        for step in request.form.getlist('steps[]'):
            if step.strip(): content += f"- {step.strip()}\n"

        filename = create_filename(name)
        
        # Admin thêm -> Vào thẳng Data chính. User thêm -> Vào Pending
        if session['role'] == 'admin':
            save_path = os.path.join(DATA_FOLDER, filename)
            msg = "Admin đã thêm món mới thành công!"
            action_reload = True
        else:
            save_path = os.path.join(PENDING_FOLDER, filename)
            msg = "Đã gửi công thức! Vui lòng chờ Admin duyệt."
            action_reload = False

        try:
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            if action_reload:
                data_store.reload_data()
                
            flash(msg, 'success')
            return redirect(url_for('public.index'))
        except Exception as e:
            flash(f"Lỗi: {str(e)}", 'error')

    return render_template('add_recipe.html')