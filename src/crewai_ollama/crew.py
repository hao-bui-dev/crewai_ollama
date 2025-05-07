from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from pathlib import Path
from crewai_ollama.tools.excel_tool import ExcelParseTool
from crewai_ollama.agents_logic.extract_data_logic import extract_table_from_excel, save_transformed_table

@CrewBase
class CrewaiOllama():
    """Schema mapping crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def file_parsing_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['file_parsing_specialist'],  # type: ignore[index]
            tools=[ExcelParseTool()],
            verbose=True
        )

    @agent
    def schema_mapping_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['schema_mapping_specialist'],  # type: ignore[index]
            verbose=True
        )

    @task
    def extract_data(self) -> Task:
        return Task(
            config=self.tasks_config['extract_data'],  # type: ignore[index]
            callback=lambda _: extract_table_from_excel("data/sample_invoice.xlsx"),
            agent=self.file_parsing_specialist()
        )

    @task
    def map_schema(self) -> Task:
        return Task(
            config=self.tasks_config['map_schema'],  # type: ignore[index]
            agent=self.schema_mapping_specialist(),
            callback=lambda task_output: save_transformed_table(task_output.raw)
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
