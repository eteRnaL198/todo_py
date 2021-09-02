import tkinter as tk

class App:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title('TODOアプリ')
        self.master.geometry('400x300')

        # tasks → [{btn:tk.CheckButton, text:string val:boolean}, {}]
        self.tasks = []
        self.input_area = InputArea(self.master, self.tasks, self._remove_task)
        self.input_area.pack()

    def _remove_task(self):
        i=0
        for task in self.tasks:
            if task['val'].get():
                task['btn'].destroy()
                self.tasks.pop(i)
            else:
                i += 1


    def mainloop(self):
        self.master.mainloop()

class InputArea(tk.Frame):
    """
    TODOの入力エリア
    ユーザーの入力の処理
    TODOテキストを追加ボタンで追加
    """
    def __init__(self, master, tasks, remove):
        super(InputArea, self).__init__(master)

        self.tasks = tasks
        self.remove = remove

        self.label = tk.Label(self, text='TODO')
        self.label.pack(side='left')

        self.entry = tk.Entry(self)
        self.entry.pack(side='left')

        self.add_btn = tk.Button(self, text='追加', command=self._update_task)
        self.add_btn.pack(anchor=tk.N)

        self.rem_btn = tk.Button(self, text='削除', command=self.remove)
        self.rem_btn.pack(anchor=tk.N)

    def _update_task(self):
        if self.entry.get():

            self.is_checked = tk.BooleanVar()
            self.text = tk.StringVar()
            self.text.set(self.entry.get())
            self.check_btn = tk.Checkbutton(self, textvariable=self.text, variable=self.is_checked)
            self.elem = {"btn": self.check_btn, "val": self.is_checked}
            self.tasks.append(self.elem)
            self.tasks[len(self.tasks)-1]["btn"].pack(side='left')

            self.entry.delete(0, tk.END)

            
def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()