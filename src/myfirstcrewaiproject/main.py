from decouple import config
from crewai import Crew, Process
from textwrap import dedent

from myfirstcrewaiproject.agents.research_agents import CustomAgents
from myfirstcrewaiproject.tasks.research_tasks import CustomTasks
from google.generativeai import configure, generate_text  # Correct the import statement
from dotenv import load_dotenv
import os
import litellm  # Import liteLLM
from config import GEMINI_API_KEY

# Load environment variables
load_dotenv()

# Retrieve the API key from the environment
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise EnvironmentError("ERROR: GEMINI_API_KEY not found in .env file")

# Configure the Gemini API
configure(api_key=gemini_api_key)

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
        process_identification_task = self.tasks.process_identification_task(business_analyst, self.business_info)
        automation_design_task = self.tasks.automation_design_task(solutions_architect, "identified processes from task 1")

        # Form the crew with defined agents and tasks
        crew = Crew(
            agents=[business_analyst, solutions_architect],
            tasks=[process_identification_task, automation_design_task],
            verbose=True,
        )

        # Execute the crew to carry out the business automation project
        return crew.kickoff()

def main():
    # Configure LiteLLM with the API key
    os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY
    
    # Example business information
    business_info = """
    Our YouTube channel focuses on creating educational content for software developers.
    We spend a significant amount of time on filming and editing videos.
    We are looking for ways to automate these processes to improve efficiency.
    """
    
    if not GEMINI_API_KEY:
        raise ValueError("Gemini API key not found. Please set it in the .env file.")
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set the GOOGLE_API_KEY environment variable.")
    
    # Initialize and run the automation crew
    automation_crew = AutomationCrew(business_info)
    result = automation_crew.run()
    print(result)

if __name__ == "__main__":
    main()