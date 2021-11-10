from tkinter import *
from tkinter import messagebox, filedialog
from pdf2docx import parse

root = Tk()
root.resizable(False, False)
root.config(bg='black')
root.iconbitmap("PDF To Word.ico")
root.geometry("300x190")
root.title("Word To PDF Converter")


def file():
    global pdf
    pdf = filedialog.askopenfilename(initialdir="C:/Users/Welcome/Documents", title='Select File', filetype=(("PDF", "*.pdf"),("All Files", "*.*")))
    path.insert(0, str(pdf))


Label(root, text='PDF To Word Converter', font=('rosemary', 20, 'bold', 'italic', 'underline'), bg='black', fg='#06beb6').pack(pady=10)
path=Entry(root,width=28, bd=0, font=('times', 15, 'italic'), bg='black', fg='gray')
path.pack()
im = Button(root, text='Import', command=file, bg='black', fg='white', activebackground='black', activeforeground="#ee9ca7", font=("rosemary", 15, "italic"), bd=0)
im.pack()

def export():
    if len(path.get()) != 0 :
        word = filedialog.asksaveasfilename(initialdir="C:/Users/Welcome/Documents", title='Save As', defaultextension=".docx",
                                      filetype=(("Word", "*.docx"), ("All Files", "*.*")))
        parse(str(pdf), str(word), start=0, end=None)
        messagebox.showinfo('PDF To Word', 'Word File Exported Successfully!')
        path.delete(0, END)
    else:
        messagebox.showerror('PDF To Word', 'No File Was Imported')

ex = Button(root, text='Export', command=export, bg='black', fg='white', activebackground='black', activeforeground="#00FF00", font=("rosemary", 15, "italic"), bd=0)
ex.pack()


def exit():
    d = messagebox.askquestion('Exit Application', "Do You Want Exit The Application?")
    if d =="yes":
        root.destroy()
    else:
        return None


close = Button(root, text='Exit', command=exit, bd=0, font=("rosemary", 12, "italic"), bg='black', fg='white', activebackground='black', activeforeground='#ff0000').pack()

root.mainloop()
