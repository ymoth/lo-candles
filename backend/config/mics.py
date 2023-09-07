import aiogram

from config import settings

bot = aiogram.Bot(
    token=settings.TELEGRAM_API_TOKEN
)

ADMIN_TELEGRAM_ID = 6092172288
