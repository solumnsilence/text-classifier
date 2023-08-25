from services.base_settings import Settings


class TelegramBotSettings(Settings):
    token: str

    class Config:
        env_prefix = 'telegram_bot_'
