"""
Action handlers for CLI Assistant
Each class handles a specific type of system operation.
"""

import os
import json
import psutil
import requests
from datetime import datetime


class FileManager:
    """Handle file operations"""
    
    def create_file(self, filename, content):
        """Create a new file with given content"""
        try:
            with open(filename, 'w') as f:
                f.write(content)
            return f"✅ Created file '{filename}' with content"
        except Exception as e:
            return f"❌ Error creating file: {str(e)}"
    
    def read_file(self, filename):
        """Read and return file contents"""
        try:
            with open(filename, 'r') as f:
                content = f.read()
            return f"📄 Contents of '{filename}':\n{content}"
        except FileNotFoundError:
            return f"❌ File '{filename}' not found"
        except Exception as e:
            return f"❌ Error reading file: {str(e)}"
    
    def list_files(self, directory="."):
        """List files in directory"""
        try:
            files = os.listdir(directory)
            if not files:
                return f"📁 Directory '{directory}' is empty"
            
            file_list = "\n".join([f"  - {f}" for f in sorted(files)])
            return f"📁 Files in '{directory}':\n{file_list}"
        except Exception as e:
            return f"❌ Error listing files: {str(e)}"


class SystemInfo:
    """Handle system information requests"""
    
    def get_info(self):
        """Get basic system information"""
        try:
            # Get system stats
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            info = f"""
💻 System Information:
  - CPU Usage: {cpu_percent}%
  - Memory: {memory.percent}% used ({self._bytes_to_gb(memory.used):.1f}GB / {self._bytes_to_gb(memory.total):.1f}GB)
  - Disk: {disk.percent}% used ({self._bytes_to_gb(disk.used):.1f}GB / {self._bytes_to_gb(disk.total):.1f}GB)
  - Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
  - Working Directory: {os.getcwd()}
            """.strip()
            
            return info
        except Exception as e:
            return f"❌ Error getting system info: {str(e)}"
    
    def _bytes_to_gb(self, bytes_val):
        """Convert bytes to gigabytes"""
        return bytes_val / (1024**3)


class WebSearch:
    """Handle web search operations (mock implementation)"""
    
    def search(self, query):
        """Perform a web search (simplified mock)"""
        if not query:
            return "❌ Please provide a search query"
        
        try:
            # Mock search results (in a real implementation, you'd use a search API)
            mock_results = [
                f"🔍 Search results for '{query}':",
                "  1. Example Result 1 - https://example1.com",
                "  2. Example Result 2 - https://example2.com", 
                "  3. Example Result 3 - https://example3.com",
                "",
                "💡 Note: This is a mock implementation. Integrate with a real search API for actual results."
            ]
            
            return "\n".join(mock_results)
        except Exception as e:
            return f"❌ Error performing search: {str(e)}"