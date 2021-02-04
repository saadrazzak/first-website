# creat a stack class impement a method which can add and remove the value 
# last come fist out
# and a method which can return the top value of stack 
class Stack:

	def __init__(self):
		self.stack = []

	def add(self, data):
		self.stack.append(data)

	def top(self):
		return self.stack[-1]

	def remove(self):
		if (len(self.stack)) <= 0:
			print("stack is empty")
		else:
			self.stack.pop()



#		CONVERT INFIX TO PRIFIX 
# infix exp (a+b*c) to postfix exp (abc*+)

# to check the stack's operator order in bodmas
def higher_pre(stack_op, exp_op):

	high = ["*" , "/"]
	low = ["+" , "-"]

	if stack_op in low and exp_op in high:
		return False
	else:
		return True

# to check the brackets if open or close
def is_open_pera(open):
	open_pera = ['(', '[' , '{']

	if open in open_pera:
		return True

def is_close_pera(close):
	close_pera = [')', ']' , '}']

	if close in close_pera:
		return True

# to convert infix expression (a+b*c) to postfix expresssion (abc*+) via bodmas rules
def infix_to_postfix(string):
	expresion = string
	operator = ["*", "/", "+", "-"]
	bracket = ['(', '[' , '{',')', ']' , '}']
	result = str()

	for i in range(len(string)):

		# ignore space and comas in expression
		if expresion[i] == ' ' or expresion[i] == ',':
			continue

		# if string[i] is operand store in stack
		elif expresion[i] not in operator and expresion[i] not in bracket :
			result = result + expresion[i]

		#  if string[i] is an operator
		elif expresion[i] in operator:

			# if stack's top value has higher order and not an open bracket
			# pop out the top value from stack and store into prefix string
			# until an open bracket incounter
			while len(a_stack.stack) != 0 and not is_open_pera(a_stack.top()) and higher_pre(a_stack.top(), expresion[i]):
				result = result + a_stack.top()
				a_stack.remove()

			# add the operator if its lower order than the stack's top value
			a_stack.add(expresion[i])

		# if string[i] is an open bracket put it into stack top
		elif is_open_pera(expresion[i]):
			a_stack.add(expresion[i])

		# if string[i] is close bracket
		elif is_close_pera(expresion[i]):

			# if string[i] is close bracket then pop out all the values from the stack
			# put it into prefix expression til an open bracket arive
			while len(a_stack.stack) != 0 and not is_open_pera(a_stack.top()):
				result = result + a_stack.top()
				a_stack.remove()

			# here an open bracket arive so it pop out
			a_stack.remove()

	# add the remaing operator at the top of the stack to prefix expression
	result = result + a_stack.top()
	a_stack.remove()

	return result 



a_stack = Stack()

# exp = "5*4+3"
exp = "3 - [5+{2-(1-7)}]"
# exp = "1 + (4*3)- (2*1) "

postfix = infix_to_postfix(exp)
print(postfix)



#		EVOLUTE THE POSTFIX EXPRESION

# evalute only one digit equation 


# perform calculation by bodmas order
# and return back the value to stack
def perform_task(operator, op2, op1):
	operators = ["*", "/", "+", "-"]
	res = 0

	if operator == operators[0]:
		res = int(op2) * int(op1)
		return res
	elif operator == operators[1]:
		res = int(op2) / int(op1)
		return res 
	elif operator == operators[2]:
		res = int(op2) + int(op1)
		return res
	else:
		res = int(op2) - int(op1)
		return res



# evoltuion of postfix expression by bodmas rule
# put all the operand on the stack uuntil an operator arive
# calculate the last two values using this operator 
# and put back the result back to the top of the operand stack
def evolute_postfix(postfix):
	terms = postfix
	operators = ["*", "/", "+", "-"]

	for i in range(len(terms)):
		# if postfix[i] is an operand put it on the stack
		if postfix[i] not in operators:
			b_stack.add(postfix[i])

		# if its an operator pop out last tow operand from stack
		elif postfix[i] in operators:
			op2 = b_stack.top()
			b_stack.remove()
			op1 = b_stack.top()
			b_stack.remove()

			# check which operator it is 
			for j in range(len(operators)):
				if postfix[i] == operators[j]:
					OP = operators[j]

			#  calculate last two operands and put back it result back on the stack
			result = perform_task(OP, op2, op1)
			b_stack.add(result)

	return b_stack.top()


b_stack = Stack()

ans = evolute_postfix(postfix)

print(ans)
