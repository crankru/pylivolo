import wiringpi as wpi

class Livolo:
    def __init__(self, pinNumber, debug=False, repeats=150, p_short=110, p_long=300, p_start=520):
        self.debug = debug
        self.repeats = repeats
        self.p_short = p_short # 110 works quite OK
        self.p_long = p_long # 300 works quite OK
        self.p_start = p_start # 520 works quite OK
        self.high = True
        self.pinNumber = pinNumber
        
        self.debugMsg('Pin: {}'.format(self.pinNumber))
		
		# wpi.setup('wpi')
        wpi.wiringPiSetup()
        wpi.pinMode(self.pinNumber, wpi.OUTPUT) 

    def sendButton(self, remoteID, keycode):
        self.debugMsg("sendButton: remoteID: {} keycode {}".format(remoteID, keycode))

        for pulse in range(self.repeats):
			
            self.sendPulse(1) # Start  
            self.high = True # first pulse is always high

			# transmit remoteID
			# for i = 15; i >= 0; i--
            for i in reversed(range(15)):
				txPulse = remoteID & (1 << i) # read bits from remote ID
				if txPulse > 0:
					self.selectPulse(1)
				else:
					self.selectPulse(0)

			# XXX transmit keycode
			# for (i = 6; i >= 0; i--)
            for i in reversed(range(6)):
				txPulse = keycode & (1 << i) # read bits from keycode
				if txPulse > 0:
					self.selectPulse(1)
				else:
					self.selectPulse(0)
  
        wpi.digitalWrite(self.pinNumber, wpi.LOW)

    def selectPulse(self, inBit):			
		# if current pulse should be high, send High Zero
		if inBit == 0: 
			if self.high == True:
				self.sendPulse(2)
				self.sendPulse(4)
			else:
				self.sendPulse(4) # else send Low Zero
				self.sendPulse(2)

		# if current pulse should be high, send High One
		elif inBit == 1: 
			if self.high == True:
				self.sendPulse(3)
			else:
				self.sendPulse(5) # else send Low One
				
			self.high = not self.high # invert next pulse

    # transmit pulse
    def sendPulse(self, txPulse):
		
		if txPulse == 0: # Start
			wpi.digitalWrite(self.pinNumber, wpi.LOW)
			wpi.delayMicroseconds(self.p_start); # 550
		   
		elif txPulse == 1: # Start
			wpi.digitalWrite(self.pinNumber, wpi.HIGH)
			wpi.delayMicroseconds(self.p_start); # 550

		elif txPulse == 2: # "High Zero"
			wpi.digitalWrite(self.pinNumber, wpi.LOW)
			wpi.delayMicroseconds(self.p_short) # 110
		 
		elif txPulse == 3: # "High One"
			wpi.digitalWrite(self.pinNumber, wpi.LOW)
			wpi.delayMicroseconds(self.p_long) # 303

		elif txPulse == 4: # "Low Zero"
			wpi.digitalWrite(self.pinNumber, wpi.HIGH)
			wpi.delayMicroseconds(self.p_short) # 110

		elif txPulse == 5:	# "Low One"
			wpi.digitalWrite(self.pinNumber, wpi.HIGH)
			wpi.delayMicroseconds(self.p_long) # 290

    def debugMsg(self, msg):
		if self.debug == True:
			print(msg)