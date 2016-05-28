# Implement Queue using two Stacks.


class queueUsingTwoStack():
	def __init__(self):
		self.stack1 = []
		self.stack2 = []
		self.numberOfPushOperation = 0
		self.numberOfPopOperation = 0

	def Enqueue(self, element):
		self.stack1.append(element)
		self.numberOfPushOperation += 1

	def Dequeue(self):
		if not self.stack2:
			while self.stack1:
				stack1TopElement = self.stack1.pop()
				self.numberOfPopOperation += 1
				self.stack2.append(stack1TopElement)
				self.numberOfPushOperation += 1

		if not self.stack2:
			return "Queue is empty"
		else:
			self.numberOfPopOperation += 1
			return self.stack2.pop()

	def NumberOfOprations(self):
		return "Number of push operations = " + str(self.numberOfPushOperation) + "\nNumber of pop operations = " + str(self.numberOfPopOperation)

if __name__ == "__main__":
	q = queueUsingTwoStack()

	q.Enqueue(1)
	q.Enqueue(2)
	q.Enqueue(3)
	print q.NumberOfOprations()
	print q.Dequeue()
	print q.NumberOfOprations()
	q.Enqueue(4)
	q.Enqueue(5)
	print q.NumberOfOprations()
	print q.Dequeue()
	print q.Dequeue()
	print q.NumberOfOprations()
	print q.Dequeue()
	print q.Dequeue()
	print q.NumberOfOprations()
	print q.Dequeue()
