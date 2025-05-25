from SemanticKernel.Models.Model_LLM import Model_LLM
from openai import OpenAI


class Model_OpenAI(Model_LLM):

    def __init__(self, model_name: str, api_key: str, model_type: str):
        super().__init__(model_name, api_key)
        self.model_name = model_name
        self.model_type = model_type
        self.client = OpenAI(
            api_key=api_key,
        )

    def invoke(self, content: str ,prompt: str):
        response = self.client.responses.create(
            model=self.model_type,
            instructions=content,
            input=prompt,
        )
        return response.output_text