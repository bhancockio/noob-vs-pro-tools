import os
from typing import Any, Dict, Optional, Type

import requests
from crewai.tools import BaseTool
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


class TrelloUpdateCardInput(BaseModel):
    """Input schema for TrelloUpdateCardTool."""

    card_id: str = Field(..., description="The ID of the Trello card to update.")
    name: Optional[str] = Field(None, description="The new name for the card.")
    desc: Optional[str] = Field(None, description="The new description for the card.")
    closed: Optional[bool] = Field(None, description="Whether the card is closed.")
    idMembers: Optional[str] = Field(
        None, description="Comma-separated list of member IDs to add to the card."
    )
    idAttachmentCover: Optional[str] = Field(
        None, description="The ID of the attachment to use as the cover."
    )
    idList: Optional[str] = Field(
        None, description="The ID of the list to move the card to."
    )
    idLabels: Optional[str] = Field(
        None, description="Comma-separated list of label IDs to add to the card."
    )
    idBoard: Optional[str] = Field(
        None, description="The ID of the board to move the card to."
    )
    pos: Optional[str] = Field(
        None, description="The position of the card in the list."
    )
    due: Optional[str] = Field(None, description="The due date for the card.")
    start: Optional[str] = Field(None, description="The start date for the card.")
    dueComplete: Optional[bool] = Field(
        None, description="Whether the due date is complete."
    )
    subscribed: Optional[bool] = Field(
        None, description="Whether the card is subscribed."
    )
    address: Optional[str] = Field(None, description="The address for the card.")
    locationName: Optional[str] = Field(
        None, description="The location name for the card."
    )
    coordinates: Optional[str] = Field(
        None, description="The coordinates for the card."
    )
    cover: Optional[Dict[str, Any]] = Field(
        None, description="The cover object for the card."
    )


class TrelloUpdateCardTool(BaseTool):
    name: str = "Trello Update Card Tool"
    description: str = (
        "Updates properties of a Trello card (name, description, list, etc.)"
    )
    args_schema: Type[BaseModel] = TrelloUpdateCardInput

    def _run(self, card_id: str, **kwargs) -> str:
        api_key = os.getenv("TRELLO_API_KEY")
        api_token = os.getenv("TRELLO_API_TOKEN")

        if not api_key:
            return "Error: TRELLO_API_KEY environment variable not set."
        if not api_token:
            return "Error: TRELLO_API_TOKEN environment variable not set."

        url = f"https://api.trello.com/1/cards/{card_id}"
        print("url", url)
        query = {key: value for key, value in kwargs.items() if value is not None}
        print("query", query)
        query.update({"key": api_key, "token": api_token})

        if "idList" in query:
            query["idList"] = os.getenv("TRELLO_DOING_LIST_ID")

        response = requests.put(url, params=query)

        if response.status_code == 200:
            return "Card updated successfully."
        else:
            return f"Error: {response.status_code} - {response.text}"


if __name__ == "__main__":
    # Test the TrelloUpdateCardTool
    tool = TrelloUpdateCardTool()

    test_card_id = "6782b7931f82881c5faa7d1b"
    test_properties = {
        "name": "New Card Name",
        "desc": "Updated description",
        "idList": os.getenv("TRELLO_DOING_LIST_ID"),
    }

    # Run the tool and print the result
    result = tool._run(card_id=test_card_id, **test_properties)
    print("Test Result:", result)
