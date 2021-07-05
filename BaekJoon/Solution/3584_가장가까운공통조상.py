# input 설정
n = int(input())
trees = []
test_case = []
node_nums = []
for i in range(n):
    node_num = int(input())
    nodes = []
    for j in range(node_num - 1):
        nodes.append(tuple(map(int, input().split())))
    trees.append(nodes)
    test_case.append(list(map(int, input().split())))
    node_nums.append(node_num)
    
# tree link를 dict로 만들기
tree_dicts = []
for tree in trees:
    tree_dict = {}
    for link in tree:
        tree_dict[link[1]] = link[0]
    tree_dicts.append(tree_dict)

def close_ancestor(link_dict, nodes):
    familyTrees = []
    for node in nodes:
        familyTree = [node]
        current = node
        while(1):
            try:
                current = link_dict[current]
                if current in familyTree: break
                familyTree.append(current)
            except:
                break
        familyTrees.append(familyTree)
        
    for i in range(1, len(familyTrees[0]) + 1):
        if familyTrees[0][-i:] != familyTrees[1][-i:]:
            return familyTrees[0][-(i-1)]
        
    return familyTrees[0][0]

for i in range(n):
    print(close_ancestor(tree_dicts[i], test_case[i]))