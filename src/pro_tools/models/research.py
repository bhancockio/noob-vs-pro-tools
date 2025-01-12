from typing import List

from pydantic import BaseModel, Field


class Topic(BaseModel):
    id: int = Field(..., description="The unique identifier for the topic")
    name: str = Field(..., description="The name of the topic")
    research: str = Field(..., description="The research content related to the topic")


class Research(BaseModel):
    research_topics: List[Topic] = Field(..., description="A list of research topics")
