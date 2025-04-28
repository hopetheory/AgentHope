"""
Natural Language Understanding Module for AgentHope

Handles parsing and understanding user commands.
"""

import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class CommandParser:
    def __init__(self):
        self.commands = {
            'help': self._handle_help,
            'capture': self._handle_capture,
            'type': self._handle_type
        }
        
    def parse(self, text: str) -> Dict[str, Any]:
        """Parse natural language command into executable action"""
        text = text.lower().strip()
        
        for cmd, handler in self.commands.items():
            if text.startswith(cmd):
                return handler(text)
        
        return {'action': 'unknown', 'details': text}
    
    def _handle_help(self, text: str) -> Dict[str, Any]:
        return {'action': 'help'}
        
    def _handle_capture(self, text: str) -> Dict[str, Any]:
        return {'action': 'capture', 'area': 'full'}
        
    def _handle_type(self, text: str) -> Dict[str, Any]:
        words = text.split(' ')
        if len(words) > 1:
            return {'action': 'type', 'text': ' '.join(words[1:])}
        return {'action': 'type', 'text': ''}
