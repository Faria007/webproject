# -*- coding: utf-8 -*-


from pygame import mixer
mixer.init()
mixer.music.load("shayad.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()
while 'true' :
    print("press 'p' to pause,'r' to resume")
    print("press 'e' to exit the program")
    query=input(" ")
    
    if query == 'p':
        mixer.music.pause()
        
    elif query == 'r':
        mixer.music.unpause()
     
    elif query=='e':
        mixer.music.stop()
        break