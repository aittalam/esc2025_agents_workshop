import os

from any_agent import AgentConfig, AnyAgent
from pathlib import Path

SERVER_URL=os.environ.get("ESC_SERVER_URL", "localhost")

def read_file(file_name: str) -> str:
    """Read the contents of the given `file_name`.

    Args:
        file_name: The path to the file you want to read.

    Returns:
        The contents of `file_name`.

    Raises:
        ValueError: For the following cases:
            - If the path to the file is not allowed.
    """
    file_path = Path(file_name)
    return file_path.read_text()


def scan_current_dir(pattern: str) -> list[str]:
    """Scans the current directory for files satisfying the provided pattern.
    
    Args:
        pattern: The pattern used to filter files in the current directory (e.g. "*.txt"
        for text files, "*.py" for python files, "*.*" for all files)

    Returns:
        A string representing the list of filenames that satisfy the provided pattern
    """
    current_dir = Path(".")
    files_list = [str(f) for f in current_dir.glob(pattern)]
    return str(files_list)


agent = AnyAgent.create(
    "smolagents",
    AgentConfig(
        model_id="ollama/qwen3:8b",
        api_base=f"http://{SERVER_URL}:11434",
        instructions="""You must use the available tools to find an answer.""",
        tools=[scan_current_dir, read_file],
    ),
)

agent_trace = agent.run(
    "When was Denny Vrandecic born? Check in the files."
)
