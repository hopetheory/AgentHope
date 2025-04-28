"""
Input Controller Module for AgentHope

This module handles keyboard and mouse control.
"""

import logging
import time
from typing import Tuple, Optional, List

logger = logging.getLogger(__name__)

class InputController:
    """
    Handles keyboard and mouse input control with safety mechanisms.
    """
    
    def __init__(self, config=None):
        """
        Initialize the input controller.
        
        Args:
            config: Configuration dictionary for input control
        """
        self.config = config or {}
        
        # Safety parameters
        self.safety_delay = self.config.get('safety_delay', 0.1)
        self.max_actions_per_minute = self.config.get('max_actions_per_minute', 300)
        
        # Action tracking for rate limiting
        self.action_timestamps = []
        
        logger.info("Input controller initialized")
    
    def _enforce_rate_limit(self):
        """
        Enforce rate limiting to prevent too many actions too quickly.
        """
        current_time = time.time()
        
        # Remove timestamps older than 60 seconds
        self.action_timestamps = [t for t in self.action_timestamps 
                                 if current_time - t <= 60]
        
        # Check if we're over the limit
        if len(self.action_timestamps) >= self.max_actions_per_minute:
            oldest_allowed = current_time - 60
            sleep_time = oldest_allowed - self.action_timestamps[0]
            if sleep_time > 0:
                logger.warning(f"Rate limit reached. Pausing for {sleep_time:.2f} seconds")
                time.sleep(sleep_time)
        
        # Add current action
        self.action_timestamps.append(current_time)
    
    def move_mouse(self, x, y, duration=0.5):
        """
        Move the mouse to the specified coordinates.
        
        Args:
            x: X coordinate
            y: Y coordinate
            duration: Time (in seconds) the movement should take
        """
        self._enforce_rate_limit()
        
        # TODO: Implement actual mouse movement
        # For now, just log the action
        logger.info(f"Moving mouse to ({x}, {y}) over {duration} seconds")
        
        time.sleep(self.safety_delay)
    
    def click(self, x=None, y=None, button='left', clicks=1):
        """
        Click at the current or specified position.
        
        Args:
            x: Optional X coordinate. If None, uses current position.
            y: Optional Y coordinate. If None, uses current position.
            button: Mouse button to click ('left', 'right', 'middle')
            clicks: Number of clicks
        """
        self._enforce_rate_limit()
        
        # TODO: Implement actual mouse clicking
        # For now, just log the action
        if x is not None and y is not None:
            logger.info(f"Clicking {button} button at ({x}, {y}) {clicks} times")
        else:
            logger.info(f"Clicking {button} button at current position {clicks} times")
        
        time.sleep(self.safety_delay)
    
    def type_text(self, text, interval=0.01):
        """
        Type text with the keyboard.
        
        Args:
            text: Text to type
            interval: Time between keypresses
        """
        self._enforce_rate_limit()
        
        # TODO: Implement actual typing
        # For now, just log the action
        logger.info(f"Typing text: {text}")
        
        time.sleep(self.safety_delay)
    
    def press_key(self, key):
        """
        Press a single key.
        
        Args:
            key: Key to press (e.g., 'enter', 'tab', 'a', etc.)
        """
        self._enforce_rate_limit()
        
        # TODO: Implement actual key pressing
        # For now, just log the action
        logger.info(f"Pressing key: {key}")
        
        time.sleep(self.safety_delay)
