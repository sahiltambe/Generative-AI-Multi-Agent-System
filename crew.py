from crewai import Crew,Process
from tasks import lead_task, scrum_task
from agents import team_lead,scrum_master

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[scrum_master,team_lead],
    tasks=[scrum_task,lead_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'Agile Practices'})
print(result)
# result=crew.kickoff(inputs={'topic':'DevOps Integration'})
# print(result)
# result=crew.kickoff(inputs={'topic':'Microservices Architecture'})
# print(result)