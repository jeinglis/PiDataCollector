import DataCollector
import time

DataCollector.ConfigureCollector()
DataCollector.InitializeAnalogInput()
DataCollector.InitializeDigitalInput()

#create file if it doesn't exist if it does append the file
output = open('output.csv', 'a+')

while True:
	temp = DataCollector.PollAnalog(0)
	value = ('analog_0', temp[0], temp[1])
	s = str(value)
	output.write(s)

	temp = DataCollector.PollAnalog(1)
	value = ('analog_0', temp[0], temp[1])
	s = str(value)
	output.write(s)

	time.sleep(0.5)

