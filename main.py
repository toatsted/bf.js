import sys
from tkinter import Tk, Label, Button, StringVar, Toplevel, Message
from tkinter.filedialog import askopenfilename

from bf import read

class MainGUI:
    def __init__(self, master):
        self.master = master
        master.title("Brainf*uck Interpreter")

        self.greet_button = Button(master, text="Choose File", command=self.chooseFile)
        self.greet_button.pack()

    def chooseFile(self):
      file = askopenfilename();
      f = open(file, 'r')
      query = f.read().rstrip('\n')
      f.close()
      end = read(query)

      popup = Toplevel(self.master)
      msg = Message(popup, text=end)
      msg.pack()

      btn = Button(popup, text="Dismiss", command=self.master.quit )
      btn.pack()

def main():
	root = Tk()
	my_gui = MainGUI(root)
	root.mainloop()

if __name__ == '__main__':
	main()