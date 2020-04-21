import pygame
import sys
import board
import piece


SCREEN = pygame.display.set_mode((800, 600))


class GameApp:
    def __init__(self):
        pygame.init()
        self.board = [
                ["br", "bk", "bb", "bq", "bK", "bb", "bk", "br"],
                ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                ["wr", "wk", "wb", "wq", "wK", "wb", "wk", "wr"],
                ]
        self.selected = None

    def execute(self):
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    x = x // 100
                    y = y // 75 
                    cell_type = self.board[y][x] 
                    if self.selected == None and cell_type != 0:
                        self.selectedcell = (y, x)
                        self.selected = cell_type
                    elif self.selected != None:
                        self.board[y][x] = self.selected 
                        self.selected = None
                        self.board[self.selectedcell[0]][self.selectedcell[1]] = 0


            SCREEN.fill((0, 0, 0))
            board.BoardRenderer(SCREEN)
            piece.Piece.draw(piece.Piece(),SCREEN,self.board)
            pygame.display.flip()


if __name__=="__main__":
    game = GameApp()

    game.execute()
