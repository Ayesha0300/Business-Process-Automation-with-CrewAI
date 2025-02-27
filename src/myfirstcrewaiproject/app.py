import streamlit as st
from myfirstcrewaiproject.main import AutomationCrew 

def main():
    st.title("Business Process Automation with CrewAI")
    
    st.header("Business Information")
    business_info = st.text_area("Enter your business information here:", height=200)
    
    if st.button("Run Automation"):
        if business_info:
            automation_crew = AutomationCrew(business_info)
            result = automation_crew.run()
            st.success("Automation completed successfully!")
            st.write(result)
        else:
            st.error("Please enter the business information.")

if __name__ == "__main__":
    main()
