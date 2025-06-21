from typing import Dict, Any, Tuple
import os
from dotenv import load_dotenv
import logging
from langchain_openai import ChatOpenAI
from crewai import Agent, Task, Crew
import json

load_dotenv()

class DomainClassifier:
    def __init__(self):
        self.domains = [
            "Healthcare",
            "Financial Services",
            "Manufacturing",
            "Retail",
            "Education",
            "Logistics",
            "Energy",
            "Telecommunications",
            "Real Estate",
            "Hospitality",
            "Technology",
        ]
        self.role = "Domain Classification Specialist"
        self.goal = "Classify projects into the most relevant domain based on the project description"
        self.backstory = "You are an expert at analyzing projects and determining their best-fit industry domain."
        self.LLM = ChatOpenAI(model="gpt-4o-mini", temperature=0.1, openai_api_key=os.getenv("OPENAI_API_KEY"))
        self.verbose = True
        self.agent = Agent(
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            llm=self.LLM,
            verbose=self.verbose
        )
    def classify(self, project_data: dict) -> dict | None:
        """
        Analyze the project data (expects at least a 'description' key) and return the best-fit domain as a string.
        """
        name = project_data.get("name", "Untitled Project")
        description = project_data.get("description", "")
        tags = ", ".join(project_data.get("tags", [])) if isinstance(project_data.get("tags", []), list) else project_data.get("tags", "No tags provided")
        project_type = ", ".join(project_data.get("type", [])) if isinstance(project_data.get("type", []), list) else project_data.get("type", "No project type provided")
        technologies = ", ".join(project_data.get("technologies", [])) if isinstance(project_data.get("technologies", []), list) else project_data.get("technologies", "No technologies provided")
        stakeholders = ", ".join(project_data.get("stakeholders", [])) if isinstance(project_data.get("stakeholders", []), list) else project_data.get("stakeholders", "No stakeholders provided")
        objectives = ", ".join(project_data.get("objectives", [])) if isinstance(project_data.get("objectives", []), list) else project_data.get("objectives", "No objectives provided")
        location = ", ".join(project_data.get("location", [])) if isinstance(project_data.get("location", []), list) else project_data.get("location", "No location provided")
        regulatory_context = ", ".join(project_data.get("regulatory_context", [])) if isinstance(project_data.get("regulatory_context", []), list) else project_data.get("regulatory_context", "No regulatory context provided")

        prompt = f"""
Below is a list of industries followed by details about a project. Please tell me which industry this project would most fit into:

Industries: {self.domains}
Project Name: {name}
Project Description: {description}
Tags: {tags}
Project Type: {project_type}
Technologies Used: {technologies}
Stakeholders: {stakeholders}
Objectives: {objectives}
Location: {location}
Regulatory Context: {regulatory_context}

Please respond in the following JSON format:
{{
  "industry": "...",
  "confidence": ...,
  "reasoning": "..."
}}
"""
        
        task = Task(
            description=prompt,
            agent=self.agent,
            expected_output="A JSON object with keys: industry, confidence, reasoning"
            )
        crew = Crew(agents=[self.agent], tasks=[task])
        #result = crew.kickoff()
        #print("Crew result dir:", dir(result))
        #print("Crew result:", json.loads(result.raw), type(result.raw))

        try:
            result = crew.kickoff()
            output_dict = result.raw #json.loads(result.output)
            if isinstance(output_dict, str):
                output_dict = json.loads(output_dict)
                print(type(output_dict))
            return output_dict
        except Exception as e:
            logging.error(f"Error executing task: {e}")
            return None

