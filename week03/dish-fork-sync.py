import threading
from multiprocessing import Process
import queue


class DiningPhilosophers(threading.Thread):
    def __init__(self, Philosopher,Time):
        self.Philosopher = Philosopher
        self.Time = Time
        self.Lock = threading.Lock()

    def wantsToEat(self):
        eat_list.append(self.Philosopher,1,self.Time)

    def pickLeftFork(self):
        print(f'哲学家 {self.Philosopher} 拿起左边的叉子')
        # self.Lock.acquire()

    def pickRightFork(self):
        print(f'哲学家 {self.Philosopher} 拿起右边的叉子')
        # self.Lock.acquire()
    
    def putLeftFork(self):
        print(f'哲学家 {self.Philosopher} 放下左边的叉子')
        # self.Lock.release()

    def putRightFork(self):
        print(f'哲学家 {self.Philosopher} 放下右边的叉子')
        # self.Lock.release()

    def eat(self):
        print(f'哲学家第 {self.Time} 次吃面')

        
# a 哲学家编号。
# b 指定叉子：{1 : 左边, 2 : 右边}.
# c 指定行为：{1 : 拿起, 2 : 放下, 3 : 吃面}

if __name__ == "__main__":
    eat_list = []
    for Philosopher in range(1,5):
        p = DiningPhilosophers(Philosopher,1)
        p.Lock.acquire()
        p.pickLeftFork()
        eat_list.append([Philosopher,1,1])
        p.pickRightFork()
        eat_list.append([Philosopher,2,1])
        p.eat()
        eat_list.append([Philosopher,2,3])
        p.Lock.release()
        p.putLeftFork()
        eat_list.append([Philosopher,1,2])
        p.putRightFork()
        eat_list.append([Philosopher,2,2])
    print(eat_list)
        


   
    
