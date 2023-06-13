import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    koukaton = pg.image.load("ex01/fig/3.png")
    koukaton = pg.transform.flip(koukaton,True,False)
    koukaton_1 = pg.transform.rotozoom(koukaton, 10, 1.0)
    koukaton_list = [koukaton,koukaton_1]
    tmr = 0
    x = 0
    xx = 0
    w = 0
    j = 1
    oo = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(bg_img, [-x, 0])
        screen.blit(pg.transform.flip(bg_img,True,False),[1600-xx,0])
        i = tmr % 2
        koukaton_2 = pg.transform.rotozoom(koukaton, w, 1.0)
        screen.blit(koukaton_2,[300,200])
        pg.display.update()
        tmr += 1      
        x += 1
        xx += 1
        w += j
        if (x == 1601):
            x = -1600
        if (xx == 3201):
            xx = 0
        if (w >= 10):
            j = -1
        elif(w <= 0):
            j = 1

        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()