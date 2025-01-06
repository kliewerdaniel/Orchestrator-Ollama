import os
import requests
from .base_agent import BaseAgent

class FinalAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.endpoint = "http://localhost:11434/api/generate"

    def process(self, prompt):
        message = prompt.get('message', '')
        code = prompt.get('code', '')
        readme = prompt.get('readme', '')
        
        message_str = message if isinstance(message, str) else str(message)
        
        data = {
            "model": self.model,
            "prompt": f"""System: You are a project manager verifying if a software project is ready for deployment. 
            Check if all aspects like product requirements, design specs, code, testing, 
            security, and deployment scripts are complete and coherent.

            User: Based on the following project details, determine if the project is complete and ready 
            for deployment. Provide a 'Yes' or 'No' answer with a brief explanation.

            Message: {message_str}
            
            Code: {code}
            
            README: {readme}""",
            "stream": False
        }
        
        try:
            response = requests.post(self.endpoint, json=data).json()
            result = response.get('response', '')
            enhanced_message = f"{message_str}\n\n{result}"
            
            return {
                'message': enhanced_message,
                'code': code,
                'readme': readme
            }
        except Exception as e:
            print(f"Error in FinalAgent: {str(e)}")
            return {
                'message': message_str,
                'code': code,
                'readme': readme
            }
