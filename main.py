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



def insert_line_at_five(file_path, new_line):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Stelle sicher, dass die Liste lang genug ist. Falls nicht, füge leere Zeilen hinzu.
    while len(lines) < 4:
        lines.append('\n')

    # Füge die neue Zeile bei Index 4 ein, was der fünften Zeile entspricht.
    lines.insert(4, new_line + '\n')

    with open(file_path, 'w') as file:
        file.writelines(lines)


## Schreibe binäre Daten in eine Datei
#st = "test"
#st.encode()
#file = open('beispiel.dat', 'wb')

#bytes_to_write = bytes([1,2,3,4,5,6,7,8,9])  # Eine Liste von Bytes

#file.write(bytes_to_write)
#
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
