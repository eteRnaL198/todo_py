import tkinter as tk

class App:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title('TODOアプリ')
        self.master.geometry('400x300')

        self.tasks = Tasks(self.master)
        self.input_area = InputArea(self.master, self.tasks)
        self.input_area.pack()
        self.tasks.pack()

    def mainloop(self):
        self.master.mainloop()

class InputArea(tk.Frame):
    def __init__(self, master, tasks):
        super(InputArea, self).__init__(master)

        self.label = tk.Label(self, text='TODO')
        self.label.pack(side='left', pady=8)

        self.entry = tk.Entry(self)
        self.entry.pack(side='left')

        self.add_btn = tk.Button(self, text='追加', command=lambda: self._update_task(tasks))
        self.add_btn.pack(side='left', padx=8)

        self.rem_btn = tk.Button(self, text='削除', command=tasks.remove_task)
        self.rem_btn.pack(side='left')

    def _update_task(self, tasks):
        if self.entry.get():
            tasks.add_task(self.entry.get())
            self.entry.delete(0, tk.END)

class Tasks(tk.Frame):
    def __init__(self, master):
        super(Tasks, self).__init__(master)
        self.tasks = []

    def add_task(self, newText):
        # tasks → [{btn:tk.CheckButton, text:string val:boolean}, {..}]
        self.is_checked = tk.BooleanVar()
        self.text = tk.StringVar()
        self.text.set(newText)
        self.check_btn = tk.Checkbutton(self, textvariable=self.text, variable=self.is_checked)
        self.elem = {"btn": self.check_btn, "val": self.is_checked}
        self.tasks.append(self.elem)
        self.tasks[len(self.tasks)-1]["btn"].pack()

    def remove_task(self):
        i=0
        for task in self.tasks:
            if task['val'].get():
                task['btn'].destroy()
                self.tasks.pop(i)
            else:
                i += 1

            
def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()