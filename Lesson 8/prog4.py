def CN(W, H):
    return W / (H * H)
def ON(n):
    if n < 18.5:
        return('Недостаточный вес')
    if 18.5 < n < 25:
        return('ИМТ в норме')
    if n > 25:
        return('Избыточный вес')
We = int(input())
Hi = int(input())
print(ON(CN(We, Hi)))