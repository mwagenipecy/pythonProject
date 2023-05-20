
def sort_element(numbers):
    for _ in range(len(numbers ) -1):
        for i in range(len(numbers ) -1):
            if numbers[i ]> numbers[ i +1]:
                numbers[ i +1] ,numbers[i ] =numbers[i], numbers[ i +1]
    print( 6//2)
    return print( numbers)


numbers =[4 ,2 ,4 ,6 ,1 ,4 ,9 ,0 ,2 ,304 ,4 ,5 ,6 ,6 ,7 ,9]
print(range(len(numbers)))
mid =len(numbers )//2
left =numbers[:mid]
right =numbers[mid:]
data =[67 ,34]
sort_element(numbers)

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def parse_tuple(data, space="\t" ,level=1):
        print('data', data)
        if isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode(data[0])
            node.right = TreeNode(data[2])

        else:
            node = [12 ,3 ,4 ,5]
            print(1)
            print(space *(- 1 *level )+ str(2 )+ space *level + str(2))
            print(space *(- 2 *level )+ str(3 )+ space *( 1 +level) + str(3))
            print(space *(- 3 *level )+ str(4 )+ space *( 2 +level) + str(4))
        return [x for x in node if x is  None ]


tree_pulse = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
var = TreeNode(tree_pulse)
print(var.parse_tuple())

def get_the_self_tree(data):
    global node
    if data is None:
        node = None
        print("hello  it is nothing to show now")

    elif len(data) == 3 and data is tuple:
        key_value = int(input('enter the key value'))
        if key_value in data:
            node = data[1]
            node.left = data[0]
            node.right = data[2]
        return print(node.right)


print(get_the_self_tree((6, 7, 8)))

var = TreeNode(tree_pulse[0])
print(len(tree_pulse), tree_pulse[0])
var.parse_tuple()
