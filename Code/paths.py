import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(ROOT_DIR,'Config')
PLANNER_PROMPT = os.path.join(CONFIG_DIR,'planner_prompt.yaml')
RESEARCHER_PROMPT = os.path.join(CONFIG_DIR,'research_prompt.yaml')
REVIEW_PROMPT = os.path.join(CONFIG_DIR,'review_prompt.yaml')
WRITER_PROMPT = os.path.join(CONFIG_DIR,'writer_prompt.yaml')