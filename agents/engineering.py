import os
import requests
from .base_agent import BaseAgent

class EngineeringAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.endpoint = "http://localhost:11434/api/generate"

    def process(self, message, code="", readme=""):
        message_str = message if isinstance(message, str) else str(message)
        
        data = {
            "model": self.model,
            "prompt": f"""System: You are an experienced software engineer specializing in architecture and implementation.
            
            User: Based on the requirements, provide technical implementation details including:
            - Architecture decisions
            - Technology stack recommendations
            - Implementation approach
            - Key technical considerations

            Requirements: {message_str}""",
            "stream": False
        }
        
        try:
            response = requests.post(self.endpoint, json=data).json()
            engineering_spec = response.get('response', '')
            enhanced_message = f"{message_str}\n\n{engineering_spec}"
            
            return {
                'message': enhanced_message,
                'code': code,
                'readme': readme
            }
        except Exception as e:
            print(f"Error in EngineeringAgent: {str(e)}")
            return {
                'message': message_str,
                'code': code,
                'readme': readme
            }
