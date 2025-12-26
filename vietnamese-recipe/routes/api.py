from flask import Blueprint, request, jsonify
from data_manager import data_store

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_msg = data.get('message', '')
    # Gọi chatbot engine thông qua data_store
    response = data_store.chatbot.generate_response(user_msg)
    return jsonify(response)

@api_bp.route('/api/recipes', methods=['GET'])
def get_recipes():
    return jsonify(data_store.recipes)