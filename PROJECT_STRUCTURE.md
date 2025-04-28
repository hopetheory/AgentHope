# AgentHope Project Structure

## Directory Structure
```
AgentHope/
├── config/
│   └── config.yaml
├── docs/
│   ├── architecture/
│   ├── usage/
│   └── development/
├── src/
│   ├── core/
│   │   ├── engine.py
│   │   └── config.py
│   ├── vision/
│   │   └── screen_capture.py
│   ├── control/
│   │   └── input_controller.py
│   ├── nlu/
│   │   └── command_parser.py
│   ├── learning/
│   │   └── experience_tracker.py
│   ├── memory/
│   │   └── knowledge_store.py
│   ├── utils/
│   │   └── safety.py
│   └── main.py
├── tests/
│   └── test_vision.py
├── README.md
└── requirements.txt
```

## Key Files and Their Purposes

1. **main.py**: Entry point for the application that initializes all components
2. **core/engine.py**: Central coordination system that manages all components
3. **vision/screen_capture.py**: Handles capturing and analyzing screen content
4. **control/input_controller.py**: Manages keyboard and mouse input
5. **nlu/command_parser.py**: Parses natural language commands
6. **learning/experience_tracker.py**: Tracks and learns from agent experiences
7. **memory/knowledge_store.py**: Manages persistent storage of knowledge
8. **utils/safety.py**: Provides safety mechanisms for the agent

## Initial Dependencies (requirements.txt)
- python-dotenv: For environment variable management
- pyyaml: For configuration file parsing
- pyautogui: For screen capture and input control
- pillow: For image processing
- opencv-python: For computer vision capabilities
- pytesseract: For OCR (text recognition)
- pynput: For keyboard and mouse monitoring
- pyperclip: For clipboard access
