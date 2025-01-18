# ProTools Crew

Welcome to the ProTools Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/pro_tools/config/agents.yaml` to define your agents
- Modify `src/pro_tools/config/tasks.yaml` to define your tasks
- Modify `src/pro_tools/crew.py` to add your own logic, tools and specific args
- Modify `src/pro_tools/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the pro-tools Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Important Resources To Connect Your Crew to Trello
- https://www.merge.dev/blog/trello-api-key
- https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-lists-get
- https://docs.tavily.com/docs/python-sdk/tavily-search/getting-started
