#!/usr/bin/env python

import time
import socket
import scrollphathd

# Uncomment the below if your display is upside down
# (e.g. if you're using it in a Pimoroni Scroll Bot)
# scrollphathd.rotate(degrees=180)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

# set a more eye-friendly default brightness
scrollphathd.write_string(hostname + " " + IPAddr, brightness=0.5)

# Auto scroll using a while + time mechanism (no thread)
while True:
    # Show the buffer
    scrollphathd.show()
    # Scroll the buffer content
    scrollphathd.scroll()
    # Wait for 0.1s
    time.sleep(0.1)
