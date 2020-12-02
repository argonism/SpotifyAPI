import threading, queue
import time
 
def printNum(num, q):
    for i in num:
        print("Num:",i)
        time.sleep(5)
        q.put(i)
 
def addX(q):
    while True:
        _num = q.get()
        _num += 10
        print("Num(add10):",_num);
        time.sleep(10)
        q.task_done()
 
q = queue.Queue()
for n in range(2):
    thread = threading.Thread(target=addX, args=(q,))
    thread.start()
 
num = [1,2,3,4,5,6,7,8,9]
printNum(num, q)
q.join()