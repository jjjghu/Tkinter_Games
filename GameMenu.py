from tkinter import *
from three_hall import three_hall 
from TicTacToe import TicTacToe 
from MineSweeper import MineSweeper


MONTY_HALL = "Monty Hall"
TIC_TAC_TOE = "Tic Tac Toe"
MINESWEEPER = "Mine Sweeper"
class GameMenu:
    def __init__(self):
        # 創建主視窗
        self.window = Tk()
        self.window.title('Game Menu')
        self.setGeometry()

        # 建立選單畫面
        self.menu_frame = Frame(self.window, bg="black")
        self.menu_frame.grid(row=0, column=0, sticky="nsew")
        self.create_menu()
        
    def start(self):
        self.window.mainloop()

    def setGeometry(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        w, h = 600, 800
        x, y = (screen_width - w) // 2, (screen_height - h) // 2
        self.window.geometry(f"{w}x{h}+{x}+{y}")
        self.window.configure(bg="BLACK")
        self.window.resizable(False, False)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
    def griding(self, frame, rows, cols):
        for i in range(rows):
            frame.grid_rowconfigure(i, weight=1)
        for i in range(cols):
            frame.grid_columnconfigure(i, weight=1)
    
    def enter_games(self, gameType : str):
        self.window.withdraw()
        game_window = Toplevel(self.window)
        print(gameType)
        if gameType == MONTY_HALL:
            game = three_hall(game_window)
        elif gameType == TIC_TAC_TOE: 
            game = TicTacToe(game_window)
        elif gameType == MINESWEEPER:
            game = MineSweeper(game_window) 
        self.window.wait_window(game_window)
        self.window.deiconify()
    
    def create_menu(self):
        self.griding(self.menu_frame,8, 5)
        
        title_label = Label(self.menu_frame, text="任天堂最新版", font=("Arial", 30), bg="black", fg="white")
        title_label.grid(row=1, column=2, padx=20, pady=20, sticky="NSEW")
        
        row = 2
        gameTypes = [MONTY_HALL, TIC_TAC_TOE, MINESWEEPER]
        for gameType in gameTypes:
            button = Button(self.menu_frame, text=gameType, font=("Arial", 14), bg="lightblue", activebackground="lightblue",
                            command = lambda gameType=gameType: self.enter_games(gameType))
            button.grid(row=row,column=2,padx=50,pady=20,sticky=NSEW)
            row += 1
                        
        exit_btn = Button(self.menu_frame, text="退出", font=("Arial", 14),
                          bg="red", activebackground="darkred",
                          command=self.window.quit)
        exit_btn.grid(row=row, column=2, padx=50, pady=20, sticky="NSEW")
        
if __name__ == "__main__":
    gamemenu = GameMenu()
    gamemenu.start()