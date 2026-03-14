#!/usr/bin/env python3
"""
Personal CLI Assistant with OpenAI Integration
Accepts natural language commands and converts them to system actions.
"""

import click
import json
import os
from openai import OpenAI
from actions import FileManager, SystemInfo, WebSearch


class CLIAssistant:
    def __init__(self):
        # Initialize OpenAI client
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("Please set OPENAI_API_KEY environment variable")
        
        self.client = OpenAI(api_key=api_key)
        
        # Initialize action handlers
        self.file_manager = FileManager()
        self.system_info = SystemInfo()
        self.web_search = WebSearch()
        
        # Define available actions for the AI
        self.available_actions = {
            "file_create": "Create a new file with content",
            "file_read": "Read contents of a file", 
            "file_list": "List files in directory",
            "system_info": "Get system information",
            "web_search": "Search the web for information"
        }
    
    def interpret_command(self, user_input):
        """
        Use OpenAI to interpret natural language and return structured action
        """
        system_prompt = f"""
        You are a CLI assistant. Convert user requests into JSON actions.
        Available actions: {json.dumps(self.available_actions, indent=2)}
        
        Return ONLY a JSON object with this structure:
        {{
            "action": "action_name",
            "parameters": {{
                "param1": "value1",
                "param2": "value2"
            }}
        }}
        
        Examples:
        User: "create a file called test.txt with hello world"
        Response: {{"action": "file_create", "parameters": {{"filename": "test.txt", "content": "hello world"}}}}
        
        User: "list files"
        Response: {{"action": "file_list", "parameters": {{"directory": "."}}}}
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.1
            )
            
            # Parse the JSON response
            action_json = response.choices[0].message.content.strip()
            return json.loads(action_json)
            
        except Exception as e:
            return {"error": f"Failed to interpret command: {str(e)}"}
    
    def execute_action(self, action_data):
        """
        Execute the interpreted action
        """
        if "error" in action_data:
            return action_data["error"]
        
        action = action_data.get("action")
        params = action_data.get("parameters", {})
        
        try:
            # Route to appropriate handler
            if action == "file_create":
                return self.file_manager.create_file(params.get("filename"), params.get("content", ""))
            elif action == "file_read":
                return self.file_manager.read_file(params.get("filename"))
            elif action == "file_list":
                return self.file_manager.list_files(params.get("directory", "."))
            elif action == "system_info":
                return self.system_info.get_info()
            elif action == "web_search":
                return self.web_search.search(params.get("query", ""))
            else:
                return f"Unknown action: {action}"
                
        except Exception as e:
            return f"Error executing action: {str(e)}"


@click.command()
@click.argument('command', required=False)
@click.option('--interactive', '-i', is_flag=True, help='Run in interactive mode')
def main(command, interactive):
    """
    Personal CLI Assistant - Convert natural language to system actions
    """
    try:
        assistant = CLIAssistant()
        
        if interactive:
            # Interactive mode
            click.echo("🤖 CLI Assistant started! Type 'quit' to exit.")
            while True:
                user_input = click.prompt("You")
                if user_input.lower() in ['quit', 'exit', 'q']:
                    click.echo("Goodbye!")
                    break
                
                # Process command
                action_data = assistant.interpret_command(user_input)
                result = assistant.execute_action(action_data)
                click.echo(f"🤖 Assistant: {result}")
        
        elif command:
            # Single command mode
            action_data = assistant.interpret_command(command)
            result = assistant.execute_action(action_data)
            click.echo(result)
        
        else:
            # Show help if no command provided
            ctx = click.get_current_context()
            click.echo(ctx.get_help())
            click.echo("\n💡 Example: python cli_assistant.py \"create a file called test.txt\"")
    
    except ValueError as e:
        click.echo(f"❌ Error: {e}", err=True)
    except Exception as e:
        click.echo(f"❌ Unexpected error: {e}", err=True)


if __name__ == '__main__':
    main()