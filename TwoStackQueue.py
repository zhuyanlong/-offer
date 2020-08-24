# https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6?tpId=13&&tqId=11158&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self, node):
        # write code here
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(node)

    def pop(self):
        # return xx
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

def main():
    s=Solution()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    s.push(5)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())

main()