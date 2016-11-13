#Author James Inglis
# provide functions for reading analog and digital values from the PI

from datetime import datetime
# Import config file and parser
import configparser
config = None
# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SP
import Adafruit_MCP3008
# Import GPIO library
import RPI.GPIO as GPIO


# Software SPI configuration:
CLK  = 0
MISO = 0
MOSI = 0
CS   = 0
mcp = None

# DigitalInput configuration
pinsUsed = None
digitalPoints = None


def ConfigureCollector()
	#Parse config file
	config = configparser.ConfigParser()
	config.read('Config.ini')
	return;

def InitializeAnalogInput()
	if config == None:
		ConfigureCollector()
	# Software SPI configuration:
	CLK  = config.get('SPI', 'CLK')
	MISO = config.get('SPI', 'MISO')
	MOSI = config.get('SPI', 'MOSI')
	CS   = config.get('SPI', 'CS')
	mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
	return;

def InitializeDigitalInput()
	if config == None:
		ConfigureCollector()
	GPIO.setmode(GPIO.BCM)

	pinsUsed = config.get('GPIO', 'pinsUsed')
	digitalPoints = None
	current = 'pin0'
	for x in range(pinsUsed):
		current = 'pin'+ x
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
