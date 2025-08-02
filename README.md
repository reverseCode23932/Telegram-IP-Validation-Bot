# Telegram IP Location Bot

This is an asynchronous Telegram bot that receives an IP address or domain name from a user and replies with geolocation information and a Google Maps link.

## Features

- Asynchronous (fast and scalable)
- Uses [ip-api.com](http://ip-api.com/) for IP/domain geolocation
- Replies with country, region, city, ISP, coordinates, and Google Maps link
- Logs all activity to `bot.log`

## Requirements

- Python 3.8+
- Telegram bot token

Install dependencies:
```
pip install -r requirements.txt
```

## Usage

1. **Set your Telegram bot token as an environment variable:**

   On Windows:
   ```
   set TELEGRAM_BOT_TOKEN=your_bot_token
   ```

   On Linux/macOS:
   ```
   export TELEGRAM_BOT_TOKEN=your_bot_token
   ```

2. **Run the bot:**
   ```
   python main.py
   ```

3. **Interact with the bot in Telegram:**
   - Send `/start` to get a welcome message.
   - Send any IP address (e.g., `8.8.8.8`) or domain (e.g., `google.com`) to get location info.

## Example

```
User: 8.8.8.8
Bot:
IP: 8.8.8.8
Country: United States
Region: California
City: Mountain View
ISP: Google LLC
Latitude: 37.4056
Longitude: -122.0775
Google Maps: https://www.google.com/maps?q=37.4056,-122.0775
```

## Logging

All bot activity and errors are logged to `bot.log`.

## License

MIT
