import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Config:
    telegram_bot_token: str
    anthropic_api_key: str
    claude_model: str
    max_tokens: int
    log_level: str
    response_max_chars: int
    request_timeout_s: int
    retry_attempts: int
    retry_base_delay_s: float


def load_config() -> Config:
    load_dotenv()

    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')

    if not telegram_bot_token:
        raise ValueError('TELEGRAM_BOT_TOKEN is required')
    if not anthropic_api_key:
        raise ValueError('ANTHROPIC_API_KEY is required')

    claude_model = os.getenv('CLAUDE_MODEL', 'claude-3-5-sonnet-20241022')
    max_tokens = int(os.getenv('MAX_TOKENS', '2048'))
    log_level = os.getenv('LOG_LEVEL', 'INFO')
    response_max_chars = int(os.getenv('RESPONSE_MAX_CHARS', '3900'))
    request_timeout_s = int(os.getenv('REQUEST_TIMEOUT_S', '30'))
    retry_attempts = int(os.getenv('RETRY_ATTEMPTS', '2'))
    retry_base_delay_s = float(os.getenv('RETRY_BASE_DELAY_S', '1.0'))

    return Config(
        telegram_bot_token=telegram_bot_token,
        anthropic_api_key=anthropic_api_key,
        claude_model=claude_model,
        max_tokens=max_tokens,
        log_level=log_level,
        response_max_chars=response_max_chars,
        request_timeout_s=request_timeout_s,
        retry_attempts=retry_attempts,
        retry_base_delay_s=retry_base_delay_s,
    )
