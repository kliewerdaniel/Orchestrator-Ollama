from .config import ModelConfig

class BaseAgent:
    def __init__(self):
        self.endpoint = "http://localhost:11434/api/generate"
        self.model = ModelConfig.DEFAULT_MODEL