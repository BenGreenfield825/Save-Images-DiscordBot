from discord.ext import commands
import uuid

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print("Bot is ready")


@client.command()
async def save(ctx):
    imageName = str(uuid.uuid4()) + '.jpg'
    await ctx.message.attachments[0].save(imageName)

client.run('TOKEN')

