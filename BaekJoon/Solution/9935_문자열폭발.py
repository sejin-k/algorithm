'''문제 접근 법
text = mirkovC4nizCC44
bombText = C4

mirko:v|C4|n:izCC44   -> || left, right,  ::Lrange, Rrange
'''
def check_around_words(text, bombText, idx):
    bombLen = len(bombText)
    # 폭발한 문자열의 범위
    left = idx
    right = idx + bombLen - 1
    
    while True:
        # 확인할 문자열의 범위
        Lrange = left - bombLen + 1
        Rrange = right + bombLen - 1
        # 양쪽으로 넘어갈 경우
        if Lrange < 0 and Rrange >= len(text):
            temp = text[:left] + text[right + 1:]
            Lrange, Rrange = 0, len(text) - 1
        # 오른쪽으로 넘어갈 경우
        elif Lrange >= 0 and Rrange >= len(text):
            temp = text[Lrange:left] + text[right + 1:]
            Rrange = len(text) - 1
        # 왼쪽으로 넘어갈 경우
        elif Lrange < 0 and Rrange < len(text):
            temp = text[:left] + text[right + 1:Rrange+1]
            Lrange = 0
        # 정상
        else:
            temp = text[Lrange:left] + text[right + 1:Rrange+1]

        temp_idx = temp.find(bombText)
        
        # 더이상 폭탄문자열이 없을 경우
        if temp_idx < 0:
            break

        # 폭탄문자열이 있을 경우
        pre_left = left
        pre_right = right
        left = Lrange + temp_idx
        right = left + (right - pre_left) + bombLen
    
    return left, right

if __name__=="__main__":
    # 입력값
    # text = input()
    # bombText = input()
    
    # test 입력
    text = "mirkovC4nizCC44"
    bombText = "C4"
    left = 0
    
    while True:
        idx = text[left:].find(bombText)
        if idx < 0:
            break
        idx = left + idx
        
        left, right = check_around_words(text, bombText, idx)
        text = text[:left] + text[right+1:]
    if len(text) == 0: print("FRULA")
    else: print(text)