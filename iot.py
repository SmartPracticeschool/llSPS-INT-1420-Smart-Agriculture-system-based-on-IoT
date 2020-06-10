## This is the received code need to read this (kb , its looks like auto light code , major changes are required)
import time
import sys
import ibmiotf.application # to install pip install ibmiotf
import ibmiotf.device

#Provide your IBM Watson Device Credentials
organization = "tm8dr6" #replace the ORG ID
deviceType = "command"#replace the Device type wi
deviceId = "3"#replace Device ID
authMethod = "token"
authToken = "9468351011" #Replace the authtoken

## working on this
def myCommandCallback(cmd): # function for Callback
        #print("Command received: %s" % cmd.data)
        ## made it with same lines to not get errors , code works now
        if cmd.data['command']=='lighton':
                print("Motor ON IS RECEIVED")

        elif cmd.data['command']=='lightoff':
                print("Motor OFF IS RECEIVED")

        if cmd.command == "setInterval":

                if 'interval' not in cmd.data:
                        print("Error - command is missing required information: 'interval'")
                else:
                        interval = cmd.data['interval']
        elif cmd.command == "print":
                if 'message' not in cmd.data:
                        print("Error - command is missing required information: 'message'")
                else:
                        output=cmd.data['message']
                        print(output)
##iot on desktop
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................

except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:

        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
