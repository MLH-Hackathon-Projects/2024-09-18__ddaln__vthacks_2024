from flask import Flask, jsonify
from DatabaseManager import DatabaseManager

app = Flask(__name__)

# Initialize DatabaseManager
db_manager = DatabaseManager()

@app.route('/random-user', methods=['GET'])
def get_random_user():
    try:
        # Fetch a random user
        user = db_manager.fetch_random_user()
        if user:
            return jsonify(user)
        else:
            return jsonify({"message": "No user found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Other routes...
