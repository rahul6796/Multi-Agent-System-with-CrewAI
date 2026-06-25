from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import PDFSearchTool
# from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

# # define the knowledge source.

# research_paper = PDFKnowledgeSource(
#     file_paths=['2301.00234v6.pdf'],
#     chunk_size=1500,
#     chunk_overlap=250
# )


@CrewBase
class KnowledgeCrew():
    """KnowledgeCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # define the path of the agent and task yaml.
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"


    # define the agents
    @agent
    def research_summarization(self) -> Agent:

        return Agent(
            config = self.agents_config['research_summarization'],
            verbose = True,
            tools = [PDFSearchTool(
                pdf='knowledge/icl_paper.pdf'
            )]
        ) 
    

    # define the task
    @task
    def summarization_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarization_task'],
            output_file='response/output.md'
        )
    
    # define the crew

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            # knowledge_sources=[research_paper],
        )
        


