# Telegram Bot API Library
## Requirements
- Module requests (You can get it on: https://www.pypi.com/project/requests/)

## Errors and Exceptions
- `BotNotExistsError`: When the bot not exists, this error will raise.
- `NoInternetConnectionError`: When the computer has no Internet, this error will raise.

## Help
If you need help, just type `python -m telegrambot --help` to the shell. 

## Installation
For installing this library as python module, you just need to run `install.py`. 

If you want to uninstall, just type `python -m telegrambot --uninstall` to the shell. Then, the module will uninstall itself.

## Usage and initalisation
```python
import telegrambot
bot = telgrambot.bot(apikey: str)
```
Parameters
- apikey: 
Required, string. The API-Key of your bot (like `1234:abcdefg`).

## Methods
### Send a Text Message
You can send a Text message using the `bot.sendTextMessage()`
#### Syntax:
```python
bot.sendTextMessage(chat_id, text[, disable_web_page_preview = False, disable_notification = False, reply_to_message_id = None, allow_sending_without_reply = True, parse_mode = `MarkdownV2`])
```

#### Parameters:
- `chat_id`: Required, integer or string. Unique identifier of the chat.
- `text`: Required, string. The text to send as message.
- `disable_web_page_preview`: Optional, bool. Disabels the link preview for this message. Default is False.
- `disable_notification`: Optional, bool. Sends the message silently, when set to True. Default is False.
- `reply_to_message_id`: Optional, integer. If the message is a reply, the ID of the original message. Set this parameter to None, if you don`t want to send the message as a reply. Default is None.
- `allow_sending_without_reply`: Optional, integer. Sends the message even is the reply_to_message_id is invalid or not set. Default is True.
-` parse_mode`: Optional, string. Mode for parsing entities in the message text. Must be set to:
    - `MarkdownV2`
    - `HTML`
    - `Markdown`

    Default is `MarkdownV2`