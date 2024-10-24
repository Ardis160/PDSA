from collections.abc import Iterable
from typing import Union, Optional, TypeVar

T = TypeVar('T')


class Node:
    def __init__(self, value: Optional[T], next: Optional['Node'] = None):
        self.value = value
        self.next = next

    def add_after(self, node: 'Node'):
        node.next = self.next
        self.next = node

    def delete_after(self):
        self.next = self.next.next

    def __repr__(self):
        return f'Node({self.value}, {hex(id(self))}'

    def __str__(self):
        return repr(self)

class OurQueue:
    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head
        self.tail = self.head

    def enqueue(self, value: T):
        self.tail.add_after(Node(value))
        self.tail = self.tail.next

    def d_queue(self)-> T:
        val = self.head.next.value
        self.head.delete_after()
        return val

    @property
    def empty(self)->bool:
        return self.head.next is self.head

    def __bool__(self) ->bool:
        return self.empty

    def to_list(self)->list[T]:
        seznam= []
        while self.empty:
            seznam.append(self.d_queue())
        return seznam

    def note_iter(self)->Iterable[Node]:
        current = self.head.next
        while current is not self.head:
            yield current
            current = current.next


q = OurQueue()

for i in range(100):
    q.enqueue(i)
print("deg", q.d_queue())
for n in q.note_iter():
    print(n)
print("list", q.to_list())
