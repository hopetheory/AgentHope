"""
Safety Module for AgentHope

Provides safety mechanisms for the agent.
"""

import logging
import time
from typing import Callable, Any

logger = logging.getLogger(__name__)

def rate_limited(max_calls: int, period: float):
    """Decorator to limit how often a function can be called"""
    def decorator(func: Callable):
        calls = []
        
        def wrapper(*args, **kwargs) -> Any:
            now = time.time()
            calls[:] = [call for call in calls if call > now - period]
            
            if len(calls) >= max_calls:
                wait_time = period - (now - calls[0])
                logger.warning(f"Rate limit reached. Waiting {wait_time:.2f} seconds")
                time.sleep(wait_time)
                return wrapper(*args, **kwargs)
                
            calls.append(now)
            return func(*args, **kwargs)
            
        return wrapper
    return decorator

def confirm_action(prompt: str) -> bool:
    """Require confirmation before performing sensitive actions"""
    logger.warning(f"CONFIRMATION REQUIRED: {prompt}")
    # In actual implementation, this would get user input
    return True
