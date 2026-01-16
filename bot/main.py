import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from bot.config import load_config
from bot.handlers import feedback, plan, start
from bot.prompts.system_prompts import PLAN_GENERATOR_SYSTEM_PROMPT
from bot.services.claude_service import ClaudeService
from bot.services.plan_generator import PlanGenerator


async def main() -> None:
    config = load_config()

    logging.basicConfig(
        level=config.log_level,
        format='%(asctime)s %(levelname)s %(name)s: %(message)s',
    )

    bot = Bot(
        token=config.telegram_bot_token,
        default=DefaultBotProperties(parse_mode='HTML'),
    )
    dp = Dispatcher()

    claude_service = ClaudeService(
        api_key=config.anthropic_api_key,
        model=config.claude_model,
        max_tokens=config.max_tokens,
        timeout_s=config.request_timeout_s,
        retry_attempts=config.retry_attempts,
        retry_base_delay_s=config.retry_base_delay_s,
    )

    plan_generator = PlanGenerator(
        claude_service=claude_service,
        system_prompt=PLAN_GENERATOR_SYSTEM_PROMPT,
        response_max_chars=config.response_max_chars,
    )

    dp.include_router(start.router)
    dp.include_router(plan.router)
    dp.include_router(feedback.router)

    me = await bot.get_me()
    logging.getLogger(__name__).info('Bot started: @%s (%s)', me.username, me.id)

    await dp.start_polling(bot, plan_generator=plan_generator)


if __name__ == '__main__':
    asyncio.run(main())
