# AI Content Team — Streamlit Workspace

Brief toolkit for content-generation agents and a Streamlit demo app.

## Overview

This repository contains a small framework of agent-based modules, tools, and a Streamlit app used to orchestrate AI-assisted content workflows. It includes planner, researcher, reviewer, and writer agents, utilities for prompts and configuration, and GitHub MCP intergration.

## Repository structure

- `streamlit_app.py` — Streamlit front-end for running demos and interacting with agents.
- `Agents/` — Agent implementations: `PlannerAgent.py`, `ResearcherAgent.py`, `ReviewAgent.py`, `WriterAgent.py`.
- `Code/` — Core utilities: `llm.py`, `prompt_builder.py`, `load_config.py`, `paths.py`.
- `Config/` — YAML prompt templates for each agent.
- `Tools/` — External integrations: `websearcher.py`, `github_mcp.py`.
- `Workflows/` — Graphs and workflow definitions.
- `requirements.txt` — Python dependencies.

## Quickstart

1. Create and activate a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app.

```bash
streamlit run streamlit_app.py
```

## How to use

- Open the Streamlit UI to run demos and interact with agent workflows.
- Edit YAML prompts in `Config/` to customize agent behavior.
- Use modules in `Code/` to extend LLM integrations or modify prompt building.

## Key files

- [streamlit_app.py](streamlit_app.py) — app entry point
- [Agents/PlannerAgent.py](Agents/PlannerAgent.py)
- [Agents/ResearcherAgent.py](Agents/ResearcherAgent.py)
- [Agents/ReviewAgent.py](Agents/ReviewAgent.py)
- [Agents/WriterAgent.py](Agents/WriterAgent.py)
- [Code/llm.py](Code/llm.py) — LLM wrapper

## Contributing

Open an issue or PR with clear description and tests. Keep changes focused and documented.

## License

