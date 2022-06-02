from typing import List


def sort_process(processes: List[dict]):
    entry_vs_num = {}
    for num, dic in enumerate(processes):
        entry = list(dic.keys())[0]
        if entry in entry_vs_num:
            entry_vs_num[entry] = [entry_vs_num[entry], num]
        else:
            entry_vs_num[entry] = num

    entry_vs_num = {i: entry_vs_num[i] for i in sorted(entry_vs_num)}
    answer = []
    for i in entry_vs_num:
        if type(entry_vs_num[i]) == list:
            a = []
            for j in entry_vs_num[i]: a.append(list(processes[j].values())[0])
            for l, k in enumerate(sorted(a)):
                answer.append({
                    'NUM': entry_vs_num[i][l],
                    'ENTER': i,
                    'RUN': k
                })
            continue

        answer.append({
            'NUM': entry_vs_num[i],
            'ENTER': i,
            'RUN': list(processes[entry_vs_num[i]].values())[0]
        })

    return answer


if __name__ == '__main__':
    print(sort_process([{1: 10}, {5: 5}, {5: 12}, {1: 3}, {2: 3}]))