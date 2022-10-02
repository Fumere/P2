#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 18:49:42 2022

@author: dharmendrakhakhar
"""

# A simple implementation of Priority Queue
# using Queue.
class PriorityQueue():
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	# for checking if the queue is empty
	def isEmpty(self):
		return len(self.queue) == 0

	# for inserting an element in the queue
	def insert(self, data):
		self.queue.append(data)

	# for popping an element based on Priority
	def delete(self):
		try:
			min_val = 0
			for i in range(len(self.queue)):
				if self.queue[i][1] < self.queue[min_val][1]:
					min_val = i
			item = self.queue[min_val][0]
			del self.queue[min_val]
			return item
		except IndexError:
			print('Error')

# if __name__ == '__main__':
# 	myQueue = PriorityQueue()
# 	myQueue.insert(12)
# 	myQueue.insert(1)
# 	myQueue.insert(14)
# 	myQueue.insert(7)
# 	print(myQueue)		
# # 	while not myQueue.isEmpty():
#     # myQueue.delete()

