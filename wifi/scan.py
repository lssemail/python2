import pywifi
import time

def scan(sleeptime):
    wifi = pywifi.PyWiFi()

    iface = wifi.interfaces()[0]

    iface.scan()
    time.sleep(sleeptime)

    return iface.scan_results()

results = scan(10)
for r in results:
    print(r.ssid)