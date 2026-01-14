# Requirements Analyst Agent – Assignment 2

## Overview
This project implements an AI-powered Requirements Analyst Agent using the **CrewAI framework**.
The agent analyzes e-commerce user stories and automatically extracts structured, testable requirements.

## Framework Usage (Critical Requirement)
This solution is built using **CrewAI**, satisfying the assignment requirement for an AI agent framework.

### AI Components Used
- **Framework**: CrewAI
- **Agent**: Requirements Analyst Agent
- **Task**: Requirement Extraction Task
- **LLM**: Groq-hosted LLaMA 3 model
- **Orchestration**: Crew with single-agent execution

No rule-based or keyword-matching logic is used.
All outputs are generated dynamically via an LLM.

## Architecture
```User Story
↓
CrewAI Agent (LLM-powered)
↓
Task Execution
↓
Structured JSON Output```


## Files
- `agents/requirements_agent.py` – Defines AI agent with role, goal, and LLM
- `tasks/requirements_task.py` – Defines task instructions and schema
- `crew.py` – Combines agent and task using CrewAI
- `main.py` – Executes the crew
- `output/sample_output.json` – Generated result

## Output Schema
The agent outputs strictly valid JSON including:
- Functional requirements
- Non-functional requirements
- Edge cases
- Gaps and ambiguities

## How to Run
```bash
pip install -r requirements.txt
python main.py
