import sys

def generate_input(test):
    input_list = []
    for line in test:
        line = line.replace("\n", "")
        input_list.extend([line])
    return input_list

def generate_bridge(input):
    tmp_list=[]
    for i in range(1,len(input)):
        s = input[i]
        tmp_list.append([x for x in range(int(s.split(' ')[0]),int(s.split(' ')[1])+1)])
    return tmp_list

def generate_start_end(input):
    start = 0
    end = len(input)-1
    return start,end

def generate_graph(input):
    graph = {}
    for i in range(len(input)):
        a = set(input[i])
        tmp_value = []
        for j in range(len(input)):
            b = set(input[j])
            if len(a.intersection(b)) > 1 and i<j :
                tmp_value.append(j)
            else:
                pass
        if len(tmp_value)!=0:
            graph[i] = tmp_value
    return graph

def bfs_pace(graph,start,end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return len(path)-1
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

def bfs_paths(graph,start,end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == end:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def shortest_path(graph,start,end):
    try:
        return next(bfs_paths(graph,start,end))
    except StopIteration:
        return None

def bfs_shortest_path(graph, start, end):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
     # return path if start is goal
    if start == end:
        return "Start = goal"
     # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == end:
                    return new_path
             # mark node as explored
            explored.append(node)
    # in case there's no path between the 2 nodes
    return "connecting path doesn't exist"


def main(test):
    input_list = generate_input(test)
    bridge_list = generate_bridge(input_list)
    jump_graph = generate_graph(bridge_list)
    start,end = generate_start_end(bridge_list)
    # path = bfs_shortest_path(jump_graph, start, end)
    # path = shortest_path(jump_graph,start,end)
    # pace = len(path)-1
    pace = bfs_pace(jump_graph,start,end)
    # print(start,end)
    # print(input_list)
    # print(bridge_list)
    # print(start,end)
    # print(jump_graph)
    # print(path)
    print(pace)

input = open(r'input.txt')
# input = sys.stdin
main(input)
