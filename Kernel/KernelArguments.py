from typing import Any

class KernelArguments:

    arguments: dict[str, Any]

    def __init__(self):
        self.arguments = {}

    def __call__(self, arguments: dict[str, str]):
        self.arguments = self.arguments | arguments

    def execute(self, prompt: str):
        template = prompt

        for key, value in self.arguments.items():
            placeholder = f"{{{{ ${key} }}}}"
            template = template.replace(placeholder, value)

        return template