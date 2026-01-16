import logging
from datetime import datetime, timezone

from aiogram import Router, F
from aiogram.types import Message

from bot.services.plan_generator import PlanGenerator
from bot.utils.formatters import format_for_telegram
from bot.utils.validators import validate_input


logger = logging.getLogger(__name__)
router = Router()


@router.message(F.text & ~F.text.startswith('/'))
async def handle_plan(message: Message, plan_generator: PlanGenerator) -> None:
    if not message.text:
        return

    is_valid, error_text = validate_input(message.text)
    if not is_valid:
        await message.answer(error_text)
        return

    await message.bot.send_chat_action(message.chat.id, 'typing')

    today_utc = datetime.now(timezone.utc).date().isoformat()

    try:
        result = await plan_generator.generate(message.text, today_utc)
    except Exception as exc:
        logger.exception('Plan generation failed: %s', exc)
        await message.answer('⚠️ Сервис временно недоступен. Попробуйте позже.')
        return

    for chunk in format_for_telegram(result, plan_generator.response_max_chars):
        await message.answer(chunk, disable_web_page_preview=True)
