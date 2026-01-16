from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    text = (
        'Привет! Я бот для генерации LegalTech-планов.\n\n'
        'Напишите идею или тезисы, и я сделаю структурированный план с календарными событиями.'
    )
    await message.answer(text)


@router.message(Command('help'))
async def cmd_help(message: Message) -> None:
    text = (
        'Как пользоваться:\n'
        '1) Отправьте тему или тезисы (10-4000 символов).\n'
        '2) Получите план с метаданными и календарными мероприятиями.\n\n'
        'Команды:\n'
        '/start — начало\n'
        '/help — помощь\n'
        '/examples — примеры'
    )
    await message.answer(text)


@router.message(Command('examples'))
async def cmd_examples(message: Message) -> None:
    text = (
        'Примеры запросов:\n'
        '- AI ассистент для анализа договоров в РК\n'
        '- Legal research по судебной практике РК\n'
        '- RegTech решение для KYC/AML в банках\n'
    )
    await message.answer(text)
