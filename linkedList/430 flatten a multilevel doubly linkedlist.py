stack = [head]
dummyNode = ()
dummyNode.next = head
p = dummyNode
while stack:
    node = stack.pop()
    node.prev = p
    p.next = node
    if node.next:
        stack.append(node.next)
        node.next = None
    if node.child:
        stack.append(node.child)
        node.child = None
    p = node
dummyNode.next.prev = None
return dummyNode.next



