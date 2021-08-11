# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 09:49:48 2021

@author: Unrated
"""
import socket
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
# HOST = '192.168.43.1'
PORT = 12345       # Port to listen on (non-privileged ports are > 1023)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
while True:
    print(str(sock.recv(1024), 'utf-8'), end="", flush=True)
