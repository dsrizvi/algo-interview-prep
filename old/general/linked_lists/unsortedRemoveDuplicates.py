class Node(object):
    def __init__(self, value, next=None):
        self.next=next
        self.value=value

def removeDuplicates(node):
	seen = set()
	if not node:
		return None

	seen.add(node.value)

	while node.next and node.next.next:
		seen.add(node.value)
		if node.next.value in seen:
			node.next = node.next.next
		# else:
		node = node.next

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
	# removeDuplicates(head)
	printList(head)

if __name__ == '__main__':
	main()