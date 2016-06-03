import tkinter as tk
from tkinter import messagebox as mbox
from todo_app import ToDo
import sys


class ToDoGui:
	def __init__(self, root):
		self.t = ToDo()
		self.root = root
		self.mainframe = tk.Frame(self.root, bg="white")
		self.mainframe.pack(fill=tk.BOTH, expand=True)

		self.build_grid()
		self.build_banner()
		self.build_text_area()
		self.build_buttons()
		sys.stderr = TextRedirector(self.text, "stderr")
		self.entry()

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
		buttons_frame.grid(row=3, column=0, sticky='nsew',
											 padx=10, pady=10)
		buttons_frame.columnconfigure(0, weight=1)
		buttons_frame.columnconfigure(1, weight=1)
		buttons_frame.columnconfigure(2, weight=1)
		buttons_frame.columnconfigure(3, weight=1)
		buttons_frame.columnconfigure(4, weight=1)

		self.clear_button = tk.Button(
			buttons_frame,
			text='Clear',
			command=lambda: self.entry_field.delete(1.0, tk.END)
		)

		self.view_button= tk.Button(
			buttons_frame,
			text='View list',
			command=self.t.list_view
		)

		self.add_button = tk.Button(
			buttons_frame,
			text='Add task',
			command=lambda: self.t.add_task(self.input.get())
		)

		self.remove_button = tk.Button(
			buttons_frame,
			text='Remove task',
			command=lambda: self.t.remove_task(self.input.get())
		)

		self.complete_button = tk.Button(
			buttons_frame,
			text='Complete task',
			command=lambda: self.t.complete_task(self.input.get())
		)
		self.clear_button.grid(row=0, column=0, sticky='ew')
		self.view_button.grid(row=0, column=1, sticky='ew')
		self.add_button.grid(row=0, column=2, sticky='ew')
		self.remove_button.grid(row=0, column=3, sticky='ew')
		self.complete_button.grid(row=0, column=4, sticky='ew')

	def entry(self):
		self.input = tk.StringVar()
		entry_field = tk.Entry(self.mainframe, bd=2, textvariable=self.input)
		entry_field.grid(row=1, column=0, sticky='nwse', padx=10, pady=10)
		entry_field.insert(0, 'Enter task OR number of a task')
		entry_field.focus()
		self.entry_field = entry_field

	def build_text_area(self):
		text_frame = tk.Text(self.mainframe, wrap="word")
		text_frame.grid(row=2, column=0, sticky='nsew',
										padx=10, pady=10)

		text_frame.columnconfigure(0, weight=1)
		text_frame.config(state=tk.DISABLED)
		text_frame.tag_configure("stderr", foreground="#b22222")
		self.text = text_frame
		return self.text


class TextRedirector(object):
	def __init__(self, widget, tag="stderr"):
		self.widget = widget
		self.tag = tag

	def write(self, strs):
		self.widget.configure(state="normal")
		self.widget.delete(1.0, tk.END)
		self.widget.insert("end", strs, (self.tag,))
		self.widget.configure(state="disabled")

if __name__ == '__main__':
	root = tk.Tk()
	ToDoGui(root)
	root.mainloop()
