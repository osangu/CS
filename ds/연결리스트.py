from typing import Optional


class HeadNodeNotExistException(Exception):
    def __init__(self):
        super().__init__("ERROR: HEAD NODE DOESN'T EXIST")


class NextNodeNotExistException(Exception):
    def __init__(self, data):
        super().__init__(f"ERROR: NO NODE FOUND WITH DATA AFTER {data}")


class DataAllReadyExistException(Exception):
    def __init__(self, data):
        super().__init__(f'ERROR: NODE WHICH DATA IS {data} ALREADY EXIST')


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

    def __init__(self):
        self.__initial_node = None
        self.__iter_cnt = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.node_amount > self.__iter_cnt:
            now_node = self._find_node_by_index(self.__iter_cnt)
            self.__iter_cnt += 1
            return now_node

        else:
            self.__iter_cnt = 0
            raise StopIteration

    @property
    def _first_node(self) -> Node:
        if self.__initial_node is None: raise HeadNodeNotExistException
        return self.__initial_node

    @_first_node.setter
    def _first_node(self, node: Node):
        if self.__initial_node is None:
            self.__initial_node = node
        else:
            node.next_node = self.__initial_node
            self.__initial_node = node

    @property
    def node_amount(self) -> int:
        cnt, run_node = 1, self._first_node
        while True:
            if run_node.next_node is None: break
            cnt += 1
            run_node = run_node.next_node
        return cnt

    def push(self, node: Node):
        if self._is_smallest(node.data):
            self._first_node = node
        else:
            before_node = self._find_before_node_by_data(node.data)
            if before_node.next_node is None:
                before_node.next_node = node
            else:
                node.next_node = before_node.next_node
                before_node.next_node = node

    def _find_before_node_by_data(self, data: int):
        run_node = self._first_node
        while True:
            if (run_node.next_node is None) or (run_node.next_node.data > data): break
            run_node = run_node.next_node
        return run_node

    def _find_node_by_index(self, index: int):
        run_node = self._first_node
        for i in range(index):
            run_node = run_node.next_node
        return run_node

    def _is_smallest(self, data: int):
        global result
        try:
            result = self._first_node.data > data
        except HeadNodeNotExistException:
            result = True
        finally:
            return result
