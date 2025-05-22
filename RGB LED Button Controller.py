import RPi.GPIO as GPIO
from time import sleep

r=37
g=35
b=12

rbutton=11
gbutton=13
bbutton=15

GPIO.setmode(GPIO.BOARD)

GPIO.setup(r,GPIO.OUT)
GPIO.setup(g,GPIO.OUT)
GPIO.setup(b,GPIO.OUT)

GPIO.setup(rbutton,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(gbutton,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(bbutton,GPIO.IN,pull_up_down=GPIO.PUD_UP)

rLEDstate=False
rbuttonstateold=GPIO.HIGH
gbuttonstateold=GPIO.HIGH
bbuttonstateold=GPIO.HIGH

bpwm=GPIO.PWM(b,100)
bpwm.start(0)
index=0
bright=[0,25,50,75,100]

try:
        while True:
                rbuttonstate=GPIO.input(rbutton)
                if rbuttonstate==GPIO.LOW and rbuttonstateold==GPIO.HIGH:
                        rLEDstate= not rLEDstate
                        GPIO.output(r,rLEDstate)
                        rbuttonstate=rbuttonstateold
                        sleep(0.3)

                gbuttonstate=GPIO.input(gbutton)
                if gbuttonstate==GPIO.LOW:
                        GPIO.output(g, not GPIO.input(g))
                        sleep(0.5)
                else:
                        GPIO.output(g,GPIO.LOW)

                bbuttonstate=GPIO.input(bbutton)
                if bbuttonstate==GPIO.LOW and bbuttonstateold==GPIO.HIGH:
                        index=(index+1)%len(bright)
                        bpwm.ChangeDutyCycle(bright[index])
                        print(bright[index])
                        sleep(0.3)
                rbuttonstate=rbuttonstateold
                gbuttonstate=gbuttonstateold
                bbuttonstate=bbuttonstateold
                sleep(0.1)
except KeyboardInterrupt:
        bpwm.stop()
        GPIO.cleanup()
        print('finish')
