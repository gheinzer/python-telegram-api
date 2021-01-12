import requests
import socket


class Error(OSError):
    pass


class BotNotExistsError(Error):
    """
    When the bot not exists, this error will raise.
    """


class NoInternetConnectionError(Error):
    """
    When the computer has no Internet, this error will raise.
    """


class bot:
    def _checkInternetConnection(self):
        """
        This function is checking the internet connection with making a head-request for google.com.
        """
        try:
            requests.head(url="http://www.google.com")
            return True
        except requests.exceptions.ConnectionError:
            return False
        else:
            return False

    def __init__(self, 
    apikey: str):
        """
        Initalize the bot API. 

        Syntax:
            bot = telegrambot(apikey)

        Parameters:
            - apikey:
                Required. The API-Key of your bot (like '1234:abcdefg').
        """
        if(self._checkInternetConnection() == False):
            raise NoInternetConnectionError(
                "Your Computer is not connected to the Internet.")

        self.apikey = apikey

    def _send_request(self,method: str, request_data: list):
        request_data_str = "?"
        x = 0
        for i in request_data:
            request_data_str = request_data_str + str(request_data[x]) + "&"
            x = x + 1
        request = requests.get("https://api.telegram.org/bot" + self.apikey + "/" + method + request_data_str)

    def sendTextMessage(self, chat_id: int or str, text: str, disable_web_page_preview = False, disable_notification=False, reply_to_message_id=None, allow_sending_without_reply=True, parse_mode='MarkdownV2'):
        """
        Send a Text Message. 

        Syntax:
            sendTextMessage(chat_id, text[, disable_web_page_preview = False, disable_notification = False, reply_to_message_id = None, allow_sending_without_reply = True, parse_mode = 'MarkdownV2'])
        
        Parameters:
            - chat_id:
                Required, integer or string. Unique identifier of the chat.
            - text:
                Required, string. The text to send as message.
            - disable_web_page_preview:
                Optional, bool. Disabels the link preview for this message. Default is False.
            - disable_notification:
                Optional, bool. Sends the message silently, when set to True. Default is False.
            - reply_to_message_id:
                Optional, integer. If the message is a reply, the ID of the original message. Set this parameter to None, if you don't want to send the message as a reply. Default is None.
            - allow_sending_without_reply:
                Optional, integer. Sends the message even is the reply_to_message_id is invalid or not set. Default is True.
            - parse_mode:
                Optional, string. Mode for parsing entities in the message text. Must be set to:
                    - 'MarkdownV2'
                    - 'HTML'
                    - 'Markdown'
                Default is 'MarkdownV2'
        """
        chat_id = str(chat_id)
        text = str(text)
        disable_web_page_preview = str(disable_web_page_preview)
        disable_notification = str(disable_notification)
        allow_sending_without_reply = str(allow_sending_without_reply)
        parse_mode = str(parse_mode)

        request_data = []
        request_data.append("chat_id=" + str(chat_id))
        request_data.append("text=" + text)
        request_data.append("disable_web_page_preview=" + disable_web_page_preview)
        request_data.append("disable_notification=" + disable_notification)
        request_data.append("allow_sending_without_reply=" + allow_sending_without_reply)
        request_data.append("parse_mode=" + parse_mode)
        
        if not reply_to_message_id == None:
            reply_to_message_id = str(reply_to_message_id)
            request_data.append("reply_to_message_id=" + reply_to_message_id)
        
        self._send_request("sendMessage", request_data)
