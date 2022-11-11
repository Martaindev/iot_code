import time
import RPi.GPIO as GPIO
import telepot
import telepot.loop as MessageLoop

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

blue = 7
red = 11
yellow = 13

GPIO.setup(blue,GPIO.OUT)
GPIO.output(blue,0)

GPIO.setup(yellow,GPIO.OUT)
GPIO.output(yellow,0)

GPIO.setup(red,GPIO.OUT)
GPIO.output(red,0)

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Received: %s' %command)

    if 'on' in command:
        message = 'on'
        if 'blue' in command:
            message = message  + " blue"
            GPIO.output(blue,1)

        if 'yellow' in command:
            message = message  + " yellow"
            GPIO.output(yellow,1)

        if 'red' in command:
            message = message  + " red"
            GPIO.output(red,1)

        if 'all' in command:
            message = message + " all"
            GPIO.output(blue,1)
            GPIO.output(yellow,1)
            GPIO.output(red,1)
        message = message + " lights"
        telegram_bot.sendMessage(chat_id,message)

    if 'off' in command:
        message = 'off'
        if 'blue' in command:
            message = message + ' blue'
            GPIO.output(blue,0)
        
        if 'yellow' in command:
            message = message + " yellow"
            GPIO.output(yellow,0)
        
        if 'red' in command:
            message = message + " red"
            GPIO.output(red,0)

        if 'all' in command:
            message = message + " all"
            GPIO.output(blue,0)
            GPIO.output(yellow,0)
            GPIO.output(red,0)
        message = message + " lights"
        telegram_bot.sendMessage(chat_id,message)

telegram_bot = telepot.Bot("")
print(telegram_bot.getMe())

MessageLoop(telegram_bot,action).run_as_thread()
print("Up and Running....")

while 1:
    time.sleep(1)

             

