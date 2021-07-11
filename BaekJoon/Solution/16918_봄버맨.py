###########################################        
# test case
R, C = 6, 7
N = 2
map_ = [list('.......'),
        list('...O...'),
        list('.O..O..'),
        list('..O....'),
        list('OO.....'),
        list('OO.....')]

bombPosition = [list('.......'),
                list('...O...'),
                list('.O..O..'),
                list('..O....'),
                list('OO.....'),
                list('OO.....')]
###########################################

def bomb(map_, bombPos, R, C):
    # 새로운 폭탄 포지션
    newBombPos = map_.copy()
    
    for y in range(R):
        for x in range(C):
            if bombPos[y][x] == 'O':
                newBombPos[y][x] = '.'
                # 동
                if x+1 < C: 
                    newBombPos[y][x+1] = '.'
                # 서
                if x-1 >= 0:
                    newBombPos[y][x-1] = '.'
                # 남
                if y+1 < R:
                    newBombPos[y+1][x] = '.'
                # 북
                if y-1 >= 0:
                    newBombPos[y-1][x] = '.'
                    
    return (newBombPos, newBombPos)

def bomb_setting(R, C):
    return [['O' for x in range(C)] for y in range(R)]

def print_map(map_, R, C):
    for y in range(R):
        for x in range(C):
            print(map_[y][x], end='')
        print()

if __name__ == '__main__':
    # 입력값
    R, C, N = map(int, input().split())

    map_ = []
    bombPosition = [['.' for x in range(C)] for y in range(R)]
    for y in range(R):
        line = list(input())
        map_.append(line)
        for x in range(C):
            if map_[y][x] == 'O':
                bombPosition[y][x] = 'O'
    if N == 1:
        print_map(map_, R, C)
    
    else:

        time = 2
        # 반복
        while True:
            # 설치
            map_ = bomb_setting(R, C)
            time += 1
            if time > N: break
                
            # 펑
            map_, bombPosition = bomb(map_, bombPosition, R, C)
            time += 1
            if time > N: break

        print_map(map_, R, C)
        
########################################################################################################
#################################################방법 2#################################################
###############################################더 효율적?###############################################
# 계속 패턴이 반복되는 것을 확인
'''예시
.......    OOO.OOO    .......    OOOOOOO
...O...    O....OO    ...O...    OOOOOOO
.O..O..    ......O    .OOOO..    OOOOOOO
..O....    ....OOO    OOO....    OOOOOOO
OO.....    ...OOOO    OO.....    OOOOOOO
OO.....    ...OOOO    OO.....    OOOOOOO
'''

map_ = [list('.......'),
        list('...O...'),
        list('.O..O..'),
        list('..O....'),
        list('OO.....'),
        list('OO.....')]

bombPosition = [list('.......'),
                list('...O...'),
                list('.O..O..'),
                list('..O....'),
                list('OO.....'),
                list('OO.....')]


# def bomb(map_, bombPos, R, C):
#     # 새로운 폭탄 포지션
#     newBombPos = copy.deepcopy(map_)
    
#     for y in range(R):
#         for x in range(C):
#             if bombPos[y][x] == 'O':
#                 newBombPos[y][x] = '.'
#                 # 동
#                 if x+1 < C: 
#                     newBombPos[y][x+1] = '.'
#                 # 서
#                 if x-1 >= 0:
#                     newBombPos[y][x-1] = '.'
#                 # 남
#                 if y+1 < R:
#                     newBombPos[y+1][x] = '.'
#                 # 북
#                 if y-1 >= 0:
#                     newBombPos[y-1][x] = '.'
                    
#     return newBombPos

# def bomb_setting(R, C):
#     return [['O' for x in range(C)] for y in range(R)]

# def print_map(map_, R, C):
#     for y in range(R):
#         for x in range(C):
#             print(map_[y][x], end='')
#         print()

# if __name__ == '__main__':
#     import copy
#     # 입력값
#     R, C, N = map(int, input().split())

#     map_ = []
#     for y in range(R):
#         line = list(input())
#         map_.append(line)

#     state1 = map_
#     state2 = [['O' for x in range(C)] for y in range(R)]
#     state3 = bomb(state2, state1, R, C)
#     state4 = bomb(state2, state3, R, C)
    
#     if N == 1:
#         print_map(state1, R, C)
#     elif N % 2 == 0:
#         print_map(state2, R, C)
#     else:
#         if (N // 2) % 2 == 1:
#             print_map(state3, R, C)
#         else:
#             print_map(state4, R, C)