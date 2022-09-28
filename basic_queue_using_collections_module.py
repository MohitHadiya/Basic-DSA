from collections import deque

queue = deque()

def operation_enqueue():
	value = input("Enter Value for add in Queue : ")
	queue.append(value)

def operation_dequeue():
	if queue:
		print(queue.popleft())
	else:
		print("Queue is empty... :( ")

while True:
	choice = input("Choose option for queue operation A.Enqueue B.Dequeue C.Show Queue D.Exit : ")
	
	if choice in ['A','a']:
		operation_enqueue()
	elif choice in ['B','b']:
		operation_dequeue()
	elif choice in ['C','c']:
		print(queue)
	elif choice in ['D','d']:
		break
	else:
		print("Please enter correct option... :( ")
