import os
from typing import Type

import requests
from crewai.tools import BaseTool
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


class TrelloAddCardCommentInput(BaseModel):
    """Input schema for TrelloAddCardCommentTool."""

    card_id: str = Field(..., description="The ID of the Trello card to comment on.")
    text: str = Field(..., description="The text of the comment to add to the card.")


class TrelloAddCardCommentTool(BaseTool):
    name: str = "Trello Add Card Comment Tool"
    description: str = "Adds a comment to a specified Trello card."
    args_schema: Type[BaseModel] = TrelloAddCardCommentInput

    def _run(self, card_id: str, text: str) -> str:
        api_key = os.getenv("TRELLO_API_KEY")
        api_token = os.getenv("TRELLO_API_TOKEN")

        if not api_key:
            return "Error: TRELLO_API_KEY environment variable not set."
        if not api_token:
            return "Error: TRELLO_API_TOKEN environment variable not set."

        url = f"https://api.trello.com/1/cards/{card_id}/actions/comments"
        headers = {"Accept": "application/json"}
        query = {"text": text, "key": api_key, "token": api_token}

        response = requests.post(url, headers=headers, params=query)

        if response.status_code == 200:
            return "Comment added successfully."
        else:
            return f"Error: {response.status_code} - {response.text}"


if __name__ == "__main__":
    # Test the TrelloAddCardCommentTool
    tool = TrelloAddCardCommentTool()

    # Example card ID and comment text to test with
    test_card_id = "6782b7931f82881c5faa7d1b"
    test_text = "This is a test comment."

    # Run the tool and print the result
    result = tool._run(card_id=test_card_id, text=test_text)
    print("Test Result:", result)
