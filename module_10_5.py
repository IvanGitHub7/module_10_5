import time
import multiprocessing

all_data = []
def read_info(name):
    with open(name, 'r', encoding = 'utf-8') as file:
        all_data.append(file.readlines())

if __name__ == '__main__':

    a = int(input('Выберите способ выполнения программы (1 - линейный метод,'
                  ' 2 - многопроцессный метод) '))
    all_files = []
    for i in range(1, 5):
        all_files.append(f'./file {i}.txt')

    if a == 1:
        start = time.time()
        for file_ in all_files:
            read_info(file_)
        end = time.time()
        print('Время выполнения кода линейным методом:', end - start)
    elif a == 2:
        start = time.time()
        with multiprocessing.Pool(processes=12) as pool:
            pool.map(read_info, all_files)
        end = time.time()
        print('Время выполнения кода многопроцессным методом:', end - start)