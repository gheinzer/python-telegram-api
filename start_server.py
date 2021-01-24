from websocket import IRA_WEBSERVER
import traceback

while 1:
    try:
        IRA_WEBSERVER._start_server()
    except:
        pass
