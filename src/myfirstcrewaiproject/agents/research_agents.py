from crewai import Agent
from textwrap import dedent
import google.generativeai as genai  # Ensure this import
import os

class CustomAgents:
    def __init__(self):
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")  # Ensure this line
        if not self.gemini_api_key:
            raise EnvironmentError("ERROR: GEMINI_API_KEY not found in .env file")
        genai.configure(api_key=self.gemini_api_key)  # Configure the API key
        self.gpt_model = self.initialize_gpt_model()

    def initialize_gpt_model(self):
        # Initialize your GPT model here with the Gemini API
        return "gemini/gemini-2.0-flash"

    def business_analyst_agent(self):
        """An agent specialized in analyzing business processes to identify automation opportunities."""
        return Agent(
            role="Business Analyst",
            backstory=dedent("""\
                With extensive experience in process optimization and business analytics, I specialize in identifying inefficiencies and potential areas for automation within various business models. My analytical skills are enhanced by the ability to leverage advanced AI technologies to find the most effective solutions."""),  
            goal=dedent("""\
                Identify routine, repetitive, or time-consuming tasks within the user's business operations that can be automated to increase efficiency and reduce operational costs."""),  
            verbose=True,
            llm=self.gpt_model,  
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
            llm=self.gpt_model,  
        )
