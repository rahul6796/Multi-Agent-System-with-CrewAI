
from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class ReportSummarizationCrew():

    # define the agent datatype
    agents: list[BaseAgent]
    tasks: list[Task]

    # define the agent and task yaml file.
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # define the both the agents.

    @agent
    def report_generation(self)-> Agent:
       return Agent(
           config = self.agents_config['report_generation'],
           verbose = True
           
       )
    
    @agent
    def report_summarization(self)-> Agent:
        return Agent(
            config = self.agents_config['report_summarization'],
            verbose = True
        )

    # define the both tasks.
    # while defining the task order-should be maintain of task execution.

    @task
    def report_generation_task(self) -> Task:
        return Task(
            config = self.tasks_config['report_generation_task'],
            output_file = "reports/report.md"
        )

    @task
    def report_summarization_task(self)-> Task:
        return Task(
            config = self.tasks_config['report_summarization_task'],
            output_file = "reports/report_summary.md"
        )

    
    # define the crew
    @crew
    def crew(self)-> Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = True
        )

