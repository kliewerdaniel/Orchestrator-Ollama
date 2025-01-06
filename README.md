Tech Company Orchestrator - User Guide

Welcome to the Tech Company Orchestrator! This project is designed to simulate the workflow of a tech company by orchestrating various agents to collaboratively process prompts and generate comprehensive outputs such as code, design specifications, deployment scripts, and more. The program utilizes Ollama models and a directed graph (via NetworkX) to model the interactions between different departments (agents).

Table of Contents
	1.	Features
	2.	Requirements
	3.	Installation
	4.	Usage
	5.	Workflow
	6.	Customizing Agents
	7.	Troubleshooting
	8.	Future Improvements

Features
	•	Agent-based Workflow: Simulates different tech company departments (e.g., Product Management, Design, Engineering).
	•	Directed Graph Processing: Uses NetworkX to define the flow of data between agents.
	•	Ollama Integration: Employs locally hosted models for generating agent-specific outputs.
	•	Iterative Processing: Refines outputs across iterations until the workflow is complete.
	•	Progress Persistence: Logs intermediate and final outputs to files.
	•	Custom Prompt Support: Accepts a structured prompt from an external file (initial_prompt.txt).

Requirements
	•	Python: 3.8 or higher
	•	Dependencies:
	•	ollama
	•	networkx
	•	python-dotenv
	•	json
	•	Ollama Installed: Ensure that Ollama is installed and the required models are downloaded locally.

Installation
	1.	Clone the Repository:

git clone https://github.com/kliewerdaniel/tech-company-orchestrator.git
cd tech-company-orchestrator


	2.	Install Dependencies:
Use pip to install the required libraries:

pip install -r requirements.txt


	3.	Set Up .env File:
Create a .env file in the root directory and specify the model name you will use with Ollama:

OLLAMA_MODEL=your-model-name

Replace your-model-name with the name of the model installed in Ollama (e.g., llama-2, qwen).

Usage

Step 1: Prepare Your Initial Prompt

Create an initial_prompt.txt file in the root directory. The prompt should be a JSON-formatted dictionary containing:
	•	message: The initial idea or requirements.
	•	code: Leave this as an empty string ("") initially.
	•	readme: Leave this as an empty string ("") initially.

Example initial_prompt.txt:

{
    "message": "Develop a platform that connects freelancers with clients using AI for project matching.",
    "code": "",
    "readme": ""
}

Step 2: Run the Program

Execute the main.py file:

python main.py

Step 3: Review the Outputs

The program generates the following files:
	•	output.txt: Contains the intermediate outputs after each iteration.
	•	final_output.txt: Contains the final output, including the message, code, and readme.

Workflow

The program simulates the workflow of a tech company by processing the prompt through the following agents:
	1.	Product Management: Expands the initial idea into detailed product requirements.
	2.	Design: Creates UI/UX specifications, including wireframes and style guides.
	3.	Engineering: Develops the software application based on the specifications.
	4.	Testing: Generates comprehensive test cases for quality assurance.
	5.	Security: Analyzes and enhances the security of the application.
	6.	DevOps: Creates deployment scripts and CI/CD pipelines.
	7.	Final Agent: Verifies if the project is complete or requires further refinement.

The agents are connected in a directed graph, ensuring an organized flow of information between departments.

Customizing Agents

Modify Agent Behavior

Each agent has its own Python file (e.g., engineering.py, design.py) where you can adjust:
	•	The prompts sent to the Ollama model.
	•	How the agent processes the data (e.g., appending to code or readme).

Add a New Agent
	1.	Create a new Python file for the agent.
	2.	Define the agent’s logic (similar to existing agents).
	3.	Add the new agent to the workflow graph in main.py:

G.add_edges_from([
    ('PreviousAgent', 'NewAgent'),
    ('NewAgent', 'NextAgent')
])

Troubleshooting

Ollama Not Installed or Configured

Ensure Ollama is installed and running on your system. Verify the model name in the .env file matches the locally available model.

Invalid initial_prompt.txt Format

Validate the JSON structure using an online tool like jsonlint.com.

Empty or Incorrect Outputs
	•	Check the logs in output.txt for intermediate results.
	•	Ensure the Ollama model is accessible and configured correctly.

Future Improvements
	•	Parallel Processing: Optimize the workflow to allow parallel execution of agents where applicable.
	•	Enhanced Error Handling: Improve robustness by adding retries and better error reporting.
	•	Interactive CLI: Provide a command-line interface for easier customization of inputs and parameters.
	•	Integration Testing: Add tests to validate the functionality of each agent and the overall workflow.

Contributions

Feel free to fork the repository and submit pull requests for improvements. Feedback and suggestions are always welcome!

With this guide, you should be able to set up, run, and customize the Tech Company Orchestrator with Ollama. Happy orchestrating! 🎉