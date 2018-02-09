import network
import ubinascii
import machine
import time
import socket

IF_STA = network.WLAN(network.STA_IF)
power = machine.Pin(16, machine.Pin.OUT)
status = machine.Pin( 2, machine.Pin.OUT)

def try_internet():
	addr = socket.getaddrinfo("ipinfo.io", 80)[0][-1]
	try:
		s = socket.socket()
		s.connect(addr)
	except:
		return "No Internet"
	try:
		s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % ("ip", "ipinfo.io"), 'utf-8'))
		d = ""
		start_time = time.time()
		while True:
			data = s.recv(1024).decode()
			if data:
    				d += str(data)
			end_time = time.time()
			if end_time - start_time > 2:
				break
		if "Connection: close" in d:
			return "Captive Portal"
		else:
			ip = d.split("Via: 1.1 google")[1].strip()
			return "Internet Access: "+ip
	except:
		pass
	try:
		s.close()
	except:
		pass

def scan():
	status.on()
	f = open("ssid","a")
	f.write("")
	f.close()
	IF_STA.active(True)
	for ap in IF_STA.scan():
        	ssid, bssid, channel, RSSI, authmode, hidden = ap
       		bssid = ubinascii.hexlify(bssid)
		if authmode == 0:
			modus="OPEN"
		elif authmode==1:
			modus=="WEP"
		elif authmode==2:
			modus="WPA-PSK"
		elif authmode==3:
			modus="WPA2-PSK"
		elif authmode==4:
			modus="WPA/WPA2-PSK"
		else:
			modus="AUTH="+str(authmode)
		g = open("ssid","r")
		s = g.read()
		g.close()
		if str(bssid.decode()) not in s:
			status.on()
			if authmode==0:
				IF_STA.connect(ssid.decode())
				ip,nm,gw,dns = IF_STA.ifconfig()
				while ip=="0.0.0.0":
					time.sleep(0.5)
					ip,nm,gw,dns = IF_STA.ifconfig()
				status.off()
				internet_status = try_internet()
				f = open("ssid","a")
				f.write(str(bssid.decode())+" - "+str(ssid.decode())+" - "+modus+" - "+ip+" / "+dns+" - "+internet_status+"\n")
				f.close()
				IF_STA.disconnect()
				break
			else:
				f = open("ssid","a")
				f.write(str(bssid.decode())+" - "+str(ssid.decode())+" - "+modus+"\n")
				f.close()

power.off()
while 1:
    scan()
