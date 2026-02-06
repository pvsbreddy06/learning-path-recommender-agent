from flask import Flask, request, jsonify
from skill_assessor import assess_skills
from gap_analyzer import analyze_gap
from path_optimizer import generate_learning_path
from progress_tracker import track_progress

app = Flask(__name__)

@app.route("/assess", methods=["POST"])
def assess():
    data = request.json
    skills = assess_skills(data)
    gaps = analyze_gap(skills, data["target_role"])
    path = generate_learning_path(gaps, data["time_per_week"])
    return jsonify(path)

@app.route("/progress", methods=["POST"])
def progress():
    return jsonify(track_progress(request.json))

if __name__ == "__main__":
    app.run(debug=True)
