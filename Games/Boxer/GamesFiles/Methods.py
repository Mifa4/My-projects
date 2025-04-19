from Varibles import *
from Musics import Play
def Timer():
    global sec,minutes,hour, sec1, minutes1, hour1, sec2, sec3, minutes2, minutes3, hour2, hour3
    while True:
        sleep(1)
        if nl == 1:
            sec += 1
            if sec == 60:
                minutes += 1
                sec = 0
            if minutes == 60:
                hour += 1
                minutes = 0
            if hour == 24:
                sec,minutes,hour = 0,0,0
        elif nl == 2:
            sec1 += 1
            if sec1 == 60:
                minutes1 += 1
                sec1 = 0
            if minutes1 == 60:
                hour1 += 1
                minutes1 = 0
            if hour1 == 24:
                sec1,minutes1,hour1 = 0,0,0
        elif nl == 3:
            sec2 += 1
            if sec2 == 60:
                minutes2 += 1
                sec2 = 0
            if minutes2 == 60:
                hour2 += 1
                minutes2 = 0
            if hour2 == 24:
                sec2,minutes2,hour2 = 0,0,0
        else:
            sec3 += 1
            if sec3 == 60:
                minutes3 += 1
                sec3 = 0
            if minutes3 == 60:
                hour3 += 1
                minutes3 = 0
            if hour3== 24:
                sec3,minutes3,hour3 = 0,0,0
time = Thread(target=Timer)
time.start()

def PlayerMouve():
    global l3_rgb,l2_rgb,l1_rgb,l4_rgb
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        yPos -= 5
        if yPos <= 0:
            if nl == 3:
                nl = 1
                l3_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b3 += 1
                yPos = hl1 - playerH
            elif nl == 2:
                nl = 4
                l2_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b2 += 1
                yPos = hl1 - playerH
            elif nl == 1:
                nl = 3
                l1_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b1 += 1
                yPos = hl1 - playerH
            elif nl == 4:
                nl = 2
                l4_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b4 += 1
                yPos = hl1 - playerH
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        yPos += 5
        if yPos + playerH >= hl1:
            if nl == 4:
                nl = 2
                l4_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b4 += 1
            elif nl == 1:
                nl = 3
                l1_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b1 += 1
            elif nl == 2:
                nl = 4
                l2_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b2 += 1
            elif nl == 3:
                nl = 1
                l3_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b3 += 1
            yPos = 0

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        xPos -= 5
        if xPos <= 0:
            if nl == 2:
                nl = 1
                l2_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b2 += 1
                xPos = wl1 - playerW
            elif nl == 4:
                nl = 3
                l4_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b4 += 1
                xPos = wl1 - playerW
            elif nl == 3:
                nl = 4
                l3_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b3 += 1
                xPos = wl1 - playerW
            elif nl == 1:
                nl = 2
                l1_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b1 += 1
                xPos = wl1 - playerW
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        xPos += 5
        if xPos + playerW >= wl1:
            if nl == 4:
                nl = 3
                l4_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b4 += 1
            elif nl == 2:
                nl = 1
                l2_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b2 += 1
            elif nl == 1:
                nl = 2
                l1_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b1 += 1
            elif nl == 3:
                nl = 4
                l3_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b3 += 1
            xPos = 0

def SecretCodes():
    global l1_rgb,l2_rgb,l3_rgb,l4_rgb
    if keys[pygame.K_q] and keys[pygame.K_SPACE]:
        l1_rgb = [255,0,0]
        l2_rgb = [255,0,0]
        l3_rgb = [255,0,0]
        l4_rgb = [255,0,0]
    if keys[pygame.K_b] and keys[pygame.K_f]:
        Play('')

def Displaying():
    win.fill((255,255,255))
    win.blit(l1,(0,0))
    win.blit(l2,(w // 2,0))
    win.blit(l3,(0,h // 2))
    win.blit(l4,(w // 2,h // 2))
    l1.fill((l1_rgb[0],l1_rgb[1],l1_rgb[2]))
    l2.fill((l2_rgb[0],l2_rgb[1],l2_rgb[2]))
    l3.fill((l3_rgb[0],l3_rgb[1],l3_rgb[2]))
    l4.fill((l4_rgb[0],l4_rgb[1],l4_rgb[2]))