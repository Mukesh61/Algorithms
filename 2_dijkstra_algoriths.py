"""
Min distance or min cost finding algorith, we start with initial assumpation of point_a -> point_b as infinite cost, then check if in any route cost is lower than initial cost. <cost_table = {i:INF for i in graph.keys()}>
keep updating the cost table if current cost is less then previous one. <if cost + parent_cost < current_cost:>

if travelling like x -> y -> z
cost of x -> z in above case will be x -> y + y -> z

u->v : 6, u->w:7
v->u : 6, v->x:10
w->u : 7, w->x:1
x->w : 1, x->v:10
"""
graph = {
    "u":{"v":6, "w":7},
    "v":{"u":6,"x":10},
    "w":{"u":7, "x":1},
    "x":{"w":1, "v":10}
}

INF = float('infinity')
cost_table = {i:INF for i in graph.keys()}
unvisited = ["u"]
cost_table["u"] = 0

print(f"Initial cost table: {cost_table}")
visited = []

while unvisited:
    unvisited_item = unvisited.pop()
    print(f"pop item from unvisited {unvisited_item}")

    parent_cost = cost_table.get(unvisited_item)
    visited.append(unvisited_item)

    neighbour = graph.get(unvisited_item)
    if neighbour:
        for item, cost in neighbour.items():
            print(f"checking neighbour: {item}")
            current_cost = cost_table.get(item)
            if cost + parent_cost < current_cost:
                cost_table[item] = cost + parent_cost
            if item not in visited:
                unvisited.append(item)
    print(cost_table)

