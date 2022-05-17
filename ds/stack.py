class Stack:

    def __init__(self, stack_size: int):
        self.__stack = []
        self.__stack_size = stack_size

    def push(self, info):
        if len(self.__stack) >= self.__stack_size:
            raise Exception("!! OVER FLOW EXCEPTION !!")
        else:
            self.__stack.append(info)

    def pop(self):
        if len(self.__stack) == 0:
            raise Exception("!! UNDER FLOW EXCEPTION !!")
        else:
            return self.__stack.pop()

    def show_as_insert_record(self):
        return self.__stack[::-1]


if __name__ == '__main__':
    stack = Stack(10)

    for i in range(1, 11): stack.push(i)

    print(stack.show_as_insert_record())

    for j in range(1, 11): print(stack.pop())