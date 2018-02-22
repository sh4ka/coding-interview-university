def pascal_triangle (n):
    pt = [[] for x in range(n)]
    for i in range(0, n):
        pt[i] = [1 for x in range(0, i+1)]
        pt[i][0] = 1
        for j in range(1, i):
            pt[i][j] = pt[i-1][j-1] + pt[i-1][j]
    print(pt)

if __name__ == '__main__':
    import sys
    n = int(sys.argv[1:][0]) # first argument, discard the rest
    pascal_triangle(n)