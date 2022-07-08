def get_rec_fact(n):
    if n<0:
        return False
    elif n<2:
        return 1
    else:
        return n*get_rec_fact(n-1)

print(get_rec_fact(-4))