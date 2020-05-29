'''
一个队列,弹出数,insert进数,始终知道里面最大是几.

方法就是每一次窗口中加入一个新的数字的时候,需要吧里面比这个新数字小的都扔了.

'''
# 通过下面的push,让队列一直保持升序
import queue
class dandiaoQueue(queue.Queue):
    def top(self):
        return self[-1]

    def push(self,a):
        for i in self:
            if i<=a:
                self.pop(0)
        self.append(a)
    def pop2(self):
        self.pop(0)
a=dandiaoQueue([])

a.push(1)
a.push(3)
a.push(2)
a.push(4)

print(a)


