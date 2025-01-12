import os
from typing import Type

import requests
from crewai.tools import BaseTool
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class TrelloGetCardsInListTool(BaseTool):
    name: str = "Trello List Cards Tool"
    description: str = "Fetches all cards from the 'To Do' list in Trello."
    args_schema: Type[BaseModel] = BaseModel

    def _run(self) -> str:
        list_id = os.getenv("TRELLO_TOOD_LIST_ID")
        api_key = os.getenv("TRELLO_API_KEY")
        api_token = os.getenv("TRELLO_API_TOKEN")

        if not list_id:
            return "Error: TRELLO_TOOD_LIST_ID environment variable not set."
        if not api_key:
            return "Error: TRELLO_API_KEY environment variable not set."
        if not api_token:
            return "Error: TRELLO_API_TOKEN environment variable not set."

        url = f"https://api.trello.com/1/lists/{list_id}/cards"
        query = {"key": api_key, "token": api_token}

        response = requests.get(url, params=query)

        if response.status_code == 200:
            data = response.json()
            trello_cards = [{"id": card["id"], "desc": card["desc"]} for card in data]
            return trello_cards
        else:
            return f"Error: {response.status_code} - {response.text}"


# Noobs test in the agent.
# Pros test in advance manually with code.
if __name__ == "__main__":
    # Test the TrelloGetCardsInListTool
    tool = TrelloGetCardsInListTool()

    # Run the tool and print the result
    result = tool._run()
    print("Test Result:", result)
