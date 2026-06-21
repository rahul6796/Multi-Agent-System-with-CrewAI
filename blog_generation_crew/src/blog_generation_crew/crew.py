from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool


web_serach_tool = SerperDevTool()


@CrewBase
class BlogGenerationCrew():

    agents: list[BaseAgent]
    tasks: list[Task]



    # define the config path of agent and task.
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"


    # define the team leader/project manager.
    @agent
    def team_leader(self)-> Agent:
        return Agent(
            config = self.agents_config['team_leader'],
            verbose = True,
            allow_deligation = True

        )
    
    # define the team members.
    @agent
    def research_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['research_agent'],
            verbose = True,
            allow_deligation = False
        )
    
    @agent
    def blog_writting_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['blog_writting_agent'],
            verbose = True,
            allow_deligation = False
            
            
        )
    
    @agent
    def blog_review_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['blog_review_agent'],
            verbose = True,
            allow_deligation = False

        )
    


    # define the Task.

    @task
    def blog_writing_task(self) -> Task:
        return Task(
            config= self.tasks_config['blog_writing_task'],
            output_file='blogs/blog.md'
        )
    

    # define the crew.
    @crew
    def crew(self)-> Crew:

        return Crew(

            agents=[self.research_agent(),
                    self.blog_writting_agent(),
                    self.blog_review_agent()],
            tasks=[self.blog_writing_task()],
            process=Process.hierarchical,
            verbose = True,
            manager_agent=self.team_leader()
        )
    

    

