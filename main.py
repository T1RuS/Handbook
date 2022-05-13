import threading
from threading import Thread
from time import sleep
import random

time_list: list = [0 for _ in range(10)]


def useful_work(i):
    print(f'Выполняется полезная работа... \n Время работы {time_list[i]}, поток {threading.current_thread().name}')
    sleep(time_list[i])
    print(f'Полезная работа выполнена. {threading.current_thread().name}')


list_threads: list = [[random.randint(1, 10), 0, Thread(target=useful_work, args=(i,), name=str(i))] for i in range(10)]
# возможное исключение list_threads = [[1, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 0], [9, 0], [9, 0]]
list_threads.sort(key=lambda x: x[1])
print(list_threads)
min_priority: int = max(map(lambda x: x[0], list_threads))

for i in range(len(list_threads)):
    buf: list = []

    if list_threads[i][1] != 0:
        continue

    for j in range(10):
        if list_threads[i][0] == list_threads[j][0] and list_threads[j][1] == 0:
            buf.append(j)

    for j in buf:
        list_threads[j][0] = min_priority
        list_threads[j][1] = 60 // len(buf)

print(list_threads)


def processing_data() -> None:
    global list_threads
    all_time: int = 0

    for i in list_threads:
        all_time += i[1]

    print(all_time, 'Общее время работы.')

    max_time: list = []

    for i in list_threads:
        max_time.append(1 - i[1] / all_time)

    print(max_time, 'максимальное время работы')

    coeff: int = 0

    for i in max_time:
        coeff += i

    print(coeff, 'coeff')

    for i in range(10):
        list_threads[i][1] = max_time[i] / coeff * 60

    print(list_threads, 'возможно нормальное время работы')


while True:
    processing_data()
    count: int = 0
    for i in range(10):
        if not 5 < list_threads[i][1] < 7:
            count += 1

    if count == 0:
        break

print(list_threads, 'нормальное время')

for i in range(10):
    time_list[i] = list_threads[i][1]

for i in range(10):
    list_threads[i][2].start()

for i in range(10):
    list_threads[i][2].join()

