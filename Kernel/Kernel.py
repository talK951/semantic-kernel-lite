from typing import Optional

from Kernel.KernelArguments import KernelArguments
from Kernel.Models.Model_LLM import Model_LLM

class Kernel:
    model: Optional[Model_LLM]

    def __init__(self):
        self.model = None

    def set_ai_model(self, model: Model_LLM):
        self.model = model

    def invoke_async(self, prompt: str, arguments: KernelArguments) -> str:
        prompt = arguments.execute(prompt)
        return self.model.invoke(content="", prompt=prompt)
