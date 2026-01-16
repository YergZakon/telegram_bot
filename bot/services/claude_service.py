import asyncio
import logging
from typing import List

from anthropic import AsyncAnthropic


logger = logging.getLogger(__name__)


class ClaudeService:
    def __init__(self, api_key: str, model: str, max_tokens: int, timeout_s: int, retry_attempts: int, retry_base_delay_s: float) -> None:
        self._client = AsyncAnthropic(api_key=api_key, timeout=timeout_s)
        self._model = model
        self._max_tokens = max_tokens
        self._retry_attempts = retry_attempts
        self._retry_base_delay_s = retry_base_delay_s

    async def generate_plan(self, user_input: str, system_prompt: str) -> str:
        last_error: Exception | None = None

        for attempt in range(self._retry_attempts + 1):
            try:
                response = await self._client.messages.create(
                    model=self._model,
                    max_tokens=self._max_tokens,
                    system=system_prompt,
                    messages=[{"role": "user", "content": user_input}],
                )
                return self._extract_text(response.content)
            except Exception as exc:  # pragma: no cover - network errors are environment-specific
                last_error = exc
                if attempt >= self._retry_attempts:
                    break
                delay = self._retry_base_delay_s * (2 ** attempt)
                logger.warning('Claude API error, retrying in %.1fs: %s', delay, exc)
                await asyncio.sleep(delay)

        raise RuntimeError('Claude API request failed') from last_error

    @staticmethod
    def _extract_text(content: List[object]) -> str:
        parts: List[str] = []
        for item in content:
            text = getattr(item, 'text', None)
            if isinstance(text, str):
                parts.append(text)
        return '\n'.join(parts).strip()
