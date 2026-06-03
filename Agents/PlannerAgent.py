from Code.prompt_builder import build_prompt_body
from Code.llm import get_llm
from Code.load_config import load_prompt
from Code.paths import PLANNER_PROMPT
class PlannerAgent:

    def run(self, query: str, audiences=None):
        if audiences is None:
            audiences = ["LinkedIn", "developers", "non-developers"]
        if isinstance(audiences, str):
            audiences = [audiences]

        audience_list = ", ".join(audiences)
        prompt_input = f"Audiences: {audience_list}\n\nUser request:\n{query}"

        llm = get_llm('llama-3.1-8b-instant')
        config = load_prompt(PLANNER_PROMPT)
        prompt = build_prompt_body(config, prompt_input)
        result = llm.invoke(prompt)

        return {
            'planner': result
        }
        
