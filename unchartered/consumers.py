# -*- coding: utf-8 -*-
import json, datetime, socket, sys, re, threading
from django.utils import timezone
from channels.generic.websocket import WebsocketConsumer

def apply_backspace(s):
    while True:
        # if you find a character followed by a backspace,
        t = re.sub('.\b', '', s, count=1)
        if len(s) == len(t):
            # now remove any backspaces from beginning
            return re.sub('\b+', '', t)
        s = t

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
# HOST = '192.168.43.1'
PORT = 12345       # Port to listen on (non-privileged ports are > 1023)


def serversocket():
    global conns
    conns = []
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        print(s.getsockname()[1])
        #s.bind(('', 0))
        s.listen(1)
        conn, addr = s.accept()
        conns.append(conn)
    
thread = threading.Thread(target=serversocket, daemon=True)
thread.start()
# sock.send(None)

class RealTimeText(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def connect(self):
        self.accept()
        
    def disconnect(self, close_code):
        pass
    
    def send_result(self):
        self.send(text_data = json.dumps({
            'load': 'fuck',
        }))    
        
    def receive(self, text_data):
        # print(text_data, print(type(text_data)))
        msg = json.loads(text_data)['msg']
        try:
            bmsg = bytes(msg, 'utf-8')
            for conn in conns:
                conn.sendall(bmsg)
        except NameError:
            pass # no connection yet
        # self.sock.send(msg) # the send api of coroutines