# esc2025_agents_workshop
A few code examples used during the esc2025_agents_workshop

## Installation

Environment,

```sh
mkdir workshop
cd workshop
python -m venv .venv # or uv venv
source .venv/bin/activate
```

Project download,

```sh
git clone https://github.com/aittalam/esc2025_agents_workshop
cd esc2025_agents_workshop
pip install -r requirements.txt
```

## Exercises

The order in which we could see the various agents is below:

* **agent_silly.py**, an "agent" that uses no tools (basically just an LLM)
* **agent_readfile.py**, reads a text file in the current directory
* **agent_vebpage.py**, search a web page
* **agent_searxng.py**, with an agent who searches the web with [searxng](https://docs.searxng.org/)
* **agent_zim.py**, with an agent that uses the MCP protocol to search into a [ZIM file](https://library.kiwix.org/#lang=eng)
