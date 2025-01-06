import requests
import os
from .base_agent import BaseAgent

class ProductManagementAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.endpoint = "http://localhost:11434/api/generate"

    def process(self, message, code="", readme=""):
        # Convert message to string if it's a dict
        message_str = message if isinstance(message, str) else str(message)
        
        data = {
            "model": self.model,
            "prompt": f"""System: You are an experienced product manager specializing in software development. 
            You excel at creating detailed product requirements, user stories, and defining 
            success metrics that align with business goals.

            User: Please expand on the following idea by developing comprehensive product requirements. 
            Include user personas, user stories with acceptance criteria, feature prioritization, 
            and success metrics. Ensure the requirements are clear, actionable, and align with 
            modern software development practices.

            Idea: {message_str}""",
            "stream": False
        }
        
        try:
            response = requests.post(self.endpoint, json=data).json()
            product_requirements = response.get('response', '')
            enhanced_message = f"{message_str}\n\n{product_requirements}"
            
            return {
                'message': enhanced_message,
                'code': code,
                'readme': readme
            }
        except Exception as e:
            print(f"Error in ProductManagementAgent: {str(e)}")
            return {
                'message': message_str,
                'code': code,
                'readme': readme
            }
