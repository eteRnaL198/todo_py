import tkinter as tk

class App:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title('TODOアプリ')
        self.master.geometry('400x300')

        self.tasks = ['foo', 'bar', 'hoge']
        self.input_area = InputArea(self.master, self.tasks, self.reRenderTaskList)
        self.input_area.pack()
        self.task_list = TaskList(self.master, self.tasks)
        self.task_list.pack()

    def reRenderTaskList(self):
        self.task_list.destroy()
        self.task_list.pack()

    def mainloop(self):
        self.master.mainloop()

class InputArea(tk.Frame):
    """
    TODOの入力エリア
    ユーザーの入力の処理
    TODOテキストを追加ボタンで追加
    """
    def __init__(self, master, tasks, reRender):
        super(InputArea, self).__init__(master)

        self.tasks = tasks
        self.reRender = reRender

        self.label = tk.Label(self, text='TODO')
        self.label.pack(side='left')

        self.entry = tk.Entry(self)
        self.entry.pack(side='left')

        self.add_btn = tk.Button(self, text='追加', command=self._add_task)
        self.add_btn.pack(side='left')

    def _add_task(self):
        self.tasks.append(self.entry.get())
        self.reRender()
        print(self.tasks)
        # print('add', self.entry.get())

class TaskList(tk.Frame):
    def __init__(self, master, tasks):
        super(TaskList, self).__init__(master)
        for task in tasks:
            self.check_btn = tk.Checkbutton(self, text=task)
            self.check_btn.pack()

def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()