import board, digitalio, pulseio

BRAKEVCC = 0
CW = 1
CCW = 2
BRAKEGND = 3

# VNH2SP30 pin definitions
# xxx[0] controls '1' outputs
# xxx[1] controls '2' outputs
inApin = [digitalio.DigitalInOut(board.D7), digitalio.DigitalInOut(board.D4)]   # INA: Clockwise input
inBpin = [digitalio.DigitalInOut(board.D8), digitalio.DigitalInOut(board.D9)]   # INB: Counter-clockwise input
pwmpin = [pulseio.PWMOut(board.D5, frequency = 500, duty_cycle = 0), pulseio.PWMOut(board.D6, frequency = 500, duty_cycle = 0)]   # PWM input

# These pins are not used, but they were present in original library
#cspin = [2, 3]   # CS: Current sense ANALOG input
#enpin = [0, 1]   # EN: Status of switches output (Analog pin)

statpin = digitalio.DigitalInOut(board.D13)
statpin.direction = digitalio.Direction.OUTPUT

# Initialize digital pins as outputs
for i in range(2):
	inApin[i].direction = digitalio.Direction.OUTPUT
	inBpin[i].direction = digitalio.Direction.OUTPUT

# Initialize braked
for i in range(2):
	inApin[i].value = 0
	inBpin[i].value = 0

#void loop()
#{
#  motorGo(0, CW, 1023);
#  motorGo(1, CCW, 1023);
#  delay(500);
#
#  motorGo(0, CCW, 1023);
#  motorGo(1, CW, 1023);
#  delay(500);
#  
#  if ((analogRead(cspin[0]) < CS_THRESHOLD) && (analogRead(cspin[1]) < CS_THRESHOLD))
#    digitalWrite(statpin, HIGH);
#}

def motorOff(motor):
	# Initialize braked
	for i in range(2):
		inApin[i].value = 0
		inBpin[i].value = 0
	pwmpin[motor].duty_cycle = 0


# motorGo() will set a motor going in a specific direction
# the motor will continue going in that direction, at that speed
# until told to do otherwise.
 
# motor: this should be either 0 or 1, will selet which of the two
# motors to be controlled
 
# direct: Should be between 0 and 3, with the following result
# 0: Brake to VCC
# 1: Clockwise
# 2: CounterClockwise
# 3: Brake to GND
 
# pwm: should be a value between 0 and 65535, higher the number, the faster
# it'll go

def motorGo(motor, direct, pwm = 0):
	if motor <= 1:
		if direct <=4:
			# Set inA[motor]
			if direct <=1:
				inApin[motor].value = 1
			else:
				inApin[motor].value = 0
			# Set inB[motor]
			if (direct == 0) or (direct == 2):
				inBpin[motor].value = 1
			else:
				inBpin[motor].value = 0
	pwmpin[motor].duty_cycle = pwm
