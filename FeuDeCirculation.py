import RPi.GPIO as GPIO
import time

ledRougePin = 11    # define ledPin
ledVertPin  = 13
ledJaunePin = 15
def setup():
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    GPIO.setup(ledRougePin, GPIO.OUT) # set the ledPin to OUTPUT mode
    GPIO.setup(ledVertPin, GPIO.OUT)
    GPIO.setup(ledJaunePin, GPIO.OUT)
    GPIO.output(ledRougePin, GPIO.LOW)  # make ledPin output LOW level
    GPIO.output(ledVertPin,  GPIO.LOW)
    GPIO.output(ledJaunePin, GPIO.LOW)

    print ('using pin%d'%ledRougePin)
    print ('using pin%d'%ledVertPin)
    print ('using pin%d'%ledJaunePin)
def loop():
    while True:
        GPIO.output(ledRougePin, GPIO.HIGH)  # make ledPin output HIGH level to turn on led
        print ('led rouge turned on >>>')     # print information on terminal
        time.sleep(1)                   # Wait for 1 second
        GPIO.output(ledRougePin, GPIO.LOW)   # make ledPin output LOW level to turn off led
        GPIO.output(ledJaunePin, GPIO.HIGH)
        print ('led vert turned on <<<')
        time.sleep(1)
        GPIO.output(ledJaunePin, GPIO.LOW)
        GPIO.output(ledVertPin, GPIO.HIGH)
        print('led jaune turned on <<<')
        time.sleep(1)
        GPIO.output(ledVertPin, GPIO.LOW)
def destroy():
    GPIO.cleanup()                      # Release all GPIO

if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()