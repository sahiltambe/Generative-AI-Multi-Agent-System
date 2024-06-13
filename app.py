import streamlit as st
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

# Importing necessary modules and functions
from agents import create_agent, scrum_master, team_lead
from tasks import create_task, scrum_task, lead_task
from tools import tool
from crew import create_crew
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize Google Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Async function to kickoff the crew
async def kickoff_crew(crew, inputs):
    result = await crew.kickoff(inputs=inputs)
    return result

# Streamlit app
st.title("Generative AI Multi-Agent System for Software Company")

# User inputs for agents
st.header("Scrum Master")
role1 = "Scrum Master"
goal1 = 'Ensure the team adheres to agile practices and delivers high-quality software in {topic}'
backstory1 = (
    "As a Scrum Master, you are dedicated to facilitating the agile process, "
    "removing impediments, and ensuring the team's productivity. "
    "You foster a culture of continuous improvement and adaptability."
)

st.header("Team Lead")
role2 = "Team Lead"
goal2 = 'Lead the software development team to deliver innovative solutions in {topic}'
backstory2 = (
    "As a Team Lead, you guide your team through technical challenges, "
    "mentor team members, and ensure successful project delivery. "
    "You have a strong technical background and a strategic vision for the project."
)

st.header("Task 1")
description1 = (
    "Facilitate the sprint planning meeting for the {topic} project. "
    "Ensure the team has a clear understanding of the sprint goals and tasks. "
    "Address any impediments and foster collaboration among team members."
)
expected_output1 = 'A detailed sprint plan outlining tasks, timelines, and assigned responsibilities, along with a list of identified impediments and resolutions.'

st.header("Task 2")
description2 = (
    "Oversee the development process for the {topic} project. "
    "Resolve technical issues, provide guidance to the development team, and ensure code quality. "
    "Mentor team members and promote best practices in software development."
)
expected_output2 = 'A comprehensive report on the project progress, key technical challenges faced and resolved, and a review of the code quality and adherence to best practices.'

if st.button("Execute Tasks"):
    # Create agents
    agent1 = create_agent(role1, goal1, backstory1, [tool], llm, True)
    agent2 = create_agent(role2, goal2, backstory2, [tool], llm, False)
    
    # Create tasks
    task1 = create_task(description1, expected_output1, [tool], agent1)
    task2 = create_task(description2, expected_output2, [tool], agent2)
    
    # Form the crew
    crew = create_crew([agent1, agent2], [task1, task2])
    
    # Run the kickoff asynchronously
    result = asyncio.run(kickoff_crew(crew, {'topic': 'DevOps Integration'}))  # Example topic
    
    st.header("Task Results")
    st.write(result)
