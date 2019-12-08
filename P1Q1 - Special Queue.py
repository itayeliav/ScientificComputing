#Part 1 Question 1 - Special Queue


#-----------------------------------------------------------------------


class Node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

	def __str__(self):
		return str(self.data)

class SpecialQueue:
	def __init__(self):
		self.head = Node()

	def __str__(self):
		return str(self.objectsToArray())


	def objectsToArray(self):
		objectList=[]
		if self.head.data == None:
			return "There are no objects in the list."
		else:
			objectList.append(self.head.data)
			cur_node=self.head
			while cur_node.next!=None:
				objectList.append(cur_node.next.data)
				cur_node=cur_node.next

			return objectList

	def size(self):
		queueSize=0
		cur_node = self.head
		if cur_node.data!=None:
			queueSize+=1
			while cur_node.next != None:
				cur_node = cur_node.next
				queueSize+=1
		return queueSize

	def enqueue(self,data):
			new_node = Node(data)
			cur_node = self.head
			if cur_node.data == None:
				self.head = new_node
			else:
				while cur_node.next!=None:
					cur_node=cur_node.next
				cur_node.next = new_node


	def dequeue(self):
		if self.head!=None:
			print(str(self.head.data)+"! It's your turn! Do you want mustard with it?")
			self.head = self.head.next
			if self.head==None: #To avoid the head itself being null instead of having null values.
				self.head=Node()
		else:
			print("Oh, there is no one in line. Guess i'll take a break.")

	def is_empty(self):
		if self.head.data==None:
			return True
		else:
			return False

