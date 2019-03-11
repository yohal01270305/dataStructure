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
    print("t_end =", round(t_end, 2))
    now = time.time()
    print("now   =", round(now, 2))
    print("t_end - now =", round(t_end, 2) - round(now, 2))
    i = 0
    while (now < t_end) and (not pq.is_empty()):
        print("i = ", i)
        now = time.time()   # get time now
        r = random.randint(0, max_time)
        time.sleep(r)
        person = pq.dequeue()
        print("{} -> {}".format(r, person))
        tix_sold.append(person)
        i += 1
        print("t_end =", round(t_end, 2))
        print("now   =", round(now, 2))
        print("size  =", pq.size())
        print(pq.is_empty())

    return tix_sold

if __name__ == '__main__':
    # def simulate_line(till_show, max_time, num_cus)
    # till_show : time until a move starts
    # max_time : maximum time that one person buy a ticket
    # num_cus : number of customers
    sold = simulate_line(10, 3, 120)
    for p in sold:
        print(p)
