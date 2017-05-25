'''
Author: Sai Uday Bhaskar Mudivarty
Program: Queues
'''
class Queue:
    def __init__(self):
        self.items = list()
    
    def enqueue(self,data):
        self.items.insert(0,data)
    
    def dequeue(self):
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    def size(self):
        return len(self.items)
    
    def __str__(self):
        returnstring="Queue follows: \n"
        for element in self.items:
            returnstring += str(element)+"\n"
        return returnstring


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(5)
    queue.enqueue(10)
    print(queue.dequeue())
    # print(queue.size())
    print(queue.isEmpty())
    print(queue)