def solution(inputArray):
  
    if len(inputArray) == 0:
        print(0)
    else:
        result1 = []
        for i in range(len(inputArray)-1):    
            result1.append(inputArray[i] * inputArray[i+1]) 
        return max(result1)
        
array = [5, 6, -2, -5, 7, 3]

print(solution(array))