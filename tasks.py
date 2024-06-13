from crewai import Task
from tools import tool
from agents import team_lead,scrum_master

# Example task creation for Scrum Master
scrum_task = Task(
    description=(
        "Facilitate the sprint planning meeting for the {topic} project. "
        "Ensure the team has a clear understanding of the sprint goals and tasks. "
        "Address any impediments and foster collaboration among team members."
    ),
    expected_output='A detailed sprint plan outlining tasks, timelines, and assigned responsibilities, along with a list of identified impediments and resolutions.',
    tools=[tool],
    agent=scrum_master
)

# Example task creation for Team Lead
lead_task = Task(
    description=(
        "Oversee the development process for the {topic} project. "
        "Resolve technical issues, provide guidance to the development team, and ensure code quality. "
        "Mentor team members and promote best practices in software development."
    ),
    expected_output='A comprehensive report on the project progress, key technical challenges faced and resolved, and a review of the code quality and adherence to best practices.',
    tools=[tool],
    async_execution=False,
    output_file='report.md'  # Example of output customi
)