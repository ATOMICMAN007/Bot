from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions, MissingPermissions



class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Extention loaded: Moderation")

    # Giving role via command

    @commands.command(pass_context=True)
    @has_permissions(manage_roles=True)
    # This must be exactly the name of the appropriate role
    @commands.has_role("Moderator")
    async def addrole(self, ctx, ROLE: str):
        if not ctx.message.guild:
            return
        member = ctx.message.author
        role = get(member.guild.roles, name=ROLE)
        await member.add_roles(role)
        await ctx.message.channel.send(f"Given role: {ROLE}")

    @commands.command(pass_context=True)
    @has_permissions(manage_roles=True)
    # This must be exactly the name of the appropriate role
    @commands.has_role("Moderator")
    # Removing role via command
    async def removerole(self, ctx, ROLE: str):
        member = ctx.message.author
        role = get(member.guild.roles, name=ROLE)
        await member.remove_roles(role)
        await ctx.message.channel.send(f"Removed role: {ROLE}")

    @addrole.error
    async def addrole_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have permission to do that!")

    @removerole.error
    async def removerole_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have permission to do that!")


def setup(bot):
    bot.add_cog(Moderation(bot))
