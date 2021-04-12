""" 
    remove this file later
    by Akino
"""
import json
import sys

import requests

# Make sure this URL is correct
API_URL = "http://localhost:5000/api"


def get_text_input(message):
    """ Function to get a text value from the user.

    Loops until the text is not empty.

    Returns:
        str
    """
    choice = None
    while not choice:
        try:
            choice = input(message)
        except KeyboardInterrupt:
            # Quit the program if user presses Ctrl-C
            print("Ok, quitting now.")
            sys.exit(-1)

        if not choice:
            print("Invalid input.")

    return choice


def get_int_input(message):
    """ Function to get a text value from the user.

    Loops until the value is an integer.

    Returns:
        int
    """
    choice = None
    while not choice:
        try:
            choice = input(message)
        except KeyboardInterrupt:
            # Quit the program if user presses Ctrl-C
            print("Ok, quitting now.")
            sys.exit(-1)

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input.")
            continue

    return choice


def view_score(json_data):
    """ View to display one score in the console """
    for key, value in json_data.items():
        print(f"{key:.<10} {value}")


def view_all_scores(json_data):
    """ View to display a list of scores in the console """
    print("-" * 80)
    for score in json_data:
        view_score(score)
        print("-" * 80)


def display_response(req):
    """ Helper function to display the status code a request """
    print(f"Status code: {req.status_code}")
    input("Press any key and Enter to continue.")


def process_response(req):
    """ Function that processes the output of a request.

    If the status code is 200, and there is JSON available, returns the JSON.
    Otherwise return None
    """
    if req.status_code != 200:
        display_response(req)
        return None

    try:
        data = req.json()
    except json.decoder.JSONDecodeError:
        print("The API did not return JSON. Check your code!")
        data = None

    return data


# def delete_controller():
#     """ Controller to delete a score from the API """
#     _id = None
#     while not _id:
#         _id = get_int_input("Enter the score ID: ")

#     r = requests.delete(f"{API_URL}/score/{_id}")
#     process_response(r)

# def put_controller():
#     """ Controller to update a score from the API """
#     _id = None
#     score = None
#     name = None
#     while not (_id and score and name) :
#         _id = get_int_input("Enter the score ID: ")
#         name = get_text_input("Enter the player name: ")
#         score = get_int_input("Enter a score: ")
    
#     r = requests.post(f"{API_URL}/score/{_id}", json={"name": name, "score": score})
#     process_response(r)


def post_controller():
    """ Controller to post a score on the API """
    score = None
    name = None
    while not (score and name):
        name = get_text_input("Enter the player name: ")
        score = get_int_input("Enter a score: ")

    r = requests.post(f"{API_URL}/score", json={"name": name, "score": score})
    process_response(r)


def get_all_controller():
    """ Controller to get all scores from the API """
    r = requests.get(f"{API_URL}/scores")
    data = process_response(r)
    if data:
        view_all_scores(data)


def main():
    """ Main function for our CLI program """

    # List of actions and controllers
    ACTIONS = {
        "add": ("Add a new score to the API", post_controller),
        "list": ("View scores from the API", get_all_controller),
    }

    # Main loop
    running = True
    while running:
        # Displays the list of options available
        print()
        for key, value in ACTIONS.items():
            print(f"{key}: {value[0]}")

        choice = None
        while choice not in ACTIONS.keys():
            # Loop until a correct action is chosen
            choice = get_text_input("Please choose an action: ")

        # Get the function name for that action
        controller = ACTIONS[choice][1]

        if not controller:
            # If it is False, we want to exit the program
            running = False
        else:
            # Otherwise, run the function
            controller()


if __name__ == "__main__":
    main()
