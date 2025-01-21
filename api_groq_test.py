from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os
load_dotenv()
GROQ_API_KEY=os.getenv('GROQ_API_KEY')

web_agent = Agent(
    name="Web Agent",
    model=Groq(id = 'llama-3.3-70b-versatile',
               api_key=GROQ_API_KEY),
    tools=[DuckDuckGo(news=False, search = True)],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)



if __name__ == "__main__":
    web_agent.print_response("Help me with Best Manchester United Matches", stream=False)