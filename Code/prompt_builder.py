from typing import Union, Dict, List,Any

def lower_first_character(text: str) -> str:
    
    return text[0].lower() + text[1:] if text else text


def format_prompt_section(lead_in:str, value:Union[str, list[str]]) -> str:

    if isinstance(value,list):
        formatted_value = "".join(f"{item}" for item in value)
    else:
        formatted_value = value

    return f"{lead_in}\n{formatted_value}"


def build_prompt_body(
        prompt_config: Dict[str,Any],
        input_string: Union[str, list[str], dict[str, Any]] | None = None,
        finalize:bool = True,
)-> str:
    prompt_parts = []

    if role := prompt_config.get('role'):
        prompt_parts.append(f"You are a {lower_first_character(role.strip())}")
    
    if instructions := prompt_config.get('instructions'):
        if not instructions:
            raise ValueError("Instructions are required")
        prompt_parts.append(format_prompt_section(f"your tasks are as follows",instructions))
    
    if goal := prompt_config.get('goal'):
        prompt_parts.append(format_prompt_section(f"Your goal is to achieve the following outcome",goal))

    if tone := prompt_config.get('style_or_tone'):
        prompt_parts.append(format_prompt_section("format these style and tone guidance in your response",tone))

    if examples := prompt_config.get('examples'):
        if isinstance(examples,list):
            for i, example in enumerate(examples,1):
                prompt_parts.append(f"Examples: {i} \n {example}")
            
        else:
            prompt_parts.append(str(examples))
    
    if constraints := prompt_config.get('constraints'):
        prompt_parts.append(format_prompt_section("Ensure your response follows this format",constraints))

    if input_string is not None:
        prompt_parts.append(format_prompt_section("Input", input_string))

    return "\n\n".join(prompt_parts)