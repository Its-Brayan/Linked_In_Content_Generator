import yaml

def load_prompt(config_path:str):
    with open(config_path,'r',encoding='utf-8') as f:
        config = yaml.safe_load(f)
        return config