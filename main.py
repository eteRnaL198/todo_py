import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title('TODOアプリ')
        self.master.geometry('400x300')

        self.task_list = Tasks(self.master)
        self.input_area = InputArea(self.master, self.task_list)
        self.input_area.pack()
        self.task_list.pack()

    def mainloop(self):
        self.master.mainloop()

class InputArea(tk.Frame):
    def __init__(self, master, task_list):
        super(InputArea, self).__init__(master)

        self.label = tk.Label(self, text='TODO')
        self.label.pack(side='left', pady=8)

        self.entry = tk.Entry(self)
        self.entry.pack(side='left')

        self.add_btn = tk.Button(self, text='追加', command=lambda: self._update_task(task_list))
        self.add_btn.pack(side='left', padx=8)

        self.rew_btn = tk.Button(self, text='上書き', command=lambda: self._edit_task(task_list))
        self.rew_btn.pack(side='left')

        self.rem_btn = tk.Button(self, text='削除', command=task_list.remove_task)
        self.rem_btn.pack(side='left', padx=8)

    def _update_task(self, task_list):
        if self.entry.get().strip():
            task_list.add_task(self.entry.get())
        else:
            messagebox.showwarning('warning', '文字を入力してください')
        self.entry.delete(0, tk.END)

    def _edit_task(self, task_list):
        if self.entry.get():
            for task in task_list.tasks:
                if task['val'].get():
                    task['text'].set(self.entry.get())

            self.entry.delete(0, tk.END)

class Tasks(tk.Frame):
    def __init__(self, master):
        super(Tasks, self).__init__(master)
        self.tasks = []

    def add_task(self, newText):
        # tasks → [{btn:tk.CheckButton, text:string, val:boolean}, {..}]
        self.is_checked = tk.BooleanVar()
        self.text = tk.StringVar()
        self.text.set(newText)
        self.check_btn = tk.Checkbutton(self, textvariable=self.text, variable=self.is_checked)
        self.elem = {"btn": self.check_btn, "text": self.text, "val": self.is_checked}
        self.tasks.append(self.elem)
        self.tasks[len(self.tasks)-1]["btn"].pack()

    def remove_task(self):
        new_tasks = []
        if messagebox.askyesno("confirm", "削除しますか？"):
            for task in self.tasks:
                if task['val'].get() != True:
                    new_tasks.append(task)
                else:
                    task['btn'].destroy()
            self.tasks = new_tasks
            
def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()