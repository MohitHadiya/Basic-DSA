from queue import Queue

queue = Queue()

def operation_enqueue():
	value = input("Enter Value for add in Queue : ")
	queue.put(value)

def operation_dequeue():
	if queue:
		print(queue.get())
	else:
		print("Queue is empty... :( ")

while True:
	choice = input("Choose option for queue operation A.Enqueue B.Dequeue C.Exit : ")
	
	if choice in ['A','a']:
		operation_enqueue()
	elif choice in ['B','b']:
		operation_dequeue()
	elif choice in ['C','c']:
		break
	else:
		print("Please enter correct option... :( ")
