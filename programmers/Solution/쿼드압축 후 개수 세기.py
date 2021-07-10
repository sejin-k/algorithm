# 영역안의 숫자가 같은 숫자인지 확인하는 함수
def all_same(square):
    size = len(square)
    
    # 숫자 1개일 경우
    if size == 1:
        return (True, square[0][0])
    
    # 값 정하기
    if sum(square[0]) not in [0, size]:
        return (False, -1)
    else:
        if sum(square[0]) == 0:
            value = 0
        else:
            value = size
    
    for line in square[1:]:
        if sum(line) != value:
            break
    else:
        # 모두 같을 경우
        return (True, square[0][0])
    
    # 다른 것이 있어서 break일 경우
    return (False, -1)

#     # 한개씩 검사하는 방법
#     value = square[0][0]
    
#     for i in range(size):
#         for j in range(size):
#             if square[i][j] != value:
#                 return (False, -1)
#     return (True, square[0][0])

# 4개 영역으로 분할 함수
def quad_split(square):
    size = len(square)
    split_size = size//2
    s1, s2, s3, s4 = [], [], [], []
    
    # 왼쪽 위 영역
    for i in range(size//2):
        s1.append(square[i][:split_size])
    # 오른쪽 위 영역
    for i in range(size//2):
        s2.append(square[i][split_size:])
    # 왼쪽 아래 영역
    for i in range(size//2, size):
        s3.append(square[i][:split_size])
    # 오른쪽 아래 영역
    for i in range(size//2, size):
        s4.append(square[i][split_size:])

    return (s1, s2, s3, s4)
    
    
def run(arr, ans):    
    same, value = all_same(arr)
    
    if same:
        # 한개로 묶기
        ans[value] += 1
    else:
        # 분할
        s1, s2, s3, s4 = quad_split(arr)
        run(s1, ans)
        run(s2, ans)
        run(s3, ans)
        run(s4, ans)
        
def solution(arr):
    answer = [0, 0]
    
    run(arr, answer)
    
    return answer


if __name__=='__main__':
    arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
    ans = solution(arr)
    
    print(ans)