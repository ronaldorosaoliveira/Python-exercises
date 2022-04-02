# faça um programa em Pytho que abra e reproduza o áudio de um arquivo MP3

from pygame import mixer
mixer.init()
mixer.music.load('021.mp3')
mixer.music.play(-1)
input('Agora você escuta?')

# mixer.music.play(-1) faz a música repetir infinitamente
