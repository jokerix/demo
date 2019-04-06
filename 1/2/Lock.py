import threading
import random
import time

gMoney = 1000
gLock = threading.Lock()
gTotalTime = 10
gtimes = 0


class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gtimes
        while True:
            money = random.randint(100, 1000)
            gLock.acquire()
            if gtimes >= 10:
                gLock.release()
                break
            gMoney += money
            print('%s 生产了多少%d ,剩余%d' % (threading.current_thread(), money, gMoney))
            gtimes += 1
            gLock.release()
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100, 1000)
            gLock.acquire()
            if gMoney >= money:
                gMoney -= money
                print("%s 花费了多少%d,剩余%d" % (threading.current_thread(), money, gMoney))
            else:
                if gtimes >= gTotalTime:
                    gLock.release()
                    break
                print("%s消费者准备消费%d,剩余%d,不足" % (threading.current_thread(), money, gMoney))
            gLock.release()
            time.sleep(0.5)


def main():
    for x in range(3):
        t = Consumer(name='消费者%d' % x)
        t.start()
    for x in range(5):
        t = Producer(name='生产者%d' % x)
        t.start()


if __name__ == '__main__':
    main()
