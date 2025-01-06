import os
import requests
import json
import networkx as nx
from agents.base_agent import BaseAgent
from agents.design import DesignAgent
from agents.devops import DevOpsAgent
from agents.engineering import EngineeringAgent
from agents.product_management import ProductManagementAgent
from agents.security import SecurityAgent
from agents.testing import TestingAgent
from agents.final_agent import FinalAgent

def write_to_file(prompt, filename='output.txt'):
    with open(filename, 'a') as f:
        f.write("=== Iteration Output ===\n")
        f.write("Message:\n")
        f.write(prompt.get('message', '') + "\n\n")
        f.write("Code:\n")
        f.write(prompt.get('code', '') + "\n\n")
        f.write("README:\n")
        f.write(prompt.get('readme', '') + "\n")
        f.write("="*50 + "\n\n")

def main():

    # Initialize agents
    agents = {
        'ProductManagement': ProductManagementAgent(),
        'Design': DesignAgent(),
        'Engineering': EngineeringAgent(),
        'Testing': TestingAgent(),
        'Security': SecurityAgent(),
        'DevOps': DevOpsAgent(),
        'Final': FinalAgent()
    }

    # Create a directed graph to model the flow of data between agents
    G = nx.DiGraph()

    # Add nodes
    G.add_nodes_from(agents.keys())

    # Define edges to represent the flow between agents
    G.add_edges_from([
        ('ProductManagement', 'Design'),
        ('Design', 'Engineering'),
        ('Engineering', 'Testing'),
        ('Testing', 'Security'),
        ('Security', 'DevOps'),
        ('DevOps', 'Final')
    ])

    # Read initial prompt from 'initial_prompt.txt'
    try:
        with open('initial_prompt.json', 'r') as f:
            initial_prompt_content = f.read()
        # Parse the initial prompt from JSON
        prompt = json.loads(initial_prompt_content)
    except Exception as e:
        print(f"Error reading 'initial_prompt.txt': {e}")
        return

    iteration = 0
    max_iterations = 1  # Safety to prevent infinite loops
    is_complete = False

    while iteration < max_iterations and not is_complete:
        iteration += 1
        print(f"--- Iteration {iteration} ---")

        # Process the prompt through the agents according to the graph
        for node in nx.topological_sort(G):
            if node != 'Final':
                agent = agents[node]
                try:
                    print(f"Processing with {node}Agent")
                    prompt = agent.process(prompt)
                    write_to_file(prompt)
                except Exception as e:
                    print(f"An error occurred in {node}Agent: {e}")
                    return  # Exit if there's an error
            else:
                # Check if the process is complete using the FinalAgent
                is_complete = agents['Final'].process(prompt)
                if is_complete:
                    print("Process is complete.")
                else:
                    print("Process is not yet complete. Continuing to next iteration.")

    # After the loop ends
    if not is_complete:
        print("Reached maximum iterations without completion.")
        print("Outputting the final progress as if the process is complete.")

    # Output the final progress
    with open('final_output.txt', 'w') as f:
        f.write("=== Final Output ===\n")
        f.write("Message:\n")
        f.write(prompt.get('message', '') + "\n\n")
        f.write("Code:\n")
        f.write(prompt.get('code', '') + "\n\n")
        f.write("README:\n")
        f.write(prompt.get('readme', '') + "\n")
        f.write("="*50 + "\n\n")

    print("Final progress has been saved to 'final_output.txt'.")

if __name__ == "__main__":
    main()