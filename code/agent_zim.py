import os

from any_agent import AgentConfig, AnyAgent
from any_agent.config import MCPStdio

SERVER_URL=os.environ.get("ESC_SERVER_URL", "localhost")

agent = AnyAgent.create(
    "smolagents",
    AgentConfig(
        model_id="ollama/qwen3:8b",
        api_base=f"http://{SERVER_URL}:11434",
        instructions="""You must use the available tools to find an answer.""",
        tools=[
            MCPStdio(
                command="uvx",
                args=[
                    "zim-mcp-server",
                    "/Users/mala/Downloads/zim"
                ],
            )
        ],
    ),
)

agent_trace = agent.run(
    "When was Denny Vrandecic born?"
)
