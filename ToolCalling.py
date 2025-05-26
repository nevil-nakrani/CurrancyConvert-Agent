from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.tools import tool, InjectedToolArg
from typing import Annotated
from langchain_core.messages import HumanMessage
# import speech_recognition as sr
import pyttsx3
import requests

load_dotenv()

@tool
def conversation_factor(base_currency: str, target_currency:str) -> float :
    """
    This function fetches the currency conversion factor between a given base currency and a target currency
    """
    url = f'https://v6.exchangerate-api.com/v6/478204704825054cdb243da1/pair/{base_currency}/{target_currency}'
    response = requests.get(url)
    print(response.json())
    return response.json()

@tool
def convert(base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
  """
  given a currency conversion rate this function calculates the target currency value from a given base currency value
  """
  return base_currency_value * conversion_rate

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

llm_with_tools = llm.bind_tools([conversation_factor, convert])

messages = [HumanMessage(content="How much is 100 USD in INR?")]
ai_message = llm_with_tools.invoke(messages)
print(ai_message)
messages.append(ai_message)

import json

for tool_call in ai_message.tool_calls:
  # execute the 1st tool and get the value of conversion rate
  if tool_call['name'] == 'conversation_factor':
    tool_message1 = conversation_factor.invoke(tool_call)
    # fetch this conversion rate
    conversion_rate = json.loads(tool_message1.content)['conversion_rate']
    # append this tool message to messages list
    messages.append(tool_message1)
  # execute the 2nd tool using the conversion rate from tool 1
  if tool_call['name'] == 'convert':
    # fetch the current arg
    tool_call['args']['conversion_rate'] = conversion_rate
    tool_message2 = convert.invoke(tool_call)
    messages.append(tool_message2)
    
    
result = llm_with_tools.invoke(messages).content
print(result)

engine = pyttsx3.init()
engine.say(result)
engine.runAndWait()