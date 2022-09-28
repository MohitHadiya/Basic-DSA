from collections import deque

stack = deque()

def operation_push():
	value = input("Enter value for push in stack : ")
	stack.append(value)
	print(stack)

def operation_pop():
	if stack:
		stack.pop()
		print(stack)
	else:
		print("Stack is empty")

while True:
	try:
		option = int(input("Choose Operation for stack 1.Push 2.Pop 3.Exit : "))
		if option == 1:
			 operation_push()
		elif option == 2:
			operation_pop()
		elif option == 3:
			break
		else:
			print("Choose Correct Option")
	except:
		print("Please Choose Correct Option")
