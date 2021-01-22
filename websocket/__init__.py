import socket
import os


class IRA_WEBSERVER():
    def start():
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
                requestpath = "websocket/html/public/" + str(data)
                print("Requested path: " + str(data))
                DataToSend = ""
                if os.path.exists(requestpath) and os.path.isfile(requestpath):
                    htmlfilepath = requestpath
                    htmlfile = open(htmlfile)
                    DataToSend = htmlfile.read()
                    htmlfile.close()

                if os.path.exists(requestpath) and os.path.isdir(requestpath):
                    if os.path.exists(requestpath + "/index.html") and os.path.isfile(requestpath + "/index.html"):
                        htmlfilepath = requestpath + "/index.html"
                        htmlfile = open(htmlfile)
                        DataToSend = htmlfile.read()
                        htmlfile.close()
                    else:
                        htmlfilepath = "websocket/html/ERROR404.html"
                        htmlfile = open(htmlfile)
                        DataToSend = htmlfile.read()
                        htmlfile.close()
                conn.sendall(bytearray(DataToSend.encode()))
                conn.close()
