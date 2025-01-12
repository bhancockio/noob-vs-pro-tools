import os

import requests
from dotenv import load_dotenv

# Adjust the path to your .env file
env_path = os.path.join(os.path.dirname(__file__), "../../../.env")
load_dotenv(dotenv_path=env_path)


class TrelloUtils:

    def __init__(self):
        self.api_key = os.getenv("TRELLO_API_KEY")
        self.token = os.getenv("TRELLO_API_TOKEN")

        if not self.api_key or not self.token:
            raise ValueError("TRELLO_API_KEY and TRELLO_API_TOKEN must be set.")

    def get_full_board_id(self, short_board_id):
        """
        Fetches the full board ID for the given short board ID from Trello API.

        Args:
            short_board_id (str): The short ID of the Trello board.

        Returns:
            str: The full board ID or an error message if the request fails.
        """
        url = f"https://api.trello.com/1/boards/{short_board_id}"
        query = {"key": self.api_key, "token": self.token}

        try:
            response = requests.get(url, params=query)
            if response.status_code == 200:
                board_data = response.json()
                return board_data.get(
                    "id", "Error: Full board ID not found in response."
                )
            else:
                return f"Error: {response.status_code} - {response.text}"
        except requests.RequestException as e:
            return f"Error: Unable to connect to Trello API. {e}"

    def get_board_lists(self, board_id):
        """
        Fetches all lists for the given board ID from Trello API.

        Args:
            board_id (str): The ID of the Trello board.

        Returns:
            list: A list of dictionaries containing list details or an error message if the request fails.
        """
        url = f"https://api.trello.com/1/boards/{board_id}/lists"
        query = {"key": self.api_key, "token": self.token}

        try:
            response = requests.get(url, params=query)
            if response.status_code == 200:
                return response.json()
            else:
                return f"Error: {response.status_code} - {response.text}"
        except requests.RequestException as e:
            return f"Error: Unable to connect to Trello API. {e}"

    def get_cards_in_list(self, list_id):
        """
        Fetches all cards from the specified list ID in Trello.

        Args:
            list_id (str): The ID of the Trello list.

        Returns:
            list: A list of dictionaries containing card details or an error message if the request fails.
        """
        if not list_id:
            return "Error: List ID must be provided."

        url = f"https://api.trello.com/1/lists/{list_id}/cards"
        query = {"key": self.api_key, "token": self.token}

        try:
            response = requests.get(url, params=query)
            if response.status_code == 200:
                data = response.json()
                print("Data: ", data)
                return [{"id": card["id"], "name": card["name"]} for card in data]
            else:
                return f"Error: {response.status_code} - {response.text}"
        except requests.RequestException as e:
            return f"Error: Unable to connect to Trello API. {e}"


if __name__ == "__main__":
    # Replace with your Trello short board ID

    # trello_utils = TrelloUtils()
    # short_board_id = "rCXL4ZCJ"
    # result = trello_utils.get_full_board_id(short_board_id)
    # print("Result:", result)

    # trello_utils = TrelloUtils()
    # board_id = os.getenv("TRELLO_BOARD_ID")
    # lists = trello_utils.get_board_lists(board_id)
    # print("Lists:", lists)

    trello_utils = TrelloUtils()
    list_id = os.getenv("TRELLO_TOOD_LIST_ID")
    cards = trello_utils.get_cards_in_list(list_id)
    print("Cards:", cards)
