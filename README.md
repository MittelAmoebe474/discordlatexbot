# Discord LaTeX Bot

A simple Discord bot that listens for LaTeX equations in a specific channel and replies with rendered PNG images (via [Codecogs](https://latex.codecogs.com/)).

## Features

- Detects inline `$…$` and display `$$…$$` LaTeX math.
- Renders equations at high DPI with white text on transparent background.
- Replies with one image per equation.

## Prerequisites

- Python 3.8+
- A Discord bot application with **Bot** token
- The ID of the Discord server (Guild) and the dedicated LaTeX channel

## Setup

1. **Clone the repo** (or place the script in a folder):

   ```bash
   git clone https://github.com/yourusername/discord-latex-bot.git
   cd discord-latex-bot
   ```

2. **Create and activate a virtualenv** (optional, but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate    # on Linux/macOS
   venv\Scripts\activate       # on Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the project root with these entries:

   ```ini
   DISCORD_TOKEN=your-bot-token-goes-here
   GUILD_ID=123456789012345678
   LATEX_CHANNEL_ID=987654321098765432
   ```

   - **DISCORD_TOKEN**: Your Discord bot token from the Developer Portal.
   - **GUILD_ID**: The ID of your server.
   - **LATEX_CHANNEL_ID**: The channel ID where people will post LaTeX.

## Usage

1. **Invite the bot** to your server with at least:
   - Read Messages
   - Send Messages
   - Attach Files

2. **Run the bot**:

   ```bash
   python main.py
   ```

3. **Post equations** in your LaTeX channel, for example:

   ```
   Here’s the quadratic formula: $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$
   ```

   The bot will reply with a PNG image of each equation.

## Logging & Debugging

- The bot prints every incoming message to console.
- If image generation fails, it logs the HTTP status or exception.

## Customization

- **DPI**, **font size**, and **color** are set in the script:
  ```python
  processed_latex = (
      f'\dpi{{300}} '      # change DPI here
      f'\color{{white}} '  # change text color
      f'\Large '           # change font size
      ...
  )
  ```
- You can tweak the URL template or switch to another LaTeX-rendering service if desired.

## License

MIT License. Feel free to fork and improve!
```

Save that as `README.md` alongside your `main.py` (or whatever you named it) and `requirements.txt`. You’re good to go!
