import tkinter as tk

class App:
    def __init__(self):
        # ウィンドウの初期化
        self.master = tk.Tk()
        self.master.title('TODOアプリ')
        self.master.geometry('400x300')

    def mainloop(self):
        #masterに処理を委譲
        self.master.mainloop()

def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()