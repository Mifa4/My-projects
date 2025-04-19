from Varibles import *
import Varibles

def TextRender():
    l1 = Varibles.l1
    l2 = Varibles.l2
    l3 = Varibles.l3
    l4 = Varibles.l4
    l1_rgb = Varibles.l1_rgb
    l2_rgb = Varibles.l2_rgb
    l3_rgb = Varibles.l3_rgb
    l4_rgb = Varibles.l4_rgb
    wl1 = Varibles.wl1
    wl2 = Varibles.wl2
    wl3 = Varibles.wl3
    wl4 = Varibles.wl4
    sec = Varibles.sec
    minutes = Varibles.minutes
    hour = Varibles.hour
    sec1 = Varibles.sec1
    minutes1 = Varibles.minutes1
    hour1 = Varibles.hour1
    sec2 = Varibles.sec2
    sec3 = Varibles.sec3
    minutes2 = Varibles.minutes2
    minutes3 = Varibles.minutes3
    hour2 = Varibles.hour2
    hour3 = Varibles.hour3
    b1 = Varibles.b1
    b2 = Varibles.b2
    b3 = Varibles.b3
    b4 = Varibles.b4
    L1Text = Font1.render(f'Биом{b1}',True,(255 - l1_rgb[0],255 - l1_rgb[1],255 - l1_rgb[2]))
    L2Text = Font1.render(f'Биом{b2}',True,(255 - l2_rgb[0],255 - l2_rgb[1],255 - l2_rgb[2]))
    L3Text = Font1.render(f'Биом{b3}',True,(255 - l3_rgb[0],255 - l3_rgb[1],255 - l3_rgb[2]))
    L4Text = Font1.render(f'Биом{b4}',True,(255 - l4_rgb[0],255 - l4_rgb[1],255 - l4_rgb[2]))
    time_text = f'{hour}:{minutes}:{sec}'
    time_text1 = f'{hour1}:{minutes1}:{sec1}'
    time_text2 = f'{hour2}:{minutes2}:{sec2}'
    time_text3 = f'{hour3}:{minutes3}:{sec3}'
    text_of_time = Font2.render(time_text,True,(255 - l1_rgb[0],255 - l1_rgb[1],255 -l1_rgb[2]))
    text_of_time2 = Font2.render(time_text1,True,(255 - l2_rgb[0],255 - l2_rgb[1],255 -l2_rgb[2]))
    text_of_time3 = Font2.render(time_text2,True,(255 - l3_rgb[0],255 - l3_rgb[1],255 -l3_rgb[2]))
    text_of_time4 = Font2.render(time_text3,True,(255 - l4_rgb[0],255 - l4_rgb[1],255 -l4_rgb[2]))
    l1.blit(L1Text,(wl1 // 2 - L1Text.get_width() // 2,hl1 // 2 - L1Text.get_height() // 2))
    l2.blit(L2Text,(wl2 // 2 - L2Text.get_width() // 2,hl2 // 2 - L2Text.get_height() // 2))
    l3.blit(L3Text,(wl3 // 2 - L3Text.get_width() // 2,hl3 // 2 - L3Text.get_height() // 2))
    l4.blit(L4Text,(wl4 // 2 - L4Text.get_width() // 2,hl4 // 2 - L4Text.get_height() // 2))
    l1.blit(text_of_time,(wl1 // 2 - text_of_time.get_width() // 2,0))
    l2.blit(text_of_time2,(wl2 // 2 - text_of_time2.get_width() // 2,0))
    l3.blit(text_of_time3,(wl3 // 2 - text_of_time3.get_width() // 2,0))
    l4.blit(text_of_time4,(wl4 // 2 - text_of_time4.get_width() // 2,0))