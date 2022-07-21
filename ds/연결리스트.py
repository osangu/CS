from typing import Optional


class DataAllReadyExistException(Exception):
    def __init__(self, data):
        super().__init__(data, 'ALREADY EXIST')


class Node:

    def __init__(self, data: int, next_node: Optional['Node'] = None):
        self.data = data
        self.__next_node = next_node

    @property
    def next_node(self) -> 'Node':
        return self.__next_node

    @next_node.setter
    def next_node(self, node: 'Node'):
        self.__next_node = node

    def __eq__(self, other):
        return isinstance(other, Node) and \
               self.data == other.data and \
               self.next_node == other.next_node


class LinkedList:

    def __init__(self, init_node: Node):
        self._init_node = init_node

    def push(self, node: Node):
        if self._is_smallest(node.data):
            node.next_node = self._init_node
            self._init_node = node
        else:
            before_node = self._find_before_node(node.data)
            if before_node.next_node is None:
                before_node.next_node = node
            else:
                node.next_node = before_node.next_node
                before_node.next_node = node

    def pop(self, index):
        if index == 0:
            return_node = self._init_node
            self._init_node = self._init_node.next_node
        elif index == self.node_amount:
            before_node = self._find_before_node_by_index(index)
            return_node = before_node.next_node
            before_node.next_node = None
        else:
            before_node = self._find_before_node_by_index(index)
            return_node = before_node.next_node
            before_node.next_node = before_node.next_node.next_node

        return return_node

    def show_all_node_data(self):
        print('=========================')
        run_node = self._init_node
        while True:
            print(run_node.data)
            if run_node.next_node is None: break
            run_node = run_node.next_node

    @property
    def node_amount(self):
        cnt, run_node = 1, self._init_node
        while True:
            if run_node.next_node is None: return cnt
            cnt += 1
            run_node = run_node.next_node

    def _find_before_node_by_index(self, index: int):
        run_node = self._init_node
        if index != 0:
            for i in range(index - 2):  # init node 제외로 -1 해당 인덱스 전의 node니 -1
                run_node = run_node.next_node
        return run_node

    def _find_before_node(self, data: int):
        run_node = self._init_node
        while True:
            if run_node.next_node is None: return run_node
            if run_node.next_node.data > data: return run_node
            if run_node.data == data: raise DataAllReadyExistException(data)
            run_node = run_node.next_node

    def _is_smallest(self, data) -> bool:
        return self._init_node.data > data


if __name__ == '__main__':
    linked_list = LinkedList(Node(3))

    linked_list.push(Node(1))

    linked_list.show_all_node_data()

    linked_list.push(Node(5))

    linked_list.show_all_node_data()

    linked_list.push(Node(4))

    linked_list.show_all_node_data()

    linked_list.push(Node(0))

    linked_list.show_all_node_data()

    linked_list.push(Node(7))

    linked_list.show_all_node_data()

    print('===')
    print(linked_list.pop(6).data)

    print('===')
    print(linked_list.pop(0).data)

    print('===')
    print(linked_list.pop(4).data)

    print('===')
    print(linked_list.pop(1).data)

    linked_list.show_all_node_data()
