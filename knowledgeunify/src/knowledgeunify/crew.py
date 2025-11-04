from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class Knowledgeunify():
    """Knowledgeunify crew"""

    agents: List[BaseAgent]
    tasks: List[Task]


    @agent
    def agente_suporte(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_suporte'],
            verbose=True
        )

    @agent
    def agente_rag(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_rag'],
            verbose=True
        )


    @task
    def tarefa_consutor(self) -> Task:
        return Task(
            config=self.tasks_config['tarefa_consutor'], 
            output_file='report.md',
            
        )

    @task
    def tarefa_rag(self) -> Task:
        return Task(
            config=self.tasks_config['tarefa_rag'], 

            
        )

    @crew
    def crew(self) -> Crew:


        return Crew(
            agents=self.agents,
            tasks=self.tasks, #
            process=Process.sequential,
            verbose=True,
        )
