from tkinter import *
from three_hall import three_hall 
from TicTacToe import TicTacToe 
from MineSweeper import MineSweeper

class GameMenu:
    def __init__(self):
        # 創建主視窗
        self.window = Tk()
        self.window.title('Game Menu')
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        w, h = 600, 800
        x, y = (screen_width - w) // 2, (screen_height - h) // 2
        self.window.geometry(f"{w}x{h}+{x}+{y}")
        self.window.configure(bg="BLACK")
        self.window.resizable(False, False)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        # 建立選單畫面
        self.menu_frame = Frame(self.window, bg="black")
        self.menu_frame.grid(row=0, column=0, sticky="nsew")
        self.setup_menu()

        # 顯示選單
        self.menu_frame.tkraise()

    def start(self):
        self.window.mainloop()
        
    def griding(self, frame, rows, cols):
        for i in range(rows):
            frame.grid_rowconfigure(i, weight=1)
        for i in range(cols):
            frame.grid_columnconfigure(i, weight=1)
    
    # 遊戲1: Montyhall
    def enter_monty_hall(self):
        self.window.withdraw()  
        MontyHall_window = Toplevel(self.window) 
        game = three_hall(MontyHall_window)  
        self.window.wait_window(MontyHall_window)  
        self.window.deiconify()

    # 遊戲2: TicTacToe
    def enter_TicTacToe(self):
        self.window.withdraw()  
        TicTacToe_window = Toplevel(self.window) 
        game = TicTacToe(TicTacToe_window)  
        self.window.wait_window(TicTacToe_window)  
        self.window.deiconify()
        
    # 遊戲3: MineSweeper
    def enter_minesweeper(self):
        self.window.withdraw()  
        MineSweeper_window = Toplevel(self.window) 
        game = MineSweeper(MineSweeper_window)  
        self.window.wait_window(MineSweeper_window)  
        self.window.deiconify()

    def setup_menu(self):
        self.griding(self.menu_frame,8, 5)
        
        title_label = Label(self.menu_frame, text="任天堂最新版", font=("Arial", 30), bg="black", fg="white")
        title_label.grid(row=1, column=2, padx=20, pady=20, sticky="NSEW")


        monty_hall_btn = Button(self.menu_frame, text="Monty Hall", font=("Arial", 14),
                                bg="lightblue", activebackground="lightblue",
                                command=self.enter_monty_hall)
        monty_hall_btn.grid(row=2, column=2, padx=50, pady=20, sticky="NSEW")


        monty_hall_btn = Button(self.menu_frame, text="Tic Tac Toe", font=("Arial", 14),
                                bg="lightblue", activebackground="lightblue",
                                command=self.enter_TicTacToe)
        monty_hall_btn.grid(row=3, column=2, padx=50, pady=20, sticky="NSEW")
        

        minesweeper_btn = Button(self.menu_frame, text="Mine Sweeper", font=("Arial", 14),
                                bg="lightblue", activebackground="lightblue",
                                command=self.enter_minesweeper)
        
        minesweeper_btn.grid(row=4, column=2, padx=50, pady=20, sticky="NSEW")


        exit_btn = Button(self.menu_frame, text="退出", font=("Arial", 14),
                          bg="red", activebackground="darkred",
                          command=self.window.quit)
        exit_btn.grid(row=6, column=2, padx=50, pady=20, sticky="NSEW")
        
if __name__ == "__main__":
    gamemenu = GameMenu()
    gamemenu.start()