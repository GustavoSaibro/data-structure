from .node import Node
from typing import List

class LinkedList:

    def __init__(self, head: Node,nodes: List[Node] = None) -> None:
        self.nodes = nodes
        self.head = head
    
    def push(self, node: Node) -> Node:
        self.head.set_left(node)
        node.set_right(self.head)
        self.head = node
        
        return self.head
    
    def append(self, node: Node) -> Node:
        next: Node = self.head
        while next.get_right() != None:
            next = next.get_right()
        next.set_right(node)
        node.set_left(next)
        
        return self.head
        
    def insert_after(self, value: any, node: Node) -> Node:
        next: Node = self.head
        while next.get_right() != None or next.get_value != value:
            next = next.get_right()
        node.set_right(next.get_right())
        node.set_left(next)
        next.set_right(node)
        next = node.get_right()
        next.set_left(node)

        return self.head

    def search(self, value: any) -> Node:
        node: Node = self.head
        while node.get_value() != value:
            node = node.get_right()
        
        return node
    
    def recursive_search(self, value: any) -> Node:
        node: Node = self.head
        if node.get_value == value:
            return node
        return self.recursive_search(self,value, node.get_right())

    def sort(self,asc: bool = True) -> Node:
        
        return self.head
