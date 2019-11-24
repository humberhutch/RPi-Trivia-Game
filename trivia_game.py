# August 2019 - Toronto Picademy
# Grant Hutchison and others
# This trivia game uses the Explorer hat as an input device to answer trivia
# questions. The questions will appear on the screen and the player will 
# indicate their response using the Explorer Hat buttons. A buzzer should 
# be attached to pin 18 to provide audible feedback. The correct answer will
# be displayed on the keypad and the tone will change if the answer is correct
# on incorrect.

import explorerhat as eh
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from guizero import App, Box, PushButton, Text

import time
qnum=0
questions = ["What is the capital of Ontario?","In what year did the Toronto Raptors win the NBA Title?","Who was Laura Secord?"]
answers = [["Ottawa","Toronto","Moosejaw","Windsor"],["1995","2015","2019","2000"],["Chocolate","Prime Minister","Laura Who?","Heroine of 1812"]]
correct_answers = [1,2,3]
b = TonalBuzzer(18)

def playTone(freq):
    b.play(maxToneTone(freq))
    time.sleep(4) 
    b.stop()
    
def getButton(channel, event):
    global qnum,correct_answers,b
    print ("Got {} on {}".format(event,channel))
    eh.light.off()
    if correct_answers[qnum] ==0:
        eh.light.blue.on()
    elif correct_answers[qnum] ==1:
        eh.light.yellow.on()
    elif correct_answers[qnum] ==2:
        eh.light.red.on()
    else:
        eh.light.green.on()
    
    if (channel-1)==correct_answers[qnum] and event=="press":
        b.play(Tone.from_frequency(880))
        time.sleep(1)
    else:
        b.play(Tone.from_frequency(220))
        time.sleep(1)
        b.stop()
        time.sleep(1)
        b.play(Tone.from_frequency(220))
    b.stop()

def game(): 
    global app, questions,answers, correct_answers,qnum,questionText,btn1,btn2,btn3,btn4,nextBtn
    eh.light.on()
    questionText = Text(app, questions[qnum])
    questionText.text_size = 40
    buttons_box = Box(app, width="fill", align="top")
    btn1 = PushButton(buttons_box, text=answers[qnum][0], align="left")
    btn1.bg = "blue"
    btn1.text_color="white"
    btn1.text_size = 40
    
    btn2 = PushButton(buttons_box, text=answers[qnum][1], align="left")
    btn2.bg = (209,182,16)
    btn2.text_color="white"
    btn2.text_size = 40
    
    btn3 = PushButton(buttons_box, text=answers[qnum][2], align="left")
    btn3.bg = "red"
    btn3.text_color="white"
    btn3.text_size = 40
    
    btn4 = PushButton(buttons_box, text=answers[qnum][3], align="left")
    btn4.bg = "green"
    btn4.text_color="white"
    btn4.text_size = 40

    nextBtn = PushButton(app, command=nextQ, text="Next", align="left")    
    
def nextQ():
    global questionText,btn1,btn2,btn3,btn4,nextBtn,qnum
    questionText.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    nextBtn.destroy()
    qnum+=1
    game()


# register the event handlers for the buttons
eh.touch.one.pressed(getButton)
eh.touch.two.pressed(getButton)
eh.touch.three.pressed(getButton)
eh.touch.four.pressed(getButton)

app = App()
game()
app.display()