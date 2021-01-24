import socket
import os
import _thread
import sys
import math
import toml
#from actions import actions


class IRA_WEBSERVER():
    def _start_server():
        print("Starting websocket...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.bind(('', 80))
        s.listen()
        while 1:
            print("Waiting for connections...")
            conn, addr = s.accept()
            print("connection from" + str(addr))
            with conn:
                print('Connected by', addr)
                data = conn.recv(1024).decode()
                data = data.split("GET ")
                data = data[1].split(" HTTP")[0]

                if "?" in data:
                    parameters, data = IRA_WEBSERVER._load_parameters(
                        data)
                requestpath = "websocket/html/public/" + str(data)
                print("Requested path: " + str(data))
                try:
                    print("GET Parameters: " + str(parameters))
                except NameError:
                    pass
                DataToSend = ""
                if os.path.exists(requestpath) and os.path.isfile(requestpath):
                    htmlfilepath = requestpath
                    if not ".ttf" in requestpath and not ".png" in requestpath:
                        htmlfile = open(htmlfilepath, "r")
                    else:
                        htmlfile = open(htmlfilepath, "rb")
                    DataToSend = htmlfile.read()
                    htmlfile.close()
                if not os.path.exists(requestpath) and not os.path.exists(requestpath + "/index.html") and not os.path.isfile(requestpath + "/index.html"):
                    htmlfilepath = "websocket/html/ERROR404.html"
                    htmlfile = open(htmlfilepath, "r")
                    DataToSend = htmlfile.read()
                    htmlfile.close()
                if os.path.exists(requestpath) and os.path.isdir(requestpath):
                    if os.path.exists(requestpath + "/index.html") and os.path.isfile(requestpath + "/index.html"):
                        htmlfilepath = requestpath + "/index.html"
                        htmlfile = open(htmlfilepath, "r")
                        DataToSend = htmlfile.read()
                        htmlfile.close()
                    else:
                        htmlfilepath = "websocket/html/ERROR404.html"
                        htmlfile = open(htmlfilepath, "r")
                        DataToSend = htmlfile.read()
                        htmlfile.close()

                formatting_dict = IRA_WEBSERVER.formatting_dict()

                if not ".css" in requestpath and not ".ttf" in requestpath and not ".png" in requestpath and not ".js" in requestpath:
                    DataToSend = DataToSend.format(**formatting_dict)
                if not type(DataToSend) == bytes:
                    DataToSend = bytearray(DataToSend.encode())
                conn.sendall(DataToSend)
                conn.close()

    def start():
        _thread.start_new_thread(IRA_WEBSERVER._start_server, ())

    def _load_parameters(addr: str) -> dict:
        parameters = str(addr).split("?", 1)[1]
        parameters = parameters.split("=")
        x = 0
        for i in parameters:
            parameters[x] = i.split("&")
            x = x + 1
        parameterdict = dict()
        x = 0
        for i in parameters:
            if x % 2 == 0:  # gerade Zahl
                parameterdict[i] = ""
            else:
                parameterdict[parameters[x - 1]] = i.replace("+", " ")
            x = x + 1
        return parameterdict, str(addr).split("?", 1)[0]

    def parameter_handler(parameters: dict):
        try:
            if parameters["createNewWatchedPath"] == "True" and not parameters["path"] == "":
                actions.NewPath(str(parameters["path"]))
            if parameters["deleteWatchedPath"] == "True" and not parameters["path"] == "":
                actions.NewPath(str(parameters["path"]))
        except KeyError:
            pass

        return DataToSend

    def configurated_objects() -> str:
        tomlfile = open("config.toml", "r")
        tomlcontent = toml.load(tomlfile)
        tomlfile.close()
        html_list = ""
        for i in tomlcontent["configurated_objects"]:
            html_list = html_list + "<li style='padding: 0 px;'>" + i + "</li><br>"
        return html_list

    def formatting_dict() -> dict:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)

        formatting_dict = {}
        formatting_dict["test"] = "Hello World"
        formatting_dict["ipaddr"] = ip
        formatting_dict["configuratedobjects"] = IRA_WEBSERVER.configurated_objects()
        return formatting_dict
