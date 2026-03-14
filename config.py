"""
Configuration settings for CLI Assistant
"""

import os

# OpenAI Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_MODEL = 'gpt-3.5-turbo'
OPENAI_TEMPERATURE = 0.1

# CLI Configuration
CLI_NAME = 'CLI Assistant'
CLI_VERSION = '1.0.0'

# File operation settings
MAX_FILE_SIZE = 1024 * 1024  # 1MB limit for file operations
ALLOWED_EXTENSIONS = ['.txt', '.json', '.md', '.py', '.js', '.html', '.css']

# Default directories
DEFAULT_WORK_DIR = os.getcwd()
LOG_DIR = os.path.join(DEFAULT_WORK_DIR, 'logs')

# Error messages
ERROR_MESSAGES = {
    'no_api_key': 'OpenAI API key not found. Please set OPENAI_API_KEY environment variable.',
    'file_too_large': f'File size exceeds maximum limit of {MAX_FILE_SIZE} bytes.',
    'invalid_extension': f'File extension not allowed. Supported: {", ".join(ALLOWED_EXTENSIONS)}',
    'network_error': 'Network error occurred. Please check your internet connection.'
}

# Success messages
SUCCESS_MESSAGES = {
    'file_created': '✅ File created successfully',
    'file_read': '✅ File read successfully', 
    'command_executed': '✅ Command executed successfully'
}