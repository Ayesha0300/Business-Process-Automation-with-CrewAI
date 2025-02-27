from crewai import Task
from textwrap import dedent
import google.generativeai as genai

class CustomTasks:
    def __init__(self, api_key=None):
        """Initialize the class and optionally configure the Gemini API."""
        if api_key:
            genai.configure(api_key=api_key)

    def process_identification_task(self, agent, business_info):
        """Identify business processes that can be automated."""
        return Task(
            description=dedent(f"""\
                Analyze the following business information to identify processes that can be automated:
                
                {business_info}
                
                Focus particularly on tasks related to content creation, such as filming and editing, which are time-consuming and potentially automatable."""),

            agent=agent,
            expected_output=dedent("""\
                A detailed report identifying potential automation opportunities within the YouTube content creation workflow, 
                including recommendations for using AI to streamline filming and editing processes.""")
        )

    def automation_design_task(self, agent, identified_processes):
        """Design CrewAI configurations to automate the identified processes."""
        return Task(
            description=dedent(f"""\
                Based on the identified processes below, design CrewAI setups to automate them:
                
                {identified_processes}
                
                Ensure that these setups are intuitive for users with no prior AI knowledge, 
                focusing on simplifying content production and editing."""),

            agent=agent,
            expected_output=dedent("""\
                Detailed CrewAI automation plans, including user-friendly tools and technologies 
                for automating YouTube video production and post-production tasks.""")
        )
