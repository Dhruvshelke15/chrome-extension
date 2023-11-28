import os
import json
from flask import Flask, jsonify, request
from profile_age_calculator import ProfileAgeCalculator

app = Flask(__name__)

# Load profiles from JSON files
profiles = []
for i in range(1, 11):
    file_path = f"profile{i}.json"
    if os.path.exists(file_path):
        with open(file_path, 'r' , encoding='utf-8') as file:
            profile_data = json.load(file)
            profiles.append(profile_data)

@app.route('/profiles', methods=['GET'])
def get_profiles():
    return jsonify(profiles)

@app.route('/age', methods=['GET'])
def get_age():
    name = request.args.get('name')
    profile = next((p for p in profiles if p['name'] == name), None)

    if profile:
        age = ProfileAgeCalculator.calculate_age(profile)
        return str(age) if age is not None else "Age not available"
    else:
        return "Profile not found"

if __name__ == '__main__':
    app.run(debug=True)
