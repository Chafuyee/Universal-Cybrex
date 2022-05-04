
def br():
    print("=" * 20)

br()

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

def is_balanced_brackets(text):

    bracket_stack = Stack()
    open_list = ["[", "{", "<", "("]
    closed_list = ["]", "}", ">", ")"]
    for char in text:
        if char in open_list:
            bracket_stack.push(char)
        if char in closed_list:
            if bracket_stack.size() == 0:
                return False
            check_value = bracket_stack.pop()
            if check_value == "[":
                if char != "]":
                    return False
            elif check_value == "{":
                if char != "}":
                    return False
            elif check_value == "<":
                if char != ">":
                    return False
            elif check_value == "(":
                if char != ")":
                    return False
                    

    if bracket_stack.size() == 0:
        return True
    else:
        return False


print(is_balanced_brackets('({x})(())()'))

br()