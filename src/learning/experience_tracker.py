"""
Experience Tracking Module for AgentHope

Tracks and learns from agent interactions.
"""

import logging
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict

logger = logging.getLogger(__name__)

class ExperienceTracker:
    def __init__(self, storage_path: str = "memory/experiences.json"):
        self.storage_path = Path(storage_path)
        self.experiences: List[Dict] = []
        
        if not self.storage_path.parent.exists():
            self.storage_path.parent.mkdir(parents=True)
            
    def add_experience(self, action: str, result: str):
        """Record a new experience"""
        experience = {
            'timestamp': datetime.now().isoformat(),
            'action': action,
            'result': result
        }
        self.experiences.append(experience)
        self._save()
        
    def _save(self):
        """Save experiences to file"""
        with open(self.storage_path, 'w') as f:
            json.dump(self.experiences, f, indent=2)
            
    def load(self):
        """Load experiences from file"""
        if self.storage_path.exists():
            with open(self.storage_path, 'r') as f:
                self.experiences = json.load(f)
