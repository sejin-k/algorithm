def remove_group(map_, group):    
    # 연쇄반응 제거
    for x, y in group:
        map_[y][x] = '.'
    
        
def reposition(map_):
    stack = []
    
    for x in range(w):  # 한 열씩 검사
        for y in range(h):
            if map_[y][x] != '.':  # 아래에서 위로 올라가면서 .이 아닌경우에 stack에 저장
                stack.append(map_[y][x])
        
        for y in range(h-1, -1, -1):  # 재배열 시작
            if len(stack) > 0:
                map_[y][x] = stack.pop()
            else:
                map_[y][x] = '.'
    
        
def checking(map_, x, y, color, group):
    # 들어왔을 경우 마킹
    marking[y][x] = 1
    group.append((x,y))
    
    # 네방향으로 이동하면서 확인
    # 동
    if x+1 < w and map_[y][x+1] == color and marking[y][x+1] == 0:
        checking(map_, x+1, y, color, group)
    # 서
    if x-1 >= 0 and map_[y][x-1] == color and marking[y][x-1] == 0:
        checking(map_, x-1, y, color, group)
    # 남
    if y+1 < h and map_[y+1][x] == color and marking[y+1][x] == 0:
        checking(map_, x, y+1, color, group)
    # 북
    if y-1 >= 0 and map_[y-1][x] == color and marking[y-1][x] == 0:
        checking(map_, x, y-1, color, group)
if __name__=='__main__':
    w, h = 6, 12
    
    # 초기값 입력
    map_ = []
    for i in range(h):
        map_.append(list(input()))
    chain_num = 0
    while True:  # 연쇄반응이 있을 경우
        # 필요 변수 선언
        marking = [[0 for i in range(w)] for j in range(h)]
        color_groups = []
        
        for y in range(h):
            for x in range(w):
                # 확인 안했으면 확인
                color = map_[y][x]
                if color != '.' and marking[y][x] == 0:
                    group = []  # 붙어있는 같은 색 위치 리스트
                    checking(map_, x, y, color, group)
                    if len(group) >= 4:
                        color_groups.append(group)
        # 연쇄 반응이 없을 경우 종료
        if len(color_groups) == 0:
            break
        # 연쇄반응 있을 경우 제거
        else:
            chain_num += 1
            for group in color_groups:
                remove_group(map_, group)
            # puyo 재배열
            reposition(map_)
    print(chain_num)