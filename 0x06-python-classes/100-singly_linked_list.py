#!/usr/bin/python3

""" The module docstring
"""


class Node:
    """Class of each node inside the whole list
    """
    def __init__(self, data, next_node=None):
        """ Initialize the class attributes

        Args:
            data (int): The data inside each node
            next_node (Node, optional): The reference to the next node.
            Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ The data setter
            The getter checks wether the data is integer before accept it
            otherwise raise an TypeError with a particular message

        Returns:
            int: The content of the data attribute
        """
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Next node setter
            Getter is checking wether the next_node attribute is of type
            Node before accepts it, either way raises a TypeError with a
            particular error message

        Returns:
            Node: The next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """ Class of the whole singly linked list
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """ Insert a value to the list with the sorted order
            smaller to bigger

        Args:
            value (int): The value of the new added node
        """
        new_node = Node(value, None)
        if self.__head is None:
            self.__head = new_node
            return
        if self.__head.next_node is None:
            if value < self.__head.data:
                new_node.next_node = self.__head
                self.__head = new_node
                return
            else:
                self.__head.next_node = new_node
                return
        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current_node = self.__head.next_node
        prev_node = self.__head
        while prev_node.next_node:
            if value < current_node.data:
                prev_node.next_node = new_node
                new_node.next_node = current_node
                return
            prev_node = current_node
            current_node = current_node.next_node
        prev_node.next_node = new_node
        return

    def __str__(self):
        """ Return the string output of the linked list

        Returns:
            str: The singly linked list string output
        """
        output = ""
        current_node = self.__head
        while current_node:
            output += str(current_node.data) + "\n"
            current_node = current_node.next_node

        return output[:-1]
