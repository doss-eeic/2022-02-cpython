def double_tensor_element(tensor, idx):
    idx = tuple(idx)
    ndim = len(idx)
    a = tensor
    for dim, i in enumerate(idx, 1):
        if dim == ndim:
            # reference of target element
            a[i] *= 2
        else:
            # depth  +1
            a = a[i]
    
    """
    tensor[idx] *= 2
    """


if __name__ == "__main__":
    idx = (1, 2, 1)
    ls = [[[0] * 3 for _ in range(3)] for _ in range(3)]
    num = 0
    i = 100
    for i in range(3):
        for j in range(3):
            for k in range(3):
                ls[i][j][k] = num
                num += 1
    before = ls[1][2][1]
    
    double_tensor_element(ls, idx)
    print(ls)
    
    assert ls[1][2][1] == before * 2