import tkinter as tk
from tkinter import messagebox as mbox


class ToDoGui:
	def __init__(self, root):
		self.root = root
		self.mainframe = tk.Frame(self.root, bg="white")
		self.mainframe.pack(fill=tk.BOTH, expand=True)

		self.build_grid()
		self.build_banner()
		self.build_buttons()


	def build_grid(self):
			self.mainframe.columnconfigure(0, weight=1)
			self.mainframe.rowconfigure(0, weight=0)
			self.mainframe.rowconfigure(1, weight=1)
			self.mainframe.rowconfigure(0, weight=0)


	def build_banner(self):
		banner = tk.Label(
			self.mainframe,
			bg="orange",
			text="PyKeep",
			fg="green",
			font=('Helvetica', 24)
		)
		banner.grid(
			row=0, column=0,
			sticky='ew',
			padx=10, pady=10
		)

	def build_buttons(self):
		buttons_frame = tk.Frame(self.mainframe)
		buttons_frame.grid(row=2, column=0, sticky='nsew',
											 padx=10, pady=10)
		buttons_frame.columnconfigure(0, weight=1)
		buttons_frame.columnconfigure(1, weight=1)
		buttons_frame.columnconfigure(2, weight=1)
		buttons_frame.columnconfigure(3, weight=1)

		self.view_button= tk.Button(
			buttons_frame,
			text='View list',
			command=None
		)

		self.add_button = tk.Button(
			buttons_frame,
			text='Add task',
			command=None
		)

		self.remove_button = tk.Button(
			buttons_frame,
			text='Remove task',
			command=None
		)

		self.complete_button = tk.Button(
			buttons_frame,
			text='Complete task',
			command=None
		)

		self.view_button.grid(row=0, column=0, sticky='ew')
		self.add_button.grid(row=0, column=1, sticky='ew')
		self.remove_button.grid(row=0, column=2, sticky='ew')
		self.complete_button.grid(row=0, column=3, sticky='ew')

if __name__ == '__main__':
	root = tk.Tk()
	ToDoGui(root)
	root.mainloop()
