""" Web blueprint. Defines the route /, which shows an HTML page with the list of students """
from flask import Blueprint, render_template

from models import ScoreManager

web_bp = Blueprint("web", __name__)


@web_bp.route("/")
def index():
    manager = ScoreManager()
    return render_template("home.html", players=manager.get_all_scores())