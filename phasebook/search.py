from flask import Blueprint, request,jsonify,Flask
from .data.search_data import USERS
import json

bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    args = request.args.to_dict()
    results = search_users(args)
    
    # uncomment this for bonus challenge
    # sorted_results = sort_results_by_priority(results, args)
    # return sorted_results, 200
    
    return results, 200
    
    #uncomment this for jsondumps
    # return json.dumps(results), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    results = USERS


    if args:
        results = [
            user
            for user in results
            if not args
            or (
                "id" in args and user["id"] == args["id"]
                or "name" in args and args["name"].lower() in user["name"].lower()
                or "age" in args and int(args["age"]) - 1 <= user["age"] <= int(args["age"]) + 1
                or "occupation" in args and args["occupation"].lower() in user["occupation"].lower()
            )
        ]

    results = [dict(i) for i in {tuple(user.items()) for user in results}]

    match_counts = {
        user["id"]: sum(1 for key in args if key in user and str(user[key]).lower() == args[key].lower())
        for user in results
    }

    sorted_results = sorted(results, key=lambda user: int(user["id"]))
    return sorted_results


#Bonus Challenge
def sort_results_by_priority(results, args):
    if 'id' in args:
        id_value = args['id']
        id_item = next((item for item in results if item['id'] == id_value), None)
        results.remove(id_item)  # Remove the item to prevent duplication
        sorted_results = [id_item] + sorted(
            results,
            key=lambda item: args['name'].lower() in item['name'].lower() if 'name' in args else True,
            reverse=True 
        )
    else:
        sorted_results = sorted(
            results,
            key=lambda item: args['name'].lower() in item['name'].lower() if 'name' in args else True,
            reverse=True 
        )

    return sorted_results



