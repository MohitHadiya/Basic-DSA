stack = []
def action_push():
	value = input("Enter Value for Add in stack : ")
	stack.append(value)
	print(stack)

def action_pop():
	if stack:
		stack.pop()
		print(stack)
	else:
		print("Stack is Empty")

stack_lan = int(input("Enter Size of Stack : "))
while True:
	option = input("Choose Operation for stack 1.Push 2.pop 3.Exit : ")
	if option == '1':
		if stack_lan == len(stack):
			print("Stack Is Full")
		else:
			action_push()
	elif option == '2':
		action_pop()
	elif option == '3':
		break
	else:
		print("please Choose Correct Option : ")
