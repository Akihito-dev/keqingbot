import time
import discord
from discord.ext import commands
from TagScriptEngine import Interpreter, block


class Calculator(commands.Cog):
   

    __version__ = "1.0.0"

    def __init__(self, bot):
        self.bot = bot
        blocks = [
            block.MathBlock(),
            block.RandomBlock(),
            block.RangeBlock(),
        ]
        self.engine = Interpreter(blocks)

    async def red_delete_data_for_user(self, **kwargs):
        return

    @commands.command(aliases=["calc","c"])
    async def calculate(self, ctx, *, query):
        """Math"""
        query = query.replace(",", "")
        engine_input = "{m:" + query + "}"
        start = time.monotonic()
        output = self.engine.process(engine_input)
        end = time.monotonic()

        output_string = output.body.replace("{m:", "").replace("}", "")
        e = discord.Embed(
            color=discord.Colour.purple(),
            title=f"Input: `{query}`",
            description=f"Output: `{output_string}`",
        )
        e.set_footer(text=f"Calculated in {round((end - start) * 1000, 3)} ms")
        await ctx.reply(embed=e)

def setup(client):
  client.add_cog(Calculator(client))

