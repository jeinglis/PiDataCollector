#Author James Inglis
# provide functions for reading analog and digital values from the PI

from datetime import datetime
# Import config file and parser
import configparser
config = configparser.ConfigParser()
config.read('Config.ini')

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SP
import Adafruit_MCP3008
# Import GPIO library
import RPi.GPIO as GPIO


# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# DigitalInput configuration
pinsUsed = int(float(config.get('GPIO', 'pinsUsed')))
digitalPoints = []


def ConfigureCollector():
	#Parse config file
	config = configparser.ConfigParser()
	config.read('Config.ini')
	return;

def InitializeAnalogInput():
	if config == None:
		ConfigureCollector()
	# Software SPI configuration:
	#CLK  = config['SPI']['CLK']
	#MISO = config['SPI']['MISO']
	#MOSI = config['SPI']['MOSI']
	#CS   = config['SPI']['CS']
	#CLK  = 18
        #MISO = 23
        #MOSI = 24
        #CS   = 25
	#mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
	return;

def InitializeDigitalInput():
	if config == None:
		ConfigureCollector()
	GPIO.setmode(GPIO.BCM)

	#pinsUsed = int(float(config.get('GPIO', 'pinsUsed')))
	
	digitalPoints = []
	current = 'pin0'
	for x in range(pinsUsed):
		current = 'pin'+ str(x)
		digitalPoints.append(config.get('GPIO', current))
		GPIO.setup(digitalPoints[x], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	return;

#return the value of the analog point connected to the mcp3008 pin (0-8)
def PollAnalog( pin ):
	value = [0, 0]
	value[0] = datetime.utcnow()
	value[1] = mcp.read_adc(pin)
	return value;
#return the value of the digital point connected to the pi GPIO pin
def PollDigital( pin ):
	if[pin] in digitalPoints:
		value = [0, 0]
		value[0] = datetime.utcnow()
		value[1] = GPIO.input(pin)
		return value;
	else:
		return None;
