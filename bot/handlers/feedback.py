from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command('more'))
@router.message(Command('shorter'))
@router.message(Command('change'))
@router.message(Command('format'))
async def cmd_feedback(message: Message) -> None:
    await message.answer('Функция уточнения плана в разработке.')
