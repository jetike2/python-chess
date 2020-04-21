import pygame


class Piece(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("assets/white_pwn.png")

        self.rect = self.image.get_rect()

        
    def draw(self,window,board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "wp":
                    self.image = pygame.image.load("assets/white_pwn.png")
                    self.rect.x = j * 100
                    self.rect.y = i * 75

                if board[i][j] == "bp":
                    self.image = pygame.image.load("assets/black_pwn.png")
                    self.rect.x = j * 100
                    self.rect.y = i * 75

                if board[i][j] == "br":
                    self.image = pygame.image.load("assets/black_rook.png")
                    self.rect.x = j * 100
                    self.rect.y = i * 75

                if board[i][j] == "wr":
                    self.image = pygame.image.load("assets/white_rook.png")
                    self.rect.x = j * 100
                    self.rect.y = i * 75


                if board[i][j] == "bk":
                    self.image = pygame.image.load("assets/black_knight.png")
                    self.rect.x = j * 100
                    self.rect.y = i * 75

                if board[i][j] == "wk":
                    self.image = pygame.image.load("assets/white_knight.png")
                    self.rect.x = j * 100
                    self.rect.y = i * 75

                if board[i][j] == "bb":
                    self.image = pygame.image.load("assets/black_bishop.png")
                    self.rect.x = j * 100
                    self.rect.y = i * 75

                if board[i][j] == "wb":
                    self.image = pygame.image.load("assets/white_bishop.png")
                    self.rect.x = j * 100
                    self.rect.y = i * 75

                if board[i][j] == "bq":
                    self.image = pygame.image.load("assets/black_queen.png")
                    self.rect.x = j * 100
                    self.rect.y = i * 75

                if board[i][j] == "wq":
                    self.image = pygame.image.load("assets/white_queen.png")
                    self.rect.x = j * 100
                    self.rect.y = i * 75

                if board[i][j] == "bK":
                    self.image = pygame.image.load("assets/black_king.png")
                    self.rect.x = j * 100
                    self.rect.y = i * 75

                if board[i][j] == "wK":
                    self.image = pygame.image.load("assets/white_king.png")
                    self.rect.x = j * 100
                    self.rect.y = i * 75

                window.blit(self.image, (self.rect.x,self.rect.y))

    def is_valid_move(self, celltype, cellx, celly):
        pass

