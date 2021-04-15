import datetime
from flask import Blueprint, jsonify, request
from models import Score, ScoreManager

bp_api = Blueprint("api", __name__)


@bp_api.route("/scores")
def show_list():
    """ returns the JSON list of scores """
    manager = ScoreManager()
    return jsonify([s.to_json() for s in manager.scores])


@bp_api.route("/score", methods=["POST"])
def create_score():
    """ creates a new score (from JSON data) """
    manager = ScoreManager()
    data = request.get_json()

    if "name" not in data or "score" not in data:
        return "Invalid data", 400
    
    manager.add_score(name=data["name"], score=data["score"])
    manager.save()
    return "", 204
