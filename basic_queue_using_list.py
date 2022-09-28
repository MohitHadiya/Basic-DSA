# queue = [1,2,3,4] 1 is front and 4 is tail for this program and we append from front and vise versa

queue = []

def enqueue():
	value = input('Enter value for add in queue : ')
	queue.insert(0,value)

def dequeue():
	if queue:
		queue.pop()
	else:
		print('Queue is empty. :(')

while True:
	option = input("Choose option for queue operation 1.Enqueue 2.Dequeue 3.Show Queue 4.Exit : ")
	if option == '1':
		enqueue()
	elif option == '2':
		dequeue()
	elif option == '3':
		print(queue)
	elif option == '4':
		break
	else:
		print("Please enter correct option... :(")
