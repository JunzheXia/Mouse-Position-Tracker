import pyperclip
import  PIL
import tkinter as tk
import pyautogui as pa
from tkinter import ttk, messagebox



def save_p():
    x, y = pa.position()
    positions.append((x, y))
    tree.insert('', tk.END, values=(x, y))
    messagebox.showinfo('保存成功', f'已保存位置：({x},{y})')


def delete_p():
    selection = tree.selection()
    if selection:
        tree.delete(selection)

def update_p():
    x, y = pa.position()
    cur.configure(text=f'当前鼠标位置: ({x},{y})')
    root.after(10, update_p)

def clear_all():
    if not positions:
        return
    if messagebox.askyesno('确认', '确定清空记录吗?'):
        tree.delete(*tree.get_children())
        positions.clear()


root = tk.Tk()
root.title('获取鼠标位置')
root.geometry('500x500')

positions = []

cur = ttk.Label(root, text='当前鼠标位置：(0, 0)')
cur.pack(pady=10)
btn = ttk.Button(root, text='按F2保存当前位置', command=save_p)
btn.pack(pady=10)

tree = ttk.Treeview(root, columns=['x', 'y'], show='headings')
tree.heading('x', text='x坐标')
tree.heading('y', text='y坐标')
tree.pack(fill='both', expand=True, padx=10, pady=10)

btn2 = ttk.Button(root, text='删除选中位置', command=delete_p)
btn2.pack(pady=10)

btn_clear = ttk.Button(root, text='清空记录', command=clear_all)
btn_clear.pack(pady=10)

root.bind('<F2>', lambda e: save_p())

update_p()

root.mainloop()