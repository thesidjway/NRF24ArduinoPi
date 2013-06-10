python-nrf24
============

python-lib for interfacing with nRF24L01 modules

Introduction
------------
The library is to be used with python2.

Requirements
------------
 * For SPI communication py-spidev: https://github.com/doceme/py-spidev.git
 * For GPIO WiringPi2-Python: https://github.com/Gadgetoid/WiringPi2-Python.git

Example
-------
For a sender:

	from nrf24 import Nrf24
	nrf = Nrf24(cePin=2,csnPin=3,channel=10,payload=8)
	nrf.config()
	nrf.setRADDR("host1")
	nrf.setTADDR("host2")
  
	if not nrf.isSending():
		nrf.send(map(ord,"Hello"))
		
For a receiver:

	from nrf24 import Nrf24
	nrf = Nrf24(cePin=2,csnPin=3,channel=10,payload=8)
	nrf.config()
	nrf.setRADDR("host2")
	nrf.setTADDR("host1")
  
	while True:
		if nrf.dataReady():
			print nrf.getData()
			break

	
  
  
  





