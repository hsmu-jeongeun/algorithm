def solution(a, b):    
    large = b
    small = a
    
    if a - b > 0 :
        large = a
        small = b
        
    answer = sum(range(small, large + 1))
    return answer