import memory_profile

@memory_profile.profile

def big_array():
    x = [1] * (10**5)
    y = [2] * (10**7)
    del y
    return x

if __name__ == '__main__':
    big_array()


#https://www.youtube.com/watch?v=FLp2SCNyhhg
