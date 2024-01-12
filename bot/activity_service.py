import random
import discord
from discord.ext import tasks
from bot.image_service import ImageService


class ActivityService:
    """Service responsible for periodic updates of Discord status."""

    def __init__(self, discord_client: discord.Client, img_service: ImageService):
        self.discord_client = discord_client
        self.img_service = img_service

    @tasks.loop(minutes=5)
    async def set_discord_activity(self):
        possible_categories = self.img_service.get_available_categories()
        random_category = random.choice(possible_categories)
        activity = discord.Activity(type=discord.ActivityType.watching, name=f"*{random_category}* images")
        await self.discord_client.change_presence(activity=activity)

