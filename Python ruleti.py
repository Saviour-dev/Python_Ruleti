import random
import time
import os
import pygame

pygame.init()

sound_file1 = "C:\\Users\\OYUNCU\\Downloads\\sounds\\Boş silah.mp3"
sound_file2 = "C:\\Users\\OYUNCU\\Downloads\\sounds\\Ateşlenen silah (mp3cut.net).mp3"
sound_file3 = "C:\\Users\\OYUNCU\\Downloads\\sounds\\Yere düşen kovan (mp3cut.net).mp3"
sound_file4 = "C:\\Users\\OYUNCU\\Downloads\\sounds\\Revolver mermi doldurma.mp3"

sound1 = pygame.mixer.Sound(sound_file1)
sound2 = pygame.mixer.Sound(sound_file2)
sound3 = pygame.mixer.Sound(sound_file3)
sound4 = pygame.mixer.Sound(sound_file4)

sound4.play()
num = random.randint(1, 6)

print("Bu Bir Rulet Oyunudur. Dolu Kovanı seçerseniz ölürsünüz...")

time.sleep(3)

while True:
    if num == int(input("1 ile 6 arasında bir sayı giriniz: ")) and num == num:
        sound2.play()
        time.sleep(1)
        sound3.play()
        time.sleep(2)
        print("Dolu Kovanı seçtiniz. Bilgisayarınız kapanıyor...")
        time.sleep(5)
        os.system("shutdown -s -t 1")
        break
    else:
        sound1.play()
        time.sleep(1)
        print("Tebrikler! Dolu Kovanı seçmediniz.")