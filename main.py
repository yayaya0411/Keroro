def generate_input(input):
    input = []
    with  open('input.txt','r', encoding='utf-8') as f:
        input = (f.readlines())
    input_list = [x.strip() for x in input]
    return input_list

input = 'input.txt'
input_list = generate_input(input)
input_list

def generate_bridge(input):
    tmp_list=[]
    for i in range(1,len(input)):
        s = input[i]
        tmp_list.append([x for x in range(int(s.split(' ')[0])+1,int(s.split(' ')[1]))])
        # graph['{}'.format(counter)] =
    return tmp_list

bridge_list = generate_bridge(input_list)
bridge_list
# def generate_graph(input)
for i in bridge_list:

couonter = 0
graph = {}


def generate_graph(input):
    return

generate_graph(input)
print()

# graph is in adjacent list representation
graph = {
        'A': ['D', 'F'],
        'B': ['E', 'G', 'H'],
        'C': ['D', 'F', 'G'],
        'D': ['F', 'G' ],
        'E': ['H'],
        'F': ['G'],
        'G': ['H']
        }

def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        print(path,node)
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

# print(len(bfs(graph, 'A', 'H'))-1)
