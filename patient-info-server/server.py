from flask import Flask, request, jsonify
from patient import Patient  

app = Flask(__name__)

@app.route('/submit_form', methods=['POST'])
def handle_form():
    if request.is_json:
        data = request.json
        try:
            patient = Patient(**data)  
            
            return jsonify({"message": "Patient data received", "patient": data}), 200
        except TypeError as e:
            
            return jsonify({"error": str(e)}), 400
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)

