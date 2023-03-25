from __future__ import annotations

class Node:
    def __init__(self, value: any,left: Node = None, right: Node = None) -> None:
        self.left = left
        self.right = right
        self.value = value
    
    def get_left(self) -> Node:
        return self.left
    
    def get_right(self) -> Node:
        return self.right
    
    def get_value(self) -> any:
        return self.value

    def set_left(self, left) -> None:
        self.left = left

    def set_right(self, right) -> None:
        self.right = right
    
    def set_value(self, value) -> None:
        self.value=value