## README LED Web Server

#### Authors: flourtowel & ndunkel 

## Getting Started

* ### Raspberry Pi 

	* We used a Raspberry Pi 2 Model B 
	
	* [noobs setup](https://www.raspberrypi.org/help/noobs-setup/)

	* [updates](https://www.raspberrypi.org/documentation/raspbian/updating.md)	

* ### Python GPIO Library

	* This project uses Python 2.7

	* [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO)

* ### Flask
	
	* [http://flask.pocoo.org/](http://flask.pocoo.org/)
	
	* [flask quickstart](http://flask.pocoo.org/docs/0.10/quickstart/#quickstart) 


* ### Breadboard

	* Breadboard
	* LEDs (We used Red, Yellow, Green)
	* Resistors (220 Ohms)
	* Female to Male wires to go from GPIO to breadboard

<center>![](http://i.imgur.com/DufTMVQ.jpg)</center>

There are two different versions to get pin numbers and you have to specify which one you're using. Below are pictures of the two ways you can use. [Click here for more information](http://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering)

![](http://i.imgur.com/Z3MHgui.png)

![](http://i.imgur.com/dmkVV0R.png)


## Execution Instructions

### Download Github repository

* Run the command from the terminal in your workspace:

	*  `git clone https://github.com/flourtowel/LED-Web-Server.git`

* To run the Web Server do the following commands:

	* `cd LED-Web-Server`

	* `sudo python LED_Webserver.py` 

* Then from a different host (can be a laptop, desktop or phone) open a browser and in the address bar type:
	
	* `http://192.168.1.10:5000` Note: You should run the `ifconfig` command in the terminal and use the correct IP Address for your Raspberry Pi in your local network. 

The we ran the web server in the terminal:

<center>![](http://i.imgur.com/exqjwHM.png)</center>

The IP address below is the phone connecting to the web server:

<center>![](http://i.imgur.com/MBeUbx7.png)</center>

This is what the web server interface looks like on an iPhone:

<center>![](http://i.imgur.com/A3HVPD1.jpg)</center>

When you push the buttons on the phone you get the following messages in the terminal:

<center>![](http://i.imgur.com/kCiEItw.png)</center>

And the changes take place on the LEDs.

<center>![](http://i.imgur.com/aV17fqO.jpg)</center>
