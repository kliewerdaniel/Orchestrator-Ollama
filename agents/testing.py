import os
import requests
from .base_agent import BaseAgent

class TestingAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.endpoint = "http://localhost:11434/api/generate"

    def process(self, message, code="", readme=""):
        message_str = message if isinstance(message, str) else str(message)
        
        data = {
            "model": self.model,
            "prompt": f"""System: You are an experienced QA engineer specializing in testing.
            
            User: Create a comprehensive testing strategy including:
            - Test cases
            - Testing approaches
            - Automation recommendations
            - Quality metrics

            Input: {message_str}""",
            "stream": False
        }
        
        try:
            response = requests.post(self.endpoint, json=data).json()
            testing_spec = response.get('response', '')
            enhanced_message = f"{message_str}\n\n{testing_spec}"
            
            return {
                'message': enhanced_message,
                'code': code,
                'readme': readme
            }
        except Exception as e:
            print(f"Error in TestingAgent: {str(e)}")
            return {
                'message': message_str,
                'code': code,
                'readme': readme
            }

