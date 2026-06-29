from gpiozero import LED
import os
import matplotlib.pyplot as plt
import time

red = LED(17)

temps=[]
times=[]

plt.ion()

while True:

    temp=os.popen("vcgencmd measure_temp").readline()
    temperature=float(temp.replace("temp=","").replace("'C\n",""))

    temps.append(temperature)
    times.append(len(times))

    plt.clf()
    plt.plot(times,temps)
    plt.xlabel("Time")
    plt.ylabel("CPU Temperature")
    plt.title("CPU Temperature Monitor")
    plt.pause(0.1)

    if temperature>40:
        red.blink(on_time=1,off_time=1)
    else:
        red.off()

    time.sleep(1)
