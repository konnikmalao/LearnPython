while True:
    try:
        x = int(input('Nhap so tu nhien thu nhat bat ki'))
        break
    except ValueError:
        print('Hay nhap lai so tu nhien thu nhat')

while True:
    try:
        y = int(input('Nhap so tu nhien thu hai bat ki'))
        break
    except ValueError:
        print('Hay nhap lai so tu nhien thu hai')

if x < y:
    for i in range(2, y//2 + 1):
        boi = x*i
        if boi % y == 0:
            print('Boi chung nho nhat cua hai so do la', boi)
            break
    else:
        print('Boi chung nho nhat cua hai so do la: ', x*y)
else:
    for i in range(2, x//2 + 1):
        boi = y*i
        if boi % y == 0:
            print('Boi chung nho nhat cua hai so do la', boi)
            break
    else:
        print('Boi chung nho nhat cua hai so do la: ', x * y)

