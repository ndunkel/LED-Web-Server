# @ LED_Webserver.py
# @ See LED_Form.html
# A webserver to control LED lights on a bread board using Flask and GPIO
# Mobile friendly :)
# @authors Jon Bjerke <jon-bjerke@uiowa.edu>
#	   Natasha Dunkel <natasha-dunkel@uiowa.edu>
#

from flask import Flask, render_template , request

import RPi.GPIO as GPIO					# Imports GPIO from RPi

GPIO.setmode(GPIO.BOARD)				# Setup Pin Count to be natural
GPIO.setup(29 , GPIO.OUT) 				# Setup Pin 29 as an output
p_Green = GPIO.PWM(29, 50)				# Set Pin 29 to p_Green at frequency of 50 Hz (Green LED used)
GPIO.setup(31 , GPIO.OUT)				# Setup Pin 31 as an output
p_Yellow = GPIO.PWM(31, 50)				# Set Pin 31 to p_Yellow at frequency of 50 Hz (Yellow LED used)
GPIO.setup(33, GPIO.OUT)				# Setup Pin 33 as an output 
p_Red = GPIO.PWM(33, 50)				# Set Pin 33 to p_Red at frequency of 50 Hz (Red LED used)

app = Flask(__name__)					# Set app to __name__

@app.route("/")                 
@app.route("/", methods=['POST'])  			

def lightItUp():					# Define function lightItUp		  
	if request.method == 'POST':  			# Looks for post request from site interface

		submitted_value = request.form['LEDstate']  # Submitted state request assigned to this variable
		
		if submitted_value =="Green On High":   #If request "Green On High", Green LED light turns on high
			p_Green.start(100)

		if submitted_value =="Green On Low":    #If request "Green On High", Green LED light turns on low
			p_Green.start(50)	
			
		if submitted_value =="Green Off":	#If request "Green On High", Green LED light turns off
			p_Green.stop()

		if submitted_value =="Yellow On High":	#If request "Yellow On High", Yellow LED light turns on high
			p_Yellow.start(100)	

		if submitted_value =="Yellow On Low":	#If request "Yellow On High", Yellow LED light turns on low
			p_Yellow.start(50)	
			
		if submitted_value =="Yellow Off":	#If request "Yellow On High", Yellow LED light turns on off
			p_Yellow.stop()

		if submitted_value =="Red On High":	#If request "Red On High", Red LED light turns on high
			p_Red.start(100)	

		if submitted_value =="Red On Low":	#If request "Red On High", Red LED light turns on low
			p_Red.start(50)

		if submitted_value =="Red Off":		#If request "Red On High", Red LED light turns on off.
			p_Red.stop()
		
		
		print "Button Requested: ", submitted_value  #Prints the button pressed to the terminal
       

	return render_template('LED_Form.html') 	#Renders the template for the html file
   
     
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=False)	#Runs application

GPIO.cleanup()