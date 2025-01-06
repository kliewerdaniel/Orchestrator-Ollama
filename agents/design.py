import os
import requests
from .base_agent import BaseAgent

class DesignAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.endpoint = "http://localhost:11434/api/generate"

    def process(self, message, code="", readme=""):
        # Convert message to string if it's a dict
        message_str = message if isinstance(message, str) else str(message)
        
        data = {
            "model": self.model,
            "prompt": f"""System: You are an experienced UI/UX designer specializing in creating intuitive, 
            accessible, and aesthetically pleasing interfaces for web and mobile applications. 
            You are up-to-date with modern design trends, tools, and technologies, and you 
            prioritize user-centered design principles.

            User: Based on the detailed product requirements below, please create comprehensive 
            UI/UX design specifications. Your deliverables should include:
            - High-fidelity wireframes
            - User flow diagrams
            - Interactive prototypes (if applicable)
            - Style guides with color schemes, typography, and component libraries

            Requirements: {message_str}""",
            "stream": False
        }
        
        try:
            response = requests.post(self.endpoint, json=data).json()
            design_spec = response.get('response', '')
            enhanced_message = f"{message_str}\n\n{design_spec}"
            
            return {
                'message': enhanced_message,
                'code': code,
                'readme': readme
            }
        except Exception as e:
            print(f"Error in DesignAgent: {str(e)}")
            return {
                'message': message_str,
                'code': code,
                'readme': readme
            }
