import os
import re
from io import BytesIO
import discord
from dotenv import load_dotenv
import aiohttp
from urllib.parse import quote

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
LATEX_CHANNEL_ID = os.getenv('LATEX_CHANNEL_ID')
GUILD_ID = os.getenv('GUILD_ID')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print(f"Guild ID: {GUILD_ID}")
    print(f"Latex Channel ID: {LATEX_CHANNEL_ID}")

@client.event
async def on_message(message):
    print(f"Received message from {message.author} in {message.channel}")
    print(f"Message content: {message.content}")

    if message.author.bot:
        return

    if message.channel.id != int(LATEX_CHANNEL_ID):
        print("Message not in latex channel")
        return

    latex_matches = re.findall(r'\$\$([^$]+)\$\$|\$([^$]+)\$', message.content)
    equations = []

    print(f"Found {len(latex_matches)} equations")

    for match in latex_matches:
        if match[0]:
            equations.append(match[0].strip())
        elif match[1]:
            equations.append(match[1].strip())

    if not equations:
        return

    async with aiohttp.ClientSession() as session:
        files = []
        for idx, eq in enumerate(equations, start=1):
            processed_latex = (
                    f'\\dpi{{300}} '                    # Higher DPI for better quality
                    f'\\color{{white}} '                 # White text
                    f'\\Large '                          # Larger font size
                    f'\\displaystyle '                   # Force display math style
                    f'{{ {eq} }}'                        # Wrap in braces for safety
                )
            encoded_latex = quote(processed_latex)
            url = f'https://latex.codecogs.com/png.latex?{encoded_latex}'

            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        image_data = await response.read()
                        file_name = f'equation_{idx}.png'
                        file = discord.File(BytesIO(image_data), filename=file_name)
                        files.append(file)
                    else:
                        print(f"Failed to generate image for equation {idx}: HTTP {response.status}")
            except Exception as e:
                print(f"Error processing equation {idx}: {e}")

        if files:
            await message.reply(files=files)

if __name__ == '__main__':
    client.run(TOKEN)
