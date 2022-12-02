class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


# 6 tugun yaratamiz va boglaymiz


# node_1 = Node(1)
# node_2 = Node(2)
# node_3 = Node(3)
# node_4 = Node(4)
# node_5 = Node(5)
# node_6 = Node(6)
#
# node_1.next = node_2
# node_2.next = node_3
# node_3.next = node_4
# node_4.next = node_5
# node_5.next = node_6
#
# while node_1:
#     print(node_1.data, end=' ')
#     node_1 = node_1.next


a = [1, 2, 3, 4, 5, 6, 7]
head = None
tmp = head
for i in a:
    head = Node(i, head)
    # print(i, end=' ')

while head:
    print(head.data, end=' ')
    head = head.next
