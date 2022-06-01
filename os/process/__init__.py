import pprint
from typing import List


def sort_dict_in_list(process_list: List[dict]):
    entry_vs_num = {}

    for num, j in enumerate(process_list):
        entry = list(j.keys())[0]

        if entry in entry_vs_num:
            entry_vs_num[entry] = sorted([entry_vs_num[entry], num + 1])
            continue

        entry_vs_num[entry] = num + 1
    entry_vs_num = {i: entry_vs_num[i] for i in sorted(entry_vs_num)}
    answer = []

    for i in entry_vs_num:
        if type(entry_vs_num[i]) == list:
            a = []
            for j in entry_vs_num[i]:
                a.append(list(process_list[j - 1].values())[0])
            answer.append({i: sorted(a)})
            continue

        answer.append(
            {i: list(process_list[entry_vs_num[i] - 1].values())[0]}
        )
    print(answer)


if __name__ == '__main__': sort_dict_in_list([{1: 10}, {8: 5}, {5: 12}, {1: 3}])
