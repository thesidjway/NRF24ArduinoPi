from nrf24 import Nrf24
import time
nrf = Nrf24(cePin=2,csnPin=3,channel=10,payload=8)
nrf.config()
nrf.setTADDR("clie1")
while 1>0:
	if not nrf.isSending():
    		nrf.send(map(ord,"aaaa"))
		time.sleep(1)
		nrf.send(map(ord,"bbbb"))
		time.sleep(1)
		nrf.send(map(ord,"cccc"))
		time.sleep(1)
