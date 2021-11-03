import multiprocessing as mp
import time


def print_in(text, wait_time):
    count = 0

    while count < wait_time:
        count = count + 1
        print(f'[{text}] ellapsed {count} seconds')
        time.sleep(1)


def sequencial_processing():
    print_in('subprocess 1', 3)
    print_in('subprocess 2', 5)
    print_in('subprocess 3', 10)


def processing(text, seconds):
    print_in(text, seconds)


def parallel_processing():
    pool = mp.Pool(mp.cpu_count())

    data = [
        {'text': 'subprocess 1', 'seconds': 3},
        {'text': 'subprocess 2', 'seconds': 5},
        {'text': 'subprocess 3', 'seconds': 10}
    ]
    pool.starmap(processing, [(item['text'], item['seconds']) for item in data])


if __name__ == '__main__':
    strategy = input("Digite 1 para sequencial e 2 para paralelo: ")

    if strategy == '1':
        sequencial_processing()
    else:
        parallel_processing()
