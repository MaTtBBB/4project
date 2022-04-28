from game import Game, Status
from PIL import Image, ImageDraw
from constants import *


class Shsss(Game):
    """
    !Обратите внимание! Функция get_status тут не переопределена, т.к. в классе родителе он есть.
    !Обратите внимание! Корректность хода может проверить только игра, т.к. программа отслеживает только ошибку,
    все остальные случаи не в его компетенции.
    """
    def __init__(self):     #параметры
        super().__init__()
        self.board = None
        self.win_cords = []

    def game_init(self) -> str:  #начальные параметры
        """
        Инициализация игры: создание поля, обнуление параметров.
        :return:
        str: Поле строкой.
        """
        self.win_cords = []
        self.board = [[0, 3, 0, 3, 0, 3, 0, 3], [3, 0, 3, 0, 3, 0, 3, 0], [0, 3, 0, 3, 0, 3, 0, 3], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [2, 0, 2, 0, 2, 0, 2, 0], [0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0]]
        self.status = Status.bot1_next  # ОБРАТИТЕ ВНИМАНИЕ! СТАТУС ТОЖЕ НАДО ОБНУЛЯТЬ!!!
        return self.get_board_string()

    def get_board_string(self) -> str:      #линия данных о доске
        if self.status == Status.bot1_next:
            self.board_string = 'x1'
        if self.status == Status.bot2_next:
            self.board_string = 'x2'
        for line in self.board:
            self.board_string += ' '.join([str(i) for i in line]) + '\n'
        return self.board_string[:-1]

    def bot_made_turn(self, turn: str) -> Status:  #ход
        """
        Изменение поля в зависимости от хода бота и изменение статуса.
        :param turn:
        Ход в виде строки. При написании бота берите хода формат отсюда.
        :return:
        Status: Статус игры.
        """
        try:
            x = int(turn.split()[0])
            y = int(turn.split()[1])
            xs = int(turn.split()[2])
            ys = int(turn.split()[3])
        except:  # Проверки на корректность хода
            if self.status == Status.bot1_next:
              self.status = Status.bot2_next
            else:
              self.status == Status.bot1_next
        if x not in [1, 2, 3, 4, 5, 6, 7, 8] or y not in [1, 2, 3, 4, 5, 6, 7, 8] or ys not in [1, 2, 3, 4, 5, 6, 7, 8] or xs not in [1, 2, 3, 4, 5, 6, 7, 8] or (self.board[ys - 1][xs - 1] != 2 and self.status == Status.bot1_next and self.board[ys-1][xs-1] != 4) or (self.board[ys - 1][xs - 1] != 3 and self.status == Status.bot2_next and self.board[ys-1][xs-1] != 5):
            if self.status == Status.bot1_next:
              self.status = Status.bot2_next
            else:
              self.status == Status.bot1_next
        if self.status == Status.bot1_next:
          if (self.board[ys-1][xs-1] == 2):
            if (y-ys == 1 and abs(x-xs) == 1 and self.board[y-1][x-1] < 2):
              self.board[ys-1][xs-1] = ys%2 + xs%2 - 1
              if(y == 8):
                self.board[y-1][x-1] = 4
              else:
                self.board[y-1][x-1] = 2
            elif(abs(y-ys) == 2 and abs(x-xs) == 2 and self.board[y-1][x-1] < 2 and (self.board[(y+ys)/2 - 1][(x+xs)/2 - 1] == 3 or self.board[(y+ys)/2 - 1][(x+xs)/2 - 1] == 5)):
              self.board[ys-1][xs-1] = ys%2 + xs%2 - 1
              if(y == 8):
                self.board[y-1][x-1] = 4
              else:
                self.board[y-1][x-1] = 2
              self.board[(y+ys)/2 - 1][(x+xs)/2 - 1] = ((y+ys)/2)%2 + ((x+xs)/2)%2 - 1
            else:
              if self.status == Status.bot1_next:
                self.status = Status.bot2_next
              else:
                self.status == Status.bot1_next
          elif(self.board[ys-1][xs-1] == 4):
            test = True
            for i in range(min(y - (y-ys)/abs(y-ys), ys)+1, max(y - (y-ys)/abs(y-ys), ys)):
              for j in range(min(x- (x-xs)/abs(x-xs), xs)+1, max(x- (x-xs)/abs(x-xs), xs)):
                if(self.board[i-1][j-1] > 1):
                  test = False
            if (abs(y-ys) == abs(x-xs) and self.board[y-1][x-1] < 2 and test):
              self.board[ys-1][xs-1] = ys%2 + xs%2 - 1
              self.board[y-1][x-1] = 4
            elif(abs(y-ys) == abs(x-xs) and (self.board[y - (y-ys)/abs(y-ys) -1][x - (x-xs)/abs(x-xs)-1] == 3 or self.board[y - (y-ys)/abs(y-ys) -1][x - (x-xs)/abs(x-xs)-1] == 5) and test and self.board[y - 1][x - 1] < 2):
              self.board[ys-1][xs-1] = ys%2 + xs%2 - 1
              self.board[y-1][x-1] = 4
              self.board[y - (y-ys)/abs(y-ys) -1][x - (x-xs)/abs(x-xs)-1] = (y - (y-ys)/abs(y-ys))%2 + (x - (x-xs)/abs(x-xs))%2 - 1
            else:
              if self.status == Status.bot1_next:
                self.status = Status.bot2_next
              else:
                self.status == Status.bot1_next
          else:
              if self.status == Status.bot1_next:
                self.status = Status.bot2_next
              else:
                self.status == Status.bot1_next
            self.board[y - 1][x - 1] = 1
        elif self.status == Status.bot2_next:
            if (self.board[ys-1][xs-1] == 3):
            if (y-ys == 1 and abs(x-xs) == 1 and self.board[y-1][x-1] < 2):
              self.board[ys-1][xs-1] = ys%2 + xs%2 - 1
              if(y == 1):
                self.board[y-1][x-1] = 5
              else:
                self.board[y-1][x-1] = 3
            elif(abs(y-ys) == 2 and abs(x-xs) == 2 and self.board[y-1][x-1] < 2 and (self.board[(y+ys)/2 - 1][(x+xs)/2 - 1] == 2 or self.board[(y+ys)/2 - 1][(x+xs)/2 - 1] == 4)):
              self.board[ys-1][xs-1] = ys%2 + xs%2 - 1
              if(y == 1):
                self.board[y-1][x-1] = 5
              else:
                self.board[y-1][x-1] = 3
              self.board[(y+ys)/2 - 1][(x+xs)/2 - 1] = ((y+ys)/2)%2 + ((x+xs)/2)%2 - 1
            else:
              if self.status == Status.bot1_next:
                self.status = Status.bot2_next
              else:
                self.status == Status.bot1_next
          elif(self.board[ys-1][xs-1] == 5):
            test = True
            for i in range(min(y - (y-ys)/abs(y-ys), ys)+1, max(y - (y-ys)/abs(y-ys), ys)):
              for j in range(min(x- (x-xs)/abs(x-xs), xs)+1, max(x- (x-xs)/abs(x-xs), xs)):
                if(self.board[i-1][j-1] > 1):
                  test = False
            if (abs(y-ys) == abs(x-xs) and self.board[y-1][x-1] < 2 and test):
              self.board[ys-1][xs-1] = ys%2 + xs%2 - 1
              self.board[y-1][x-1] = 5
            elif(abs(y-ys) == abs(x-xs) and (self.board[y - (y-ys)/abs(y-ys) -1][x - (x-xs)/abs(x-xs)-1] == 2 or self.board[y - (y-ys)/abs(y-ys) -1][x - (x-xs)/abs(x-xs)-1] == 4) and test and self.board[y - 1][x - 1] < 2):
              self.board[ys-1][xs-1] = ys%2 + xs%2 - 1
              self.board[y-1][x-1] = 5
              self.board[y - (y-ys)/abs(y-ys) -1][x - (x-xs)/abs(x-xs)-1] = (y - (y-ys)/abs(y-ys))%2 + (x - (x-xs)/abs(x-xs))%2 - 1
            else:
              if self.status == Status.bot1_next:
                self.status = Status.bot2_next
              else:
                self.status == Status.bot1_next
          else:
              if self.status == Status.bot1_next:
                self.status = Status.bot2_next
              else:
                self.status == Status.bot1_next
            

        return self.change_status()

    def change_status(self) -> Status:     #проверка на победу
        """
        Проверка на победу/ничью, изменение статуса.
        :return:
        Status: статус игры.
        """
        isone = False
        istwo = False
        for i in self.board:
          for j in i:
            if(j == 3 or j == 5):
              istwo = True
            if(j == 2 or j == 4):
              isone = True
        if (!istwo):
          self.status = Status.bot1_won
          return self.status
        if (!isone):
          self.status = Status.bot2_won
          return self.status
        if self.status == Status.bot1_next:
            self.status = Status.bot2_next
            return self.status
        if self.status == Status.bot2_next:
            self.status = Status.bot1_next
            return self.status

    def draw_board_image(self) -> Image:   #графика
        """
        Отрисовка поля.
        :return:
        Image: картинка поля в формате PIL Image.
        """
        image = Image.new('RGB', (420, 420), color=(255, 255, 255))
        canvas = ImageDraw.Draw(image)
        for i in range(1, 9):
          for j in range(1, 9):  # Сетка поля
            canvas.rectangle([140*(i-1), 140*(j-1), 140 * i, 140*j], width = 3, fill="black")
        for i in range(1, 9): 
            for j in range(1, 9):
                if(self.board[i-1][j-1] == 0):
                  canvas.ellipse([140*(i-1), 140*(j-1), 140 * i, 140*j], width = 3, fill="white", outline="white")
                if(self.board[i-1][j-1] == 1):
                  canvas.ellipse([140*(i-1), 140*(j-1), 140 * i, 140*j], width = 3, fill="black", outline="black")
                if(self.board[i-1][j-1] == 2):
                  canvas.ellipse([140*(i-1), 140*(j-1), 140 * i, 140*j], width = 3, fill="gray70", outline="gray70")
                if(self.board[i-1][j-1] == 3):
                  canvas.ellipse([140*(i-1), 140*(j-1), 140 * i, 140*j], width = 3, fill="gray35", outline="gray35")
                if(self.board[i-1][j-1] == 4):
                  canvas.ellipse([140*(i-1), 140*(j-1), 140 * i, 140*j], width = 3, fill="gray55", outline="gray55")
                if(self.board[i-1][j-1] == 5):
                  canvas.ellipse([140*(i-1), 140*(j-1), 140 * i, 140*j], width = 3, fill="gray20", outline="gray20")
        return image