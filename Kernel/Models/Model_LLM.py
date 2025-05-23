import asyncio

class Model_LLM:

    def __init__(self, model_name: str, api_key: str):
        self.model_name = model_name
        self.api_key = api_key


    def invoke(self, content: str,prompt: str) -> str:
        pass