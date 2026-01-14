from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv

load_dotenv()


def create_crew(user_story: str) -> Crew:
    if not user_story or not isinstance(user_story, str):
        raise ValueError("User story must be a non-empty string")

    # ✅ CrewAI-native Groq LLM (reads GROQ_API_KEY correctly)
    llm = LLM(
    model="groq/llama-3.1-8b-instant",
    temperature=0
)


    requirements_analyst = Agent(
        role="Senior Business Analyst with E-commerce Domain Expertise",
        goal=(
            "Extract, analyze, and structure clear, testable functional and "
            "non-functional requirements from business user stories"
        ),
        backstory=(
            "You are a senior business analyst specializing in e-commerce platforms. "
            "You excel at converting natural language user stories into structured, "
            "testable requirements, identifying edge cases, business rules, and gaps."
        ),
        llm=llm,
        verbose=True
    )

    task = Task(
        description=f"""
Analyze the following e-commerce user story and acceptance criteria.

USER STORY:
{user_story}

TASK INSTRUCTIONS:
1. Extract at least 10 functional requirements
2. Extract non-functional requirements (performance, usability, reliability)
3. Identify edge cases and boundary conditions
4. Identify at least 3 gaps or ambiguities
5. Assign priority and categories
6. Output ONLY valid JSON using the schema below

OUTPUT JSON SCHEMA:
{{
  "functional_requirements": [
    {{
      "id": "FR001",
      "description": "",
      "priority": "High|Medium|Low",
      "category": "",
      "testable": true
    }}
  ],
  "non_functional_requirements": [
    {{
      "id": "NFR001",
      "description": "",
      "type": "Performance|Usability|Reliability|Security",
      "measurable": true
    }}
  ],
  "edge_cases": [
    {{
      "id": "EC001",
      "description": "",
      "scenario": ""
    }}
  ],
  "gaps_identified": [
    ""
  ]
}}
""",
        expected_output="Strictly valid JSON output following the provided schema",
        agent=requirements_analyst
    )

    return Crew(
        agents=[requirements_analyst],
        tasks=[task],
        process="sequential",
        verbose=True
    )
