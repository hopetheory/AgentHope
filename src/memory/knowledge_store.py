"""
Knowledge Storage Module for AgentHope

Manages persistent storage of agent knowledge.
"""

import logging
import json
from pathlib import Path
from typing import Dict, Any

logger = logging.getLogger(__name__)

class KnowledgeStore:
    def __init__(self, storage_path: str = "memory/knowledge.json"):
        self.storage_path = Path(storage_path)
        self.knowledge: Dict[str, Any] = {}
        
        if not self.storage_path.parent.exists():
            self.storage_path.parent.mkdir(parents=True)
            
    def save(self):
        """Save knowledge to file"""
        with open(self.storage_path, 'w') as f:
            json.dump(self.knowledge, f, indent=2)
            
    def load(self):
        """Load knowledge from file"""
        if self.storage_path.exists():
            with open(self.storage_path, 'r') as f:
                self.knowledge = json.load(f)
                
    def get(self, key: str, default=None) -> Any:
        """Get knowledge by key"""
        return self.knowledge.get(key, default)
        
    def set(self, key: str, value: Any):
        """Set knowledge key-value pair"""
        self.knowledge[key] = value
