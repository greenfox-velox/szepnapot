class Stack:

	def __init__(self, things):
		self.things = things

	def size(self):
		return len(self.things)

	def push(self, item):
		self.things.append(item)

	def pop(self):
		last_item = self.things[-1]
		print(last_item)
		del last_item

s = Stack(['apple', 'banan', 'kiwi', 'orange', 'yolo'])
print(s.size())
s.push('alma')
s.pop()