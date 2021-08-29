import tkinter as tk

class App:
    def __init__(self):
        # ウィンドウの初期化
        self.master = tk.Tk()
        self.master.title('TODOアプリ')
        self.master.geometry('400x300')

        #TODO入力エリアの作成
        self.input_area = InputArea(self.master)
        self.input_area.pack()

    def mainloop(self):
        #masterに処理を委譲
        self.master.mainloop()

class InputArea(tk.Frame):
    """
    TODOの入力エリア
    ユーザーの入力の処理
    TODOテキストを追加ボタンで追加
    """
    def __init__(self, master):
        super(InputArea, self).__init__(master)

        #ラベルの作成
        self.label = tk.Label(self, text='TODO')
        self.label.pack(side='left')

        #入力行の作成
        self.entry = tk.Entry(self)
        self.entry.pack(side='left')

        #追加ボタンの作成
        self.add_btn = tk.Button(self, text='追加', command=self._click_add_btn)
        self.add_btn.pack(side='left')

    def _click_add_btn(self):
        #DEBUG: 入力値の表示
        print('add', self.entry.get())


def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()