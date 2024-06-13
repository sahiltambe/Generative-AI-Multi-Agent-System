# Multi-Agent System for Software Development Lifecycle

This repository contains a multi-agent system designed to manage different aspects of the software development lifecycle. The system includes agents such as Scrum Master, Task Assignment Agent, Progress Tracking Agent, Code Reviewer, QA Tester, and Deployment Manager. These agents collaborate to ensure smooth planning, development, testing, and deployment of software projects.

## Project Structure

- `agents.py`: Contains the definitions of various agents involved in the software development lifecycle.
- `tasks.py`: Contains the tasks assigned to each agent.
- `crew.py`: Defines the crew configuration and the process to manage the agents and tasks.
- `tools.py`: Contains the tools used by the agents to perform their tasks.
- `main.py`: Main script to run the multi-agent system.

## Agents and Tasks

### Agents

1. **Scrum Master**
   - **Role:** Oversee project progress and facilitate sprint planning.
   - **Backstory:** Ensures adherence to agile principles, removes impediments, and enhances team collaboration.
   - **Tools:** Agile management tool (e.g., Jira)

2. **Task Assignment Agent**
   - **Role:** Distribute tasks among team members based on their expertise and workload.
   - **Backstory:** Balances the workload and assigns tasks to the most suitable team members.
   - **Tools:** Task management tool (e.g., Asana)

3. **Progress Tracking Agent**
   - **Role:** Monitor ongoing tasks and provide regular updates to the Scrum Master.
   - **Backstory:** Keeps track of task statuses and reports any delays or issues.
   - **Tools:** Progress tracking tool (e.g., Trello)

4. **Code Reviewer**
   - **Role:** Analyze code for potential issues and ensure adherence to coding standards.
   - **Backstory:** Scrutinizes the code to identify bugs, security vulnerabilities, and coding standard violations.
   - **Tools:** Code analysis tool (e.g., SonarQube)

5. **QA Tester**
   - **Role:** Conduct automated tests to verify the software's functionality and performance.
   - **Backstory:** Ensures that the software meets the specified requirements and functions correctly.
   - **Tools:** Automated testing tool (e.g., Selenium)

6. **Deployment Manager**
   - **Role:** Manage the deployment of the software to different environments, ensuring a smooth and error-free release.
   - **Backstory:** Handles the deployment process, making sure that the software is correctly installed and configured in the target environments.
   - **Tools:** Deployment tool (e.g., Jenkins)

### Tasks

- **Sprint Planning Task**: Creates a detailed sprint plan with assigned tasks and timelines.
- **Task Assignment Task**: Generates a task assignment list based on team members' expertise and workload.
- **Progress Tracking Task**: Tracks the progress of ongoing tasks and generates status reports.
- **Code Review Task**: Performs a thorough code analysis to identify issues and ensure coding standards are met.
- **QA Testing Task**: Executes automated tests to verify software functionality and performance.
- **Deployment Task**: Deploys the software to the target environments and ensures it is correctly installed and configured.

## Usage

1. **Setup Environment:**
   - Ensure you have Python installed.
   - Install required libraries using `pip install -r requirements.txt`.
   - Set up environment variables for API keys (e.g., `GOOGLE_API_KEY`, `SERPER_API_KEY`).

2. **Run the Application:**
   - Execute the main script using `python crew.py`.

## Contributions
We welcome contributions to enhance the functionality and features of this application. Feel free to fork the repository, make changes, and submit a pull request.


## Contact
For any questions or support, please contact [sahiltambe1996@gmail.com](mailto:sahiltambe1996@gmail.com).
