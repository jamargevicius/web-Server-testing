'''   threeLEDcheckbox2.py 

'''
import time
import signal
import sys
import RPi.GPIO as GPIO
from flask import Flask, render_template, request, json
import threading
import json 

# *******************************************************************************************************
# ****************************    constants and delcarations   *************************
# *******************************************************************************************************
app = Flask(__name__)

whiteLEDgpio = 14
greenLEDgpio = 15
redLEDgpio = 18
GPIO.setwarnings(False) # supresses warning about GPIO already configured when restart the program
GPIO.setmode(GPIO.BCM)
GPIO.setup(whiteLEDgpio, GPIO.OUT)
GPIO.setup(greenLEDgpio, GPIO.OUT)
GPIO.setup(redLEDgpio, GPIO.OUT)
GPIO.output(whiteLEDgpio, GPIO.LOW)
GPIO.output(greenLEDgpio, GPIO.LOW)
GPIO.output(redLEDgpio, GPIO.LOW)

# *******************************************************************************************************
# **********************************    functions   - must be put before needed *************************
# *******************************************************************************************************
@app.route("/")
def main():
   return render_template('threeLEDcheckbox2.html')     

@app.route("/newWebPageDisplay")
def updatePage():
   jsonLEDs = displayStates()
   print("hello from /newWebPageDisplay ... jsonLEDs = ", jsonLEDs)
   return json.dumps(jsonLEDs)

@app.route("/update/<changePin>/<action>") # executes when someone requests a URL with the pin number and action in it:
def action(changePin, action):
   if (changePin == "whiteLEDgpio"):   LEDgpio = whiteLEDgpio
   elif (changePin == "greenLEDgpio"): LEDgpio = greenLEDgpio
   elif (changePin == "redLEDgpio"):   LEDgpio = redLEDgpio
   #print("Hello from /update .... change pin is: ", changePin)
   if action == "on":               # If the action part of the URL is "on," execute the code indented below:
      GPIO.output(LEDgpio, GPIO.HIGH)      # Set the pin high:
   if action == "off":
      GPIO.output(LEDgpio, GPIO.LOW)
   jsonLEDs = displayStates()
   return json.dumps(jsonLEDs)

def displayStates():
   whiteLEDstatus = GPIO.input(whiteLEDgpio)
   greenLEDstatus = GPIO.input(greenLEDgpio)
   redLEDstatus   = GPIO.input(redLEDgpio)
   jsonLEDs = {"whiteLEDgpioNumber": str(whiteLEDgpio), "currentWhiteLEDstatus": str(whiteLEDstatus), \
               "greenLEDgpioNumber": str(whiteLEDgpio), "currentGreenLEDstatus": str(greenLEDstatus), \
               "redLEDgpioNumber":   str(whiteLEDgpio), "currentRedLEDstatus":   str(redLEDstatus) } 
   print("jsonLEDs = ", jsonLEDs)
   return jsonLEDs

def signal_handler(sig, frame):
   print('You pressed Ctrl+C -- all LEDs turned off now')
   GPIO.output(whiteLEDgpio,GPIO.LOW)
   GPIO.output(greenLEDgpio,GPIO.LOW)
   GPIO.output(redLEDgpio,GPIO.LOW)
   sys.exit(0)

#*******************************************************************************************************
# **********************************    Main   *********************************************************
# ******************************************************************************************************
if __name__ == "__main__":
   signal.signal(signal.SIGINT, signal_handler)  # trap Ctrl-C
   app.run(host='0.0.0.0', port=80)  # can't thread this for some readon
 

'''
   def displayStates():
      whiteLEDstatus = GPIO.input(whiteLEDgpio)
      greenLEDstatus = GPIO.input(greenLEDgpio)
      redLEDstatus   = GPIO.input(redLEDgpio)
      jsonLEDs = {"whiteLEDgpioNumber": str(whiteLEDgpio), "currentWhiteLEDstatus": str(whiteLEDstatus), \
                  "greenLEDgpioNumber": str(whiteLEDgpio), "currentGreenLEDstatus": str(greenLEDstatus), \
                  "redLEDgpioNumber":   str(whiteLEDgpio), "currentRedLEDstatus":   str(redLEDstatus) } 
      print("jsonLEDs = ", jsonLEDs)
'''

'''
@app.route("/update/<changePin>/<action>") # executes when someone requests a URL with the pin number and action in it:
def action(changePin, action):
   if (changePin == "whiteLEDgpio"):   LEDgpio = whiteLEDgpio
   elif (changePin == "greenLEDgpio"): LEDgpio = greenLEDgpio
   elif (changePin == "redLEDgpio"):   LEDgpio = redLEDgpio
   print("Hello from /update .... change pin is: ", changePin)
   if action == "on":               # If the action part of the URL is "on," execute the code indented below:
      GPIO.output(LEDgpio, GPIO.HIGH)      # Set the pin high:
   if action == "off":
      GPIO.output(LEDgpio, GPIO.LOW)
   return "", 200
'''