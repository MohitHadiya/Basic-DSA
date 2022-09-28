from queue import LifoQueue

stack = LifoQueue(maxsize=3)

def operation_push():
	value = input("Enter Value for push in stack : ")
	stack.put(value,timeout = 1)

def operation_pop():
	print(stack.get(timeout = 1))

while True:
	option = int(input("Choose Operation for stack 1.Push 2.Pop 3.Exit : "))
	if option == 1:
		operation_push()
	elif option == 2:
		operation_pop()
	elif option == 3:
		break;
	else:
		print("Enter Valid Option")
