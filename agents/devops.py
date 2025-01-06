import os
import requests
from .base_agent import BaseAgent

class DevOpsAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.endpoint = "http://localhost:11434/api/generate"

    def process(self, message, code="", readme=""):
        message_str = message if isinstance(message, str) else str(message)
        
        data = {
            "model": self.model,
            "prompt": f"""System: You are an experienced DevOps engineer specializing in deployment and operations.
            
            User: Provide comprehensive DevOps recommendations including:
            - CI/CD pipeline design
            - Infrastructure setup
            - Monitoring solutions
            - Deployment strategies

            Input: {message_str}""",
            "stream": False
        }
        
        try:
            response = requests.post(self.endpoint, json=data).json()
            devops_spec = response.get('response', '')
            enhanced_message = f"{message_str}\n\n{devops_spec}"
            
            return {
                'message': enhanced_message,
                'code': code,
                'readme': readme
            }
        except Exception as e:
            print(f"Error in DevOpsAgent: {str(e)}")
            return {
                'message': message_str,
                'code': code,
                'readme': readme
            }