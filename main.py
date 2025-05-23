from dotenv import load_dotenv
import os

from Kernel.Kernel import Kernel
from Kernel.KernelArguments import KernelArguments
from Kernel.Models.Model_OpenAI import Model_OpenAI

# Load environment variables from .env file
load_dotenv()

# Get the API key
api_key = os.getenv("OPENAI_API_KEY")
kernel = Kernel()
model = Model_OpenAI("chat_gpt", api_key, "gpt-4.1-nano")
kernel.set_ai_model(model)

args = KernelArguments()
args({"name": "tal" ,"age":"20", "height": "five feet nine inches"})

prompt="Write exactly one joke about the person i am providing, be creative and funny. \n\n PERSON: \n name={{ $name }}\n age={{ $age }}\n height={{ $height }}"

print(kernel.invoke_async(prompt=prompt, arguments=args))