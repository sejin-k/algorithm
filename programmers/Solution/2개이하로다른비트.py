def solution(numbers):
    answer = []
    for num in numbers:
        num_li = list(format(num, 'b'))
        # 0인 경우
        if num == 0:
            answer.append(1)
            
        # 2진법이 모두 1로 되어있을 경우
        elif len(set(num_li)) == 1:
            answer.append((2*(num+1) - 1) - (num+1)//2)
            
        else:
            check = -1
            # 맨 뒤에서부터 최초0인부분을 찾아 1로 바꾸기(최대한 작게 키우고)
            for i in range(len(num_li)-1, 0, -1):
                if num_li[i] == '0':
                    num_li[i] = '1'
                    check = i
                    break
            # 1로 바꾼 위치 다음부터 최초 1인부분을 0으로 바꾸기(최대한 크게 줄이자)
            for i in range(check+1, len(num_li)):
                if num_li[i] == '1':
                    num_li[i] = '0'
                    break
            answer.append(int("".join(num_li), 2))
                    
    return answer
        

if __name__=='__main__':
    numbers = [1,2,3,4,5,6,7,8,9,10]
    result = solution(numbers)
    print(result)
    
'''
11111 -> 101111

11011 -> 11101

'''