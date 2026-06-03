from Code.paths import REVIEW_PROMPT
from Code.llm import get_llm
from Code.load_config import load_prompt
from Code.prompt_builder import build_prompt_body
class ReviewAgent:

    def reviewer(self, research, writer, audiences=None):
        if audiences is None:
            audiences = ["LinkedIn", "developers", "non-developers"]
        if isinstance(audiences, str):
            audiences = [audiences]

        audience_list = ", ".join(audiences)
        prompt_input = (
            f"Audiences: {audience_list}\n\n"
            f"Research:\n{research}\n\n"
            f"Draft:\n{writer}"
        )
        config = load_prompt(REVIEW_PROMPT)
        prompt = build_prompt_body(config, prompt_input)
        llm = get_llm('llama-3.3-70b-versatile')

        result = llm.invoke(prompt)

        return {
            'reviewer': result
        }