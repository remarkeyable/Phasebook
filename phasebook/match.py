import time
from flask import Blueprint, jsonify

from .data.match_data import MATCHES

bp = Blueprint("match", __name__, url_prefix="/match")

@bp.route("<int:match_id>")
def match(match_id):
    if not (0 <= match_id < len(MATCHES)):
        return "Invalid match id", 404

    start = time.time()
    is_match_result = is_match(*MATCHES[match_id])
    end = time.time()

    return jsonify({"message": "Match found" if is_match_result else "No match", "elapsedTime": end - start}), 200


def is_match(fave_numbers_1, fave_numbers_2):
    return set(fave_numbers_1) & set(fave_numbers_2) == set(fave_numbers_2)
