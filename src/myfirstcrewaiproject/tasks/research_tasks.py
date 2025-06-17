from crewai import Task
from textwrap import dedent
import google.generativeai as genai # This import might not be necessary if not used directly

class CustomTasks:
    def __init__(self):
        """Initialize the class. API configuration is handled globally."""
        # API key configuration is now handled by config.py
        # if api_key: # Removed
        #     genai.configure(api_key=api_key) # Removed
        pass

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

    def automation_design_task(self, agent, process_identification_task_context):
        """Design CrewAI configurations to automate the identified processes based on context."""
        description = dedent("""\
            Analyze the output of the process identification task, which is available in the context.
            Based on the identified processes, design CrewAI setups to automate them.
            Ensure that these setups are intuitive for users with no prior AI knowledge,
            focusing on simplifying content production and editing.""")
        return Task(
            description=description,
            agent=agent,
            expected_output=dedent("""\
                Detailed CrewAI automation plans, including user-friendly tools and technologies 
                for automating YouTube video production and post-production tasks."""),
            context=[process_identification_task_context]
        )
