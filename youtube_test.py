from phi.agent import Agent
from phi.tools.youtube_tools import YouTubeTools
from phi.model.groq import Groq


from dotenv import load_dotenv
import os
load_dotenv()
GROQ_API_KEY=os.getenv('GROQ_API_KEY')
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')

youtube_agent = Agent(
    name="Youtube Agent",
    model=Groq(id='llama-3.3-70b-versatile', api_key=GROQ_API_KEY),
    tools=[YouTubeTools()],
    show_tool_calls=True,
    description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
)

if __name__ == "__main__":
    youtube_agent.print_response("Summarize this video https://www.youtube.com/watch?v=Iv9dewmcFbs&t", markdown=True)
