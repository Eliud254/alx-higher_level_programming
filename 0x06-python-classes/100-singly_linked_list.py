#!/usr/bin/python3
"""The singly linked list"""

class Node:
    """ The class which  defines the node"""
    def __init__(self, data, next_node):
        self.__data = data
        self.__next_node = next_node
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an int')
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and vaue != None:
            raise TypeError('value must be a node object')

class SinglyLinkedList:
    def __init__(self):
        self.__head = None
