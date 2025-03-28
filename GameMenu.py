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
    
    def enter_games(self, gameType : str):
        self.window.withdraw()
        game_window = Toplevel(self.window)
        
        if gameType == MONTY_HALL:
            game = three_hall(game_window)
        elif gameType == TIC_TAC_TOE: 
            game = TicTacToe(game_window)
        elif gameType == MINESWEEPER:
            game = MineSweeper(game_window) 
        
        self.window.wait_window(game_window)
        self.window.deiconify()
    
    def create_menu(self):
        self.menu_frame = Frame(self.window, bg="black", highlightthickness=2, highlightbackground="white")
        self.menu_frame.pack(expand=True, padx=40, pady=40, fill=BOTH)
        
        # 標題
        title_label = Label(self.menu_frame, text="任天堂最新版", font=("Arial", 30), bg="black", fg="white")
        title_label.pack(pady=20)
        
        # 遊戲按鈕
        gameTypes = [MONTY_HALL, TIC_TAC_TOE, MINESWEEPER]
        for gameType in gameTypes:
            button = Button(self.menu_frame, text=gameType, font=("Arial", 14),
                            bg="lightblue", activebackground="lightblue",
                            command=lambda gameType=gameType: self.enter_games(gameType))
            button.pack(padx=50, pady=30, ipady=30, fill=X)
        
        # 退出按鈕
        exit_btn = Button(self.menu_frame, text="退出", font=("Arial", 14),
                          bg="red", activebackground="darkred",
                          command=self.window.quit)
        exit_btn.pack(padx=50, pady=30, ipady=30, fill=X)
        
if __name__ == "__main__":
    gamemenu = GameMenu()
    gamemenu.start()