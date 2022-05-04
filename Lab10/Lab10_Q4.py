
class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty() == True:
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if self.is_empty() == True:
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        if len(self.stack)== 0:
            stack_str = "[ "
        else:
            stack_str = "["
            for index in range(len(self.stack)):
                if isinstance(self.stack[index], str):
                    if index == (self.size()-1):
                        stack_str += "'" + (str(self.stack[index])) + "' "
                    else: 
                        stack_str += "'" + (str(self.stack[index])) + "', "
                else:
                    if index == (self.size()-1):
                        stack_str += (str(self.stack[index])) + " "
                    else: 
                        stack_str += (str(self.stack[index])) + ", "
        stack_str += "<-"
        return stack_str

    def clear(self):
        for index in range(len(self.stack)):
            self.stack.pop()


def evaluate_postfix(postfix_list):
    operand_stack = Stack()
    operator_list = ["+", "/", "-", "*"]
    number_list = [str(num) for num in range(100000)]
    for element in postfix_list:
        if element in number_list:
            operand_stack.push(int(element))
        else:
            if element == "+":
                num2 = operand_stack.pop()
                num1 = operand_stack.pop()
                evaluation = compute(num1, num2, "+")
                operand_stack.push(evaluation)
            elif element == "-":
                num2 = operand_stack.pop()
                num1 = operand_stack.pop()
                evaluation = compute(num1, num2, "-")
                operand_stack.push(evaluation)
            elif element == "/":
                num2 = operand_stack.pop()
                num1 = operand_stack.pop()
                evaluation = compute(num1, num2, "/")
                operand_stack.push(evaluation)
            elif element == "*":
                num2 = operand_stack.pop()
                num1 = operand_stack.pop()
                evaluation = compute(num1, num2, "*")
                operand_stack.push(evaluation)
    return operand_stack.pop()


def compute(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    else:
        return number1 // number2


print(evaluate_postfix(['2', '10', '+']))