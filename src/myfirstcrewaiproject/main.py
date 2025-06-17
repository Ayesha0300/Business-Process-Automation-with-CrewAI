from decouple import config
from crewai import Crew, Process
from textwrap import dedent

# Import necessary modules from the project
from myfirstcrewaiproject.agents.research_agents import CustomAgents
from myfirstcrewaiproject.tasks.research_tasks import CustomTasks

# Import configuration (this will also load .env and configure genai)
import config

# Standard library imports
import os

# Third-party imports
# import litellm  # Removed, as CrewAI handles LiteLLM integration
# from google.generativeai import configure, generate_text # This is now handled in config.py
# from dotenv import load_dotenv # This is now handled in config.py


# Ensure GOOGLE_API_KEY is set in the environment for components like LiteLLM.
# config.py would have already raised an error if GOOGLE_API_KEY is not found.
os.environ["GOOGLE_API_KEY"] = config.GOOGLE_API_KEY


class AutomationCrew:
    def __init__(self, business_info):
        self.business_info = business_info
        self.agents = CustomAgents()
        self.tasks = CustomTasks()

    def run(self):
        # Initialize agents
        business_analyst = self.agents.business_analyst_agent()
        solutions_architect = self.agents.solutions_architect_agent()

        # Initialize tasks with respective agents and the user-provided business information
        process_identification_task = self.tasks.process_identification_task(
            agent=business_analyst,
            business_info=self.business_info
        )
        # Pass the process_identification_task object itself as context to the automation_design_task
        automation_design_task = self.tasks.automation_design_task(
            agent=solutions_architect,
            process_identification_task_context=process_identification_task
        )

        # Form the crew with defined agents and tasks
        crew = Crew(
            agents=[business_analyst, solutions_architect],
            tasks=[process_identification_task, automation_design_task],
            verbose=True,
        )

        # Execute the crew to carry out the business automation project
        return crew.kickoff()

def main():
    # The import of config.py (done above) will ensure GOOGLE_API_KEY is loaded and configured,
    # or raise an EnvironmentError if not found. No need for a check here.
    
    # Example business information
    business_info = dedent("""\
    Our YouTube channel focuses on creating educational content for software developers.
    We spend a significant amount of time on filming and editing videos.
    We are looking for ways to automate these processes to improve efficiency.
    """)
    
    # Initialize and run the automation crew
    # The API key check is implicitly handled by the import of config.py
    automation_crew = AutomationCrew(business_info)
    result = automation_crew.run()
    print(result)

if __name__ == "__main__":
    main()