class Node:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node


def tab_to_list(tab):
    if len(tab) == 0:
        return None
    r = Node(tab[0])
    guardian = Node(0, r)
    for i in range(1, len(tab)):
        temp = Node(tab[i])
        r.next = temp
        r = r.next
    return guardian.next


def list_to_str(first):
    if first is None:
        return "None"
    msg = ""
    while first is not None:
        msg += str(first.val) + " --> "
        first = first.next
    msg += "None"
    return msg
