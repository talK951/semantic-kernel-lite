from typing import Optional, Dict, Any, List, Callable

from Kernel.KernelArguments import KernelArguments
from Kernel.Models.Model_LLM import Model_LLM
from Kernel.KernelModes import KernelModes


class Kernel:
    model: Optional[Model_LLM]
    plugins: Dict[str, Any]

    def __init__(self):
        self.model = None
        self.plugins = {}

    def set_ai_model(self, model: Model_LLM):
        self.model = model

    def invoke(self, prompt: str, arguments: KernelArguments, mode: KernelModes=KernelModes.CHAT) -> str:
        prompt = arguments.execute(prompt)
        print(f"\n\nPrompt={prompt}\n\n")
        if mode == KernelModes.CHAT:
            return self.model.invoke(content="", prompt=prompt)
        elif mode == KernelModes.AGENT:
            plan = self.make_plan(prompt)
            self.execute_plan(plan)


    def add_plugin(self, plugin: Any):
        self.plugins[plugin.kernel_name] = plugin

    def make_plan(self, prompt: str) -> List[Callable]:
        functions = "["
        for name, func in self.plugins.items():
            functions += f"{name}={func.kernel_description}"
        functions += "]"

        prompt = "Convert the following user prompt into a list of function names that represent each step required to fulfill the task. Use concise, lowercase, underscore-separated names (e.g., fetch_data, sort_list, generate_summary).\n" + "Return the result as a Python-style list of strings\n" + "Use the provided dictionary of function name to function descriptions to construct this list FOUND BELOW THE PROMPT\n" + "Example Prompt:\n" + "‘Summarize this article, then translate it to Spanish and send it via email.’\n" + " Output:\n" + " [‘summarize_article’, ‘translate_to_spanish’, ‘send_email’]\n" + f"Now convert this prompt: {prompt}\n" + f"Functions: {functions}"
        plan = self.model.invoke(content="", prompt=prompt)
        plan = self._parse_string_list(plan_str=plan)
        return [self.plugins[func_name] for func_name in plan]

    def _parse_string_list(self, plan_str: str) -> list[str]:
        # Remove the surrounding brackets
        temp = plan_str.strip()[1:-1]

        # Split by commas and strip extra quotes and spaces
        return [item.strip().strip('"').strip("'") for item in temp.split(",")]

    def execute_plan(self, plan: List[Callable]):
        for func in plan:
            func()