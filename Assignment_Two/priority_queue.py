#!/bin/python3

# Marcus Butler
# Assignment 2 - priority_queue.py
# CS635 - Advanced Object-Oriented Programming & Design
# Dr. Roger Whitney
# Fall '18

from student import Student

class PriorityQueue:
	#Inner class "Node" definition. Data field encapsulates whatever object is received. Priority
	#determined by user input as specified by numerical literal or function return.
	class Node:
		def __init__(self, data, priority):
			self.data = data
			self.priority = priority

		def get_priority(self):
			return self.priority

	#Begin PriorityQueue class definition
	def __init__(self):
		self.list = []

	def is_empty(self):
		return 

	def heapify_max_heap(self):
		"""
		This sorts the elements in a list so that the element with the highest 'priority_value'
		resides at the top of the list via max heap.
		:return:
		"""
		if len(self.list) < 1:
			return
		length = len(self.list)
		for index in range(length, 1, -2):
			parentIndex = (index - 2)//2
			rightChildIndex = parentIndex * 2 + 2
			leftChildIndex = parentIndex * 2 + 1
			#check the right child. if its priority is higher, swap with parent
			if(rightChildIndex <= (length -1)):	
				if(self.list[rightChildIndex].priority > self.list[parentIndex].priority):
					temp = self.list[rightChildIndex]
					self.list[rightChildIndex] = self.list[parentIndex]
					self.list[parentIndex] = temp
			#check the left child. if its priority is higher, swap with parent
			if(leftChildIndex <= (length -1)):	
				if(self.list[leftChildIndex].priority > self.list[parentIndex].priority):
					temp = self.list[leftChildIndex]
					self.list[leftChildIndex] = self.list[parentIndex]
					self.list[parentIndex] = temp

	#add_node function accepts an object and a priority, instantiates a new node containing the dataand appends it to the priority queue list 	
	def enqueue(self, object_input, priority):
		newNode = PriorityQueue.Node(object_input, priority)	
		self.list.append(newNode)
		self.heapify()
	
	def dequeue(self):
		if len(self.list) <= 0:
			raise ValueError ("[-] Error: Unable to remove from empty queue!")
		else:
			self.list[0] = self.list[len(self.list)-1]
			self.list.pop(len(self.list)-1)
			self.heapify()	

	def print_all_students(self):
		if len(self.list) <= 0:
			raise ValueError ("[-] Error: Empty queue. Nothing to print!")
		else:
			optimizedPriorityQueue = []
			while len(self.list) > 0:
				optimizedPriorityQueue.append(self.list[0])
				self.list[0].print_stats()
				self.remove_node()
			self.list = optimizedPriorityQueue
