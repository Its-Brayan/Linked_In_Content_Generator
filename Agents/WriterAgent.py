from Code.paths import WRITER_PROMPT
from Code.llm import get_llm
from Code.load_config import load_prompt
from Code.prompt_builder import build_prompt_body
class WriterAgent:

    def run(self, research, plan: str, audiences=None):
        if audiences is None:
            audiences = ["LinkedIn", "developers", "non-developers"]
        if isinstance(audiences, str):
            audiences = [audiences]

        audience_list = ", ".join(audiences)
        research_text = research.get('readme', '') if isinstance(research, dict) else str(research)
        repo_tree = research.get('tree', '') if isinstance(research, dict) else ''
        input_string = (
            f"Audiences: {audience_list}\n\n"
            f"Research:\n{research_text}\n\n"
            f"Repository tree:\n{repo_tree}\n\n"
            f"Plan:\n{plan}"
        )

        llm = get_llm('llama-3.1-8b-instant')
        config = load_prompt(WRITER_PROMPT)
        prompt = build_prompt_body(config, input_string)
        result = llm.invoke(prompt)
        return {
            "written": result
        }
