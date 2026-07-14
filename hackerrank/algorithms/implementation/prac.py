def kangaroo(x1, v1, x2, v2):
    v1v2 = v1 * v2
    v1_v2_can_divide = v1v2 % v1 == 0 and v1v2 % v2 == 0
    
    if x2 > x1 and v2 > v1:
        return "NO"
    if x1 > x2 and v1 > v2:
        return "NO"
    elif v1_v2_can_divide:
        return "YES"

print(kangaroo(21, 6, 47, 3)) # NO

27 33 39 45 51 56 62 68 
49 52 55 58 61 64 67 70
