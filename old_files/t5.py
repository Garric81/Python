abcd = int(input())
a = abcd // 1000
b = (abcd % 1000) // 100
c = (abcd % 100) // 10
d = abcd % 10
if  a + d == b - c:
    print('Да')
else:
    print('НЕТ')