# Azure Function LLM Project

This is a bare-bones Azure Function project set up for integrating LLM (Large Language Model) logic.

## Setup

1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Add your LLM dependencies to `requirements.txt` as needed.
3. Configure your local settings in `local.settings.json` (do not commit this file).
4. Run the function locally:
   ```bash
   func start
   ```

## File Overview
- `main.py`: Main Azure Function entry point (add your LLM logic here)
- `requirements.txt`: Python dependencies
- `.gitignore`: Files/folders to ignore in git
- `local.settings.json`: Local Azure settings (not for git) 