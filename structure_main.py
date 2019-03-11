from stack import Stack
from queue import Queue
import time
import random

def simulate_line(till_show, max_time, num_cus):
    pq = Queue()
    tix_sold = []

    for i in range(1, num_cus + 1):
        pq.enqueue("person_" + str(i))

    print("--- Show waiting customers ---")
    i = pq.size() - 1
    while i >= 0:
        print(pq.showqueue(i))
        i -= 1
    print("--- end ---\n")

    t_end = time.time() + till_show
    print("t_end", t_end)
    now = time.time()
    print("now", now)
    print("***", pq.size(), t_end - now)
    i = 0
    while now < t_end and not pq.is_empty():
        print("i = ", i)
        now = time.time()
        r = random.randint(0, max_time)
        time.sleep(r)
        person = pq.dequeue()
        print("{}, {} : {}".format(now, r, person))
        tix_sold.append(person)
        i += 1
        return tix_sold


if __name__ == '__main__':
    # def simulate_line(till_show, max_time, num_cus)
    # till_show : time until a move starts
    # max_time : maximum time that one person buy a ticket
    # num_cus : number of customers
    sold = simulate_line(5, 3, 120)
    print(sold)
