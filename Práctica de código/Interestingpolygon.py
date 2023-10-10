def interesting_polygon(n):
    if n == 1:
        return 1
    return n**2 + (n-1)**2
            
num = 3
print(interesting_polygon(num))