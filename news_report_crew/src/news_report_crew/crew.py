from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from pydantic import BaseModel, Field
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()


# define the tool.
web_serach_tool = SerperDevTool()


# define the pydantic class for output format.
class NewsReport(BaseModel):
    headline: str =  Field(description="Headline of the news")
    url : str = Field(description="URL of the news web page")
    news_summary: str = Field(description= "  Summary of the news")
    news_agency_name: str = Field(description=" Name of the news agency that published the news")

class NewsReport(BaseModel):
    news: List[NewsReport]



@CrewBase
class NewsReportCrew():
    """NewsReportCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # config path of agent and task.
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"



    # define the agnet
    @agent
    def news_reporter(self) -> Agent:

        return Agent(
            config = self.agents_config['news_reporter'],
            verbose = True,
            tools = [web_serach_tool]
        )

    # define the task

    @task
    def reporting_task(self)-> Task:

        return Task(
            config=self.tasks_config['reporting_task'],
            output_file="news.json",
            output_pydantic=NewsReport
        )
    

    # define the crew
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks =self.tasks,
            verbose=True,
            process=Process.sequential
        )


    

   