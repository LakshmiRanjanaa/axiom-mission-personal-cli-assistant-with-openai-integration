# Personal CLI Assistant with OpenAI Integration

A command-line tool that accepts natural language commands and converts them into system actions using OpenAI's API.

## Features
- Natural language command interpretation
- File operations (create, read, list)
- System information retrieval
- Web search capabilities
- Interactive conversation mode

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Set your OpenAI API key: `export OPENAI_API_KEY=your_api_key_here`
3. Run: `python cli_assistant.py "create a file called hello.txt with hello world"`

## Usage Examples
bash
# File operations
python cli_assistant.py "create a file called test.txt with some content"
python cli_assistant.py "list all files in current directory"
python cli_assistant.py "read the contents of test.txt"

# System info
python cli_assistant.py "show me system information"

# Web search
python cli_assistant.py "search the web for Python tutorials"

# Interactive mode
python cli_assistant.py --interactive
