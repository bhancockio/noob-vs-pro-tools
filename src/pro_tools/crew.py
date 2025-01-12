import os
from typing import Any, Dict  # Import os module

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, before_kickoff, crew, task

from pro_tools.utils.trello_utils import TrelloUtils


@CrewBase
class ProTools:
    """ProTools crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @before_kickoff
    def prepare_inputs(self, inputs: Dict[str, Any]):
        trello_utils = TrelloUtils()

        trello_todo_list_id = os.getenv("TRELLO_TOOD_LIST_ID")
        if trello_todo_list_id is None:
            raise ValueError("Environment variable 'TRELLO_TOOD_LIST_ID' is not set.")

        cards = trello_utils.get_cards_in_list(trello_todo_list_id)

        inputs["trello_cards"] = cards
        return inputs

    # Define agents
    @agent
    def researcher(self) -> Agent:
        """
        Creates the 'researcher' agent.
        Responsible for researching AI topics and gathering actionable insights.
        """
        return Agent(config=self.agents_config["researcher"], verbose=True)

    @agent
    def writer(self) -> Agent:
        """
        Creates the 'writer' agent.
        Responsible for crafting actionable articles based on research findings.
        """
        return Agent(config=self.agents_config["writer"], verbose=True)

    @agent
    def trello_manager(self) -> Agent:
        """
        Creates the 'trello_manager' agent.
        Responsible for saving articles as Trello comments and moving cards.
        """
        return Agent(config=self.agents_config["trello_manager"], verbose=True)

    # Define tasks
    @task
    def research_task(self) -> Task:
        """
        Creates the 'research_task'.
        Responsible for gathering actionable insights on AI topics.
        """
        return Task(config=self.tasks_config["research_task"])

    @task
    def article_task(self) -> Task:
        """
        Creates the 'article_task'.
        Responsible for turning research findings into concise and actionable articles.
        """
        return Task(config=self.tasks_config["article_task"])

    @task
    def trello_update_task(self) -> Task:
        """
        Creates the 'trello_update_task'.
        Responsible for saving articles as comments on Trello cards and moving them to the next column.
        """
        return Task(config=self.tasks_config["trello_update_task"])

    @crew
    def crew(self) -> Crew:
        """Creates the ProTools crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
