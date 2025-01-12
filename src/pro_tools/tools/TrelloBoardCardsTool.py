import os
from typing import Literal, Type

import requests
from crewai.tools import BaseTool
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


class TrelloBoardCardsInput(BaseModel):
    """Input schema for TrelloBoardCardsTool."""

    filters: Literal["all", "closed", "none", "open", "visible"] = Field(
        "all",
        description="Filters to apply to the card search. Valid values: 'all', 'closed', 'none', 'open', 'visible'.",
    )


class TrelloBoardCardsTool(BaseTool):
    name: str = "Trello Board Cards Tool"
    description: str = (
        "Fetches all cards from a specified Trello board with optional filters."
    )
    args_schema: Type[BaseModel] = TrelloBoardCardsInput

    def _run(self, filters: str = "all") -> str:
        board_id = os.getenv("TRELLO_BOARD_ID")
        api_key = os.getenv("TRELLO_API_KEY")
        api_token = os.getenv("TRELLO_API_TOKEN")

        if not board_id:
            return "Error: TRELLO_BOARD_ID environment variable not set."
        if not api_key:
            return "Error: TRELLO_API_KEY environment variable not set."
        if not api_token:
            return "Error: TRELLO_API_TOKEN environment variable not set."

        url = f"https://api.trello.com/1/boards/{board_id}/cards/{filters}"
        query = {"key": api_key, "token": api_token}

        response = requests.get(url, params=query)

        if response.status_code == 200:
            return response.json()  # Returns the list of cards as JSON
        else:
            return f"Error: {response.status_code} - {response.text}"


if __name__ == "__main__":
    # Test the TrelloBoardCardsTool
    tool = TrelloBoardCardsTool()

    # Example filter to test with; you can change this to any valid filter value
    test_filter = "open"

    # Run the tool and print the result
    result = tool._run(filters=test_filter)
    print("Test Result:", result)
