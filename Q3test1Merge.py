class sort:
	def __init__(self, data):
		self.data = data
		self.next = None

class list:
	def __init__ (self):
		self.head =None
	def peeklist(self):
		items = self.head
		while items:
			print(items.data, end = "->")
			items = items.next
	def append(self,new_data):
		new_node = sort(new_data)
		if self.head is None:
			self.head = new_node
			return
		endnode = self.head
		while endnode.next:
			endnode = endnode.next
		endnode.next = new_node
def mergelists(h1, h2):
    items = None
    if h1 is None:
        return h2
    if h2 is None:
        return h1
    if h1.data <= h2.data:
        items = h1
        items.next = mergelists(h1.next, h2)
    else:
        items = h2
        items.next = mergelists(h1, h2.next)
    return items
#call the list object the  linter  and pass the values as mentioned in the question.
if __name__ =="__main__":
    list1 = list()
    list1.append(1)
    list1.append(4)
    list1.append(6)

    list2 = list()
    list2.append(2)
    list2.append(3)
    list2.append(5)
    list3= list()
    list3.head = mergelists(list1.head, list2.head)
    print("merged list",end ="")
    list3.peeklist()
