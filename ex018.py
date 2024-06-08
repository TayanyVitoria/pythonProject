from pygame import mixer
mixer.init()
mixer.music.load('ex018.mp3')
mixer.music.play()
x = input('Digite algo para parar...')
