class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next



def split_list(head):
    """按照奇偶位拆分为两个链表"""
    head1 = head2 = None
    cur1 = cur2 = None
    count = 1
    while head:
        if count % 2 == 1:
            if cur1:
                cur1.next = head
                cur1 = cur1.next
            else:
                cur1 = head1 = head
        else:
            if cur2:
                cur2.next = head
                cur2 = cur2.next
            else:
                cur2 = head2 = head
        head = head.next
        count += 1
    cur1.next = None
    cur2.next = None
    return head1, head2

def reverse_list(head):
    """反转链表"""
    if not head or not head.next:
        return head
    pre = next = None
    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre

def merge_list(head1, head2):
    """合并两个递增链表"""
    head = Node()  # 设置一个临时结点
    tail = head
    while head1 and head2:
        if head1.val <= head2.val:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    # 合并剩余结点
    if head1:
        tail.next = head1
    if head2:
        tail.next = head2
    return head.next
