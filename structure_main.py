from stack import Stack

if __name__ == '__main__':
    stk_ob1 = Stack()
    print(stk_ob1.is_empty())

    stk_ob1.push(10)
    print(stk_ob1.is_empty())

    for i in range(0, 10):
        stk_ob1.push(i)

    print(stk_ob1.peek())
    print(stk_ob1.size())

    stk_ob2 = Stack()
    name = "Haruto"
    for ch in name:
        stk_ob2.push(ch)

    reverse = ""
    while stk_ob2.size():
        reverse += stk_ob2.pop()

    print(name)
    print(reverse)
