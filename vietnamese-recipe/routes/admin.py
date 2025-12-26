from flask import Blueprint, render_template, session, redirect, url_for, flash
from config import DATA_FOLDER, PENDING_FOLDER
from data_manager import data_store
from recipe_parser import load_recipes_from_folder
import os
import shutil

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
def dashboard():
    if session.get('role') != 'admin':
        return "Access Denied", 403
    
    # Load danh sách chờ duyệt thủ công để lấy filename
    pending_files = []
    if os.path.exists(PENDING_FOLDER):
        for filename in os.listdir(PENDING_FOLDER):
            if filename.endswith(".txt"):
                path = os.path.join(PENDING_FOLDER, filename)
                with open(path, 'r', encoding='utf-8') as f:
                    # Đọc tên món (Dòng đầu tiên thường là Name: ...)
                    first_line = f.readline()
                    name = first_line.replace("Name:", "").strip()
                pending_files.append({'filename': filename, 'name': name})

    return render_template('admin.html', pending_files=pending_files)

@admin_bp.route('/approve/<filename>')
def approve(filename):
    if session.get('role') != 'admin': return "Unauthorized", 403

    src = os.path.join(PENDING_FOLDER, filename)
    dst = os.path.join(DATA_FOLDER, filename)
    
    if os.path.exists(src):
        shutil.move(src, dst)
        data_store.reload_data() # Reload lại chatbot ngay lập tức
        flash(f"Đã duyệt: {filename}", 'success')
    else:
        flash("File không tồn tại", 'error')
        
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/reject/<filename>')
def reject(filename):
    if session.get('role') != 'admin': return "Unauthorized", 403
    
    src = os.path.join(PENDING_FOLDER, filename)
    if os.path.exists(src):
        os.remove(src)
        flash(f"Đã xóa: {filename}", 'info')
    
    return redirect(url_for('admin.dashboard'))