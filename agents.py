from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

# Example agent creation for Scrum Master
scrum_master = Agent(
    role="Scrum Master",
    goal='Ensure the team adheres to agile practices and delivers high-quality software in {topic}',
    backstory=(
        "As a Scrum Master, you are dedicated to facilitating the agile process, "
        "removing impediments, and ensuring the team's productivity. "
        "You foster a culture of continuous improvement and adaptability."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Example agent creation for Team Lead
team_lead = Agent(
    role="Team Lead",
    verbose=True,
    memory=True,
    
    goal='Lead the software development team to deliver innovative solutions in {topic}',
    backstory=(
        "As a Team Lead, you guide your team through technical challenges, "
        "mentor team members, and ensure successful project delivery. "
        "You have a strong technical background and a strategic vision for the project."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)
