from 운영체제.process import sort_process

from typing import List

from pprint import pprint


def fifo_impl(processes: List[dict]):
    processes = sort_process(processes)
    count = 0
    for i in processes:
        i['WAIT'] = count
        while i['RUN'] != 0:
            i['RUN'] -= 1
            count += 1
        del i['RUN']
        i['FINISH'] = count

    return processes


if __name__ == '__main__': pprint(fifo_impl([{0: 3}, {2: 5}, {1: 2}, {0: 10}]))
