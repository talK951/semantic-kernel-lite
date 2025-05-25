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

history = ""

user_input = input()


while (True):
    args.add_arguments({"chat_history": history, "user_input": user_input})
    prompt = "user_input={{ $user_input }} \n\n instructions=You are a chatbot assistant respond to the request.   \n\n  chat_history={{ $chat_history }}"

    answer = kernel.invoke(prompt=prompt, arguments=args)
    print("==============================")
    history += "\nuser request=" + user_input + "\nAssistants reponse=" + answer
    print(f"<<<<<<<<{history}>>>>>>>>>>>")
    print(answer)
    user_input = input()

