import os
from dotenv import load_dotenv

from typing import List, Dict

import discord
from discord.ext import commands, tasks
from discord.ext.commands import Context

from geminiAPi import setup, get_response

# ----- Global variables ----- #
env: Dict[str, str] = {}

bot = commands.Bot(command_prefix=commands.when_mentioned,
                   intents=discord.Intents.all())

# ----- Load the variables from the .env file  ----- #
def load_env(keys: List[str] = ['DISCORD_TOKEN', 'CHANNEL_ID', 'GOOGLE_API_KEY']):
    load_dotenv()
    for key in keys:
        env[key] = os.getenv(key)

# ----- Message Bot Ready  ----- #
@bot.event
async def on_ready() -> None :
    channel = bot.get_channel(int(env['CHANNEL_ID']))
    await channel.send(f'Hello! Your maid is ready!')

# Event to handle command not found errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass 

# ----- Message On Mention ----- #
@bot.event
async def on_message(message) -> None :
    # Ignore bot messages
    if message.author == bot.user:
        return

    # On Mention
    ctx = await bot.get_context(message, cls=Context)
    if bot.user in message.mentions:
        content = message.content.split(maxsplit=1)
        if len(content) > 1:
            command = content[1].strip()
            print('command is', command)
            await command_manager(message, command)
    # Let the bot process commands
    await bot.process_commands(message)

# ----- Mannage Bot Command ----- #
async def command_manager(message, command: str) -> None:
    if command == 'Hello!' :
        await message.channel.send(f'Hello {message.author.mention}!')
        return

    await message.channel.send(f'Hi! {message.author.mention} sama.')
    match command:
        case 'Bless my meal.' :
            await message.channel.send('Oishikunare moe moe kyun! :pink_heart:')
        case _ :
            await message.channel.send(get_response(command))

def main():
    load_env()
    setup(env['GOOGLE_API_KEY'])
    bot.run(env['DISCORD_TOKEN'])

if __name__ == "__main__":
    main()
