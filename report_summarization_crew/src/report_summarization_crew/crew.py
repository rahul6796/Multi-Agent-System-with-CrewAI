
from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import Any
from crewai import TaskOutput


@CrewBase
class ReportSummarizationCrew():

    # define the agent datatype
    agents: list[BaseAgent]
    tasks: list[Task]

    # define the agent and task yaml file.
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # define the both the agents.

    # define the guardrail for report summarization word count.

    def validate_word_count_of_summary(self, result: TaskOutput) -> tuple[bool, Any]:
        try:
            word_limit = 400
            result: str = result.raw.strip()

            word_count = len(result.split(" "))

            if word_count > word_limit:
                return (False, "Summary exceeds the word count of 300 words, reduce the length to 300 words")
            return (True, result)
        except Exception as e:
            return ( False, f"Unexpected error as {str(e)}")



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
            output_file = "reports/report_new.md"
        )

    @task
    def report_summarization_task(self)-> Task:
        return Task(
            config = self.tasks_config['report_summarization_task'],
            output_file = "reports/report_summary_new.md",
            guardrial= self.validate_word_count_of_summary,
            guardrail_max_retries = 3

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

