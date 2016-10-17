# child.py
#
# A sample child process for receiving messages over a channel
import channel
import sys

ch = channel.Channel(sys.stdout,sys.stdin)
while True:
    try:
        item = ch.recv()
        ch.send(("child",item))
    except EOFError:
        break

