n = int(input())

stack = [1]
            
def DFS(stack):
    go = check(stack)
    if go == -1:
        stack.pop()
        return -1
    elif go == 1:
        # 최종 길이와 같은지 검사
        if len(stack) == n:
            return 1
        # 1을 추가
        stack.append(1)
        DFS(stack)
        if len(stack) == n:
            return 1
        # 2을 추가
        stack.append(2)
        DFS(stack)
        if len(stack) == n:
            return 1
        # 3을 추가
        stack.append(3)
        DFS(stack)
        if len(stack) == n:
            return 1
        # 없을경우 pop하고 return
        stack.pop()
        return -1
    
    
def check(stack):
    '''연속되는 부분문자열에서 같은 것이 있는지 검색'''
    for i in range(1, 1 + (len(stack) // 2)):
        cur = stack[-i:]
        pre = stack[-2*i:-i]
        if cur == pre: return -1
    else:
        return 1
    
DFS(stack)
result = int("".join(map(str,stack)))
print(result)