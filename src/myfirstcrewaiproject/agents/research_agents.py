from crewai import Agent
from textwrap import dedent
import google.generativeai as genai  # Ensure this import
import os
from myfirstcrewaiproject.tools.custom_tools import get_search_tool

# config.py should have already handled API key loading and configuration.
# No need to call os.getenv or genai.configure here.

class CustomAgents:
    def __init__(self):
        # The API key is configured globally in config.py
        # self.gemini_api_key = os.getenv("GEMINI_API_KEY") # Removed
        # if not self.gemini_api_key: # Removed
        #     raise EnvironmentError("ERROR: GEMINI_API_KEY not found in .env file") # Removed
        # genai.configure(api_key=self.gemini_api_key) # Removed
        self.llm_model = self.initialize_llm_model()
        self.search_tool = get_search_tool()

    def initialize_llm_model(self):
        # This method now standardly returns the Gemini model name.
        # Configuration for this model (API key) is handled globally via config.py and environment variables.
        return "gemini/gemini-pro" # Ensures this is the model name being used.

    def business_analyst_agent(self):
        """An agent specialized in analyzing business processes to identify automation opportunities."""
        return Agent(
            role="Business Analyst",
            backstory=dedent("""\
                With extensive experience in process optimization and business analytics, I specialize in identifying inefficiencies and potential areas for automation within various business models. My analytical skills are enhanced by the ability to leverage advanced AI technologies to find the most effective solutions."""),  
            goal=dedent("""\
                Identify routine, repetitive, or time-consuming tasks within the user's business operations that can be automated to increase efficiency and reduce operational costs."""),  
            verbose=True,
            llm=self.llm_model,
            tools=[self.search_tool]
        )

    def solutions_architect_agent(self):
        """An agent dedicated to designing CrewAI configurations that automate identified business processes."""
        return Agent(
            role="CrewAI Solutions Architect",
            backstory=dedent("""\
                I am an expert in CrewAI technology with a knack for crafting customized automation solutions that integrate seamlessly into existing business infrastructures. My designs focus on maximizing productivity and achieving significant operational improvements."""),  
            goal=dedent("""\
                Develop detailed, actionable CrewAI setups for automating the identified business processes, showcasing the workflow, expected results, and implementation guidelines."""),  
            verbose=True,
            llm=self.llm_model,
        )
