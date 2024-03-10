class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def setNext(self, n):
        self.next = n


class LinkedList:
    def __init__(self):
        self.head: Node = None

    def cons(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = Node(data)
        return

    def deleteAt(self, pos):
        run = self.head
        tmp = run
        if pos == 1:
            self.head = self.head.next
        while pos != 1:
            pos -= 1
            tmp = run
            run = run.next
        tmp.next = run.next

    def insertAt(self, pos:int, data):
        if pos == 1:  # Ein neuer Knoten soll am Anfang eingefügt werden
            self.cons(data)
            return
        new_node = Node(data)
        current = self.head
        count = 1
        while current is not None and count < pos - 1:
            current = current.next
            count += 1
        if current is None:
            print("Position ist außerhalb der Liste.")
            return
        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

def main():
    l = LinkedList()
    f = open("data.txt", "r")
    for x in f:
        l.append(x.strip())
    while(True):
        print("Dateinhalt:  ")
        l.print_list()
        i = input("Eingabe: [a] exit, [i] insert, [e] edit, c [append]")
        if (i == "a"):
            break
        elif(i == "i"):
            pos = input("Position: ")
            text = input("Text:")
            l.insertAt(int(pos),text)
        elif(i == "e"):
            pos = input("Position: ")
            text = input("Text:")
            l.insertAt(int(pos),text)
            l.deleteAt(int(pos)+1)
        elif(i == "c"):
            text = input("Text: ")
            l.append(text)




main()
