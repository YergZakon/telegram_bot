from dataclasses import dataclass

from bot.services.claude_service import ClaudeService


@dataclass
class PlanGenerator:
    claude_service: ClaudeService
    system_prompt: str
    response_max_chars: int

    async def generate(self, user_input: str) -> str:
        return await self.claude_service.generate_plan(user_input, self.system_prompt)
