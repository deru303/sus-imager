import discord


class EmbedService:
    """Helper class which allows to create embeds that are consistent across the application."""

    @classmethod
    def _get_embed_base(cls) -> discord.Embed:
        embed = discord.Embed()
        embed_footer = "dc-imager by github.com/danrog303"
        embed_footer_icon = "https://avatars.githubusercontent.com/danrog303"
        embed.set_footer(text=embed_footer, icon_url=embed_footer_icon)
        return embed

    def make_success_embed(self) -> discord.Embed:
        embed = self._get_embed_base()
        embed.colour = 0xa1e899
        return embed

    def make_error_embed(self) -> discord.Embed:
        embed = self._get_embed_base()
        embed.colour = 0xdba195
        return embed
