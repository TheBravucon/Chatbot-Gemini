from typing import List, Dict

def build_system_prompt(role_instructions:str) -> str:
    base = (
        "Sos un chatbot de consola que responde en español de forma clara y util."
        "Si el usuario pide codigo, inclui explicaciones breves."
        "Evita informacion inventada. Y pedi aclaraciones si faltan datos."
    )
    return base + f"contexto de rol: {role_instructions}"

def collapse_history(history: List[Dict[str, str]]) -> List[Dict[str, str]]:
    return history