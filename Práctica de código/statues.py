def solution(statues):
    statues.sort()
    result = 0
    for i in range(len(statues)-1):
        diferencia = statues[i+1] - statues[i] 
        if diferencia > 1:
            result += diferencia - 1
    
    return result
        

            





arreglo = [6,3,2,8,10,20]

print(solution(arreglo))        