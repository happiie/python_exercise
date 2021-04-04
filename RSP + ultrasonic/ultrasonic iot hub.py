import iotc
from iotc import IOTConnectType, IOTLogLevel
import RPi.GPIO as GPIO
import time

#################Declaration for iot hub############
deviceId = "fill in your device id"
scopeId = "fill in your scope id"
deviceKey = "fill in your primary key/ secondary key"

iotc = iotc.Device(scopeId, deviceKey, deviceId, IOTConnectType.IOTC_CONNECT_SYMM_KEY)
iotc.setLogLevel(IOTLogLevel.IOTC_LOGGING_API_ONLY)

gCanSend = False
gCounter = 0

###########Declaration for ultrasonic############
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 4
GPIO_ECHO = 18
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

###########Functions for ultrasonic################

def distance():
  # set Trigger to HIGH
  GPIO.output(GPIO_TRIGGER, True)

  # set Trigger after 0.01ms to LOW
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)

  StartTime = time.time()
  StopTime = time.time()

  # save StartTime
  while GPIO.input(GPIO_ECHO) == 0:
    StartTime = time.time()

  # save time of arrival
  while GPIO.input(GPIO_ECHO) == 1:
    StopTime = time.time()

  # time difference between start and arrival
  TimeElapsed = StopTime - StartTime
  # multiply with the sonic speed (34300 cm/s)
  # and divide by 2, because there and back
  distance = (TimeElapsed * 34300) / 2

  return distance 

###########Functions for iot hub################
def onconnect(info):
  global gCanSend
  print("- [onconnect] => status:" + str(info.getStatusCode()))
  if info.getStatusCode() == 0:
     if iotc.isConnected():
       gCanSend = True

def onmessagesent(info):
  print("\t- [onmessagesent] => " + str(info.getPayload()))

def oncommand(info):
  print("- [oncommand] => " + info.getTag() + " => " + str(info.getPayload()))

def onsettingsupdated(info):
  print("- [onsettingsupdated] => " + info.getTag() + " => " + info.getPayload())

##############Run the code##################################3
if __name__ == '__main__':
  iotc.on("ConnectionStatus", onconnect)
  iotc.on("MessageSent", onmessagesent)
  iotc.on("Command", oncommand)
  iotc.on("SettingsUpdated", onsettingsupdated)

  iotc.connect()
  try:
    while iotc.isConnected():
      iotc.doNext()
      if gCanSend == True: 
        if gCounter < 4:     
          dist = distance()
          print ("Measured Distance = %.1f cm" % dist)
          print("Sending telemetry.. %d" %gCounter)
          iotc.sendTelemetry("{ \
    \"ultrasonic\": " + str("%.1f" % dist) + "}")
          gCounter += 1
          for countdown in range (5,0,-1):
            print("next data in %d" %countdown)
            time.sleep(1)
          

        else:
          break      

# Reset by pressing CTRL + C
  except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()