# here our mission - chessmess.py

import pygame as mf
import chessgotbrain
diamention_of_chess = 8
H = L = 500
SQ_BOZ = H // diamention_of_chess 
Img = {}

fps = 50

def peiceimagie():
    pz = ["p","r","n","b","q","k","P","R","N","B","Q","K"]
    for sex in pz :
        Img[sex] = mf.transform.scale(mf.image.load("images/" + sex + ".bmp") ,(SQ_BOZ ,SQ_BOZ))


def gz():
    mf.init()
    hamariscreen = mf.display.set_mode((L , H))
    clock = mf.time.Clock()
    timeisout = mf.time.Clock()
    hexfel = chessgotbrain.gamestarttt()
    peiceimagie()
    hamariscreen.fill(mf.Color("white"))
    running = True
    while running:
        for f in mf.event.get():
            if f.type == mf.quit:
                running = False
        draw_the_game(hamariscreen ,hexfel)
        clock.tick(fps)
        mf.display.flip()


'''

draw the square on baord and all graphics

'''
def draw_the_game(hamariscreen ,hexfel):
    drawboard(hamariscreen)
    draw_the_fucking_peices(hamariscreen , hexfel.board)

def drawboard(hamariscreen):
    colourrss = [mf.Color("white"), mf.Color("orange")]

    for x in range(diamention_of_chess):
        for y in range(diamention_of_chess):

            color = colourrss[(x + y) % 2]

            mf.draw.rect(
                hamariscreen,
                color,
                (x * SQ_BOZ, y * SQ_BOZ, SQ_BOZ, SQ_BOZ)
            )

def draw_the_fucking_peices(hamariscreen , board):
    for r in range(diamention_of_chess):
        for c in range(diamention_of_chess):
            peices = board[r][c]
            if peices !=  " ":
                hamariscreen.blit(Img[peices] , mf.Rect(c * SQ_BOZ, r * SQ_BOZ, SQ_BOZ, SQ_BOZ) )

        


if __name__ == "__main__":
    gz()








