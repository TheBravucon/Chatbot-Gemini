from config import settings
from llm_client import GeminiClient
from memory import ConversationMemory
from prompts import build_system_prompt, collapse_history
from roles import RolesPreset, ROLES_SYSTEM_PROMPT


class ChatService:
    def __init__(self, role: RolesPreset):
        self.role = role
        self.memory = ConversationMemory(max_messages=settings.max_history_messages)
        self.client = GeminiClient(
            api_key=settings.api_key,
            model_name=settings.model
        )

    def set_role(self, role: RolesPreset):
        self.role = role

    def ask(self, prompt: str) -> str:
        system_prompt = build_system_prompt(ROLES_SYSTEM_PROMPT[self.role])
        history = collapse_history(self.memory.get())
        response_text = self.client.generate(
            system_prompt=system_prompt,
            history=history,
            user_message=prompt,
            max_retries=settings.max_retries,
            timeout_seconds=settings.timeout_seconds
        )

        self.memory.add_user_message(prompt)
        self.memory.add_model(response_text)
        return response_text

    def reset(self):
        self.memory.clear()
