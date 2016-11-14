class Node(object):
    def __init__(self, value, next=None):
        self.next=next
        self.value=value

def reverse(node):
	if not node:
		return head
	previous = None

	while(node.next):
		next = node.next
		node.next = previous
		previous = node
		node = next

	return previous




def printList(node):
	while(node.next):
		print node.value
		node = node.next

def main():
	last = Node(3)
	head = Node(5, last)
	head = Node(8, head)
	head = Node(8, head)
	head = Node(8, head)
	head = Node(8, head)
	head = Node(2, head)
	head = Node(3, head)
	head = Node(3, head)

	# last.next = head
	printList(head)
	head = reverse(head)
	print "\n"
	printList(head)

if __name__ == '__main__':
	main()