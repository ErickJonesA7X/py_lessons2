import pygame
pygame.mixer.init()
pygame.mixer.music.load('NollieHeel.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()