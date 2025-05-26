from Kernel.KernelArguments import KernelArguments
from Kernel.KernelFunctions import kernel_function
from Kernel.Kernel import Kernel
from Kernel.KernelModes import KernelModes
from Kernel.Models.Model_OpenAI import Model_OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Get the API key
api_key = os.getenv("OPENAI_API_KEY")
kernel = Kernel()
model = Model_OpenAI("chat_gpt", api_key, "gpt-4.1-nano")
kernel.set_ai_model(model)

@kernel_function(name="create_pizza", description="Create a simple pizza")
def create_pizza():
    print("Create a simple pizza")

@kernel_function(name="add_cheeze", description="add cheese to pizza")
def add_cheeze():
    print("add cheese to pizza")

@kernel_function(name="add_tomato_suace", description="add tomato sauce to pizza")
def add_tomato_suace():
    print("add tomato sauce to pizza")

@kernel_function(name="add_sausage", description="add sausage to pizza Note sausage is a meat")
def add_sausage():
    print("add sausage to pizza")

@kernel_function(name="add_vegtables", description="add vegtables to pizza")
def add_vegtables():
    print("add vegtables to pizza")

@kernel_function(name="deliver_pizza", description="deliver pizza to costumer")
def deliver_pizza():
    print("deliver pizza to costumer")

kernel.add_plugin(create_pizza)
kernel.add_plugin(add_cheeze)
kernel.add_plugin(add_sausage)
kernel.add_plugin(add_vegtables)
kernel.add_plugin(deliver_pizza)

output = kernel.invoke(prompt="make a pizza and deliver it", mode=KernelModes.AGENT, arguments=KernelArguments())
print(output)
