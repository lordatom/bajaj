from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get('data', [])
        
        # Separate numbers and alphabets
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        
        # Find the highest lowercase alphabet
        lowercases = [char for char in alphabets if char.islower()]
        highest_lowercase = max(lowercases) if lowercases else None

        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",  # Replace with dynamic values if needed
            "email": "john@xyz.com",         # Replace with dynamic values if needed
            "roll_number": "ABCD123",        # Replace with dynamic values if needed
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
        }
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
 
