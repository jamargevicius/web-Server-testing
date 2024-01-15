# web-Server-testing
place for test code for ESP32s and RPi's that incorporate web servers

threeLEDcheckbox -- this is python-based code and html code project. It uses Flask/Jinja in a Raspberry Pi to create a webserver with 3 LEDs attached. These LEDs can be turned on/off via the html code requested by a browser.
requirements:
- Flask install is required on the RPi.
- make a directory on the RPi where the main python code will be put; make another /template directory under that; this will hold the html code.
- to run the server, use sudo python3 threeLEDcheckbox.py in the main directory, then from a browser, call up the IP address of the RPi server.
