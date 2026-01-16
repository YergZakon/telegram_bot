# LegalTech Plan Bot

Telegram-бот для генерации структурированных планов LegalTech с использованием Claude API.

## Быстрый старт

1) Создать и заполнить .env на основе .env.example
2) Установить зависимости:

```
pip install -r requirements.txt
```

3) Запустить бота:

```
python -m bot.main
```

## Переменные окружения

- TELEGRAM_BOT_TOKEN
- ANTHROPIC_API_KEY
- CLAUDE_MODEL
- MAX_TOKENS

