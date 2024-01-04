import os
import discord
from embed_service import EmbedService
from image_service import ImageService


bot = discord.Bot()
image_service = ImageService()
embed_service = EmbedService()


async def img_category_autocomplete(ctx: discord.AutocompleteContext):
    available_categories = image_service.get_available_categories()
    matching_categories = [cat for cat in available_categories if cat.lower().startswith(ctx.value.lower())]
    return sorted(matching_categories)


@bot.command(name="img", description="Show an image to your friends!")
async def img(ctx: discord.ApplicationContext, category: discord.Option(str, autocomplete=img_category_autocomplete, description="Choose image category")):
    category = str(category).lower()
    try:
        embed = embed_service.make_success_embed()
        img_path = image_service.get_random_image_in_category(category)
        img_extension = os.path.splitext(img_path)[1]
        img_name = "image" + img_extension
        file = discord.File(img_path, filename=img_name)
        embed.title = category.capitalize()
        embed.set_image(url="attachment://" + img_name)
        await ctx.response.defer()
        await ctx.respond(embed=embed, file=file)
    except AttributeError:
        embed = embed_service.make_error_embed()
        available_categories = ", ".join(sorted(image_service.get_available_categories()))
        embed_msg = f"Uh oh! I couldn't find that category.\nYou can use one of the categories below:\n**{available_categories}**"
        embed.title = category.capitalize()
        embed.add_field(name="Category does not exist!", value=embed_msg)
        await ctx.respond(embed=embed, ephemeral=True)


@bot.command(name="img-categories", description="List available image categories!")
async def img_categories(ctx):
    embed = embed_service.make_success_embed()
    available_categories = ", ".join(image_service.get_available_categories())
    embed.title = "Available categories"
    embed.add_field(name="List of available categories", value=available_categories)
    await ctx.respond(embed=embed)


if __name__ == "__main__":
    token = os.getenv("DC_IMAGER_TOKEN")
    if token:
        bot.run(token)
    else:
        print("Discord bot authentication token not specified!")
        print("You need to set DC_IMAGER_TOKEN environment variable for the bot to work.")
        exit(1)

