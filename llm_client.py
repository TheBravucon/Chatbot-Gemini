import time
from typing import Dict, List, Optional
import google.generativeai as genai
from config import settings


class GeminiClient:
    def __init__(self, api_key: str, model_name: str):
        if not api_key or not model_name:
            raise ValueError("API key no configurada")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate(
            self,
            system_prompt: str,
            history: List[Dict[str, str]],
            user_message: int,
            max_retries: int,
            timeout_seconds: int
    ) -> str:
        attempts = 0
        last_error: Optional[Exception] = None

        convo = self.model.start_chat(history=[{"role": "user", "parts": system_prompt}] + [{"role":m["role"], "parts":m["content"]} for m in history])

        while attempts < max_retries:
            try:
                response = convo.send_message(user_message)
                text = getattr(response, "text", "")
                if not text:
                    raise ValueError("Respuesta vacia del modelo")
                return text
            except ValueError as e:
                last_error = e
                sleep_seconds = 2 ** attempts
                time.sleep(sleep_seconds)
                attempts += 1
