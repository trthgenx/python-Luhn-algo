import random
from colored import fg



colorg = fg('green')
colorr = fg('red')



code = ''

n1 = random.randint(0,9)
n2 = random.randint(0,9)
n3 = random.randint(0,9)
n4 = random.randint(0,9)
n5 = random.randint(0,9)
n6 = random.randint(0,9)
n7 = random.randint(0,9)
n8 = random.randint(0,9)
n9 = random.randint(0,9)
n10 = random.randint(0,9)
n11 = random.randint(0,9)
n12 = random.randint(0,9)
n13 = random.randint(0,9)
n14 = random.randint(0,9)
n15 = random.randint(0,9)
n16 = random.randint(0,9)


def create_code():
    temp_code = str(n1)+str(n2)+str(n3)+str(n4)+str(n5)+str(n6)+str(n7)+str(n8)+str(n9)+str(n10)+str(n11) + str(n12) + str(n13) + str(n14) + str(n15) + str(n16)
    #print(temp_code)

    n15x = n15 * 2
    if (len(str(n15x)) == 2 ):
        n15x1 = str(n15x)[0]
        n15x2 = str(n15x)[1]
        final_n15 = int(n15x1) + int(n15x2)
        #print(final_n15)
        l = list(temp_code)
        l[14] = str(final_n15)
        newt = ''.join(l)
        #print(newt)
    else:
        n15r = n15x
        #print(n15r)
        l = list(temp_code)
        l[14] = str(n15r)
        newt = ''.join(l)
        #print(newt)

    n13x = n13 * 2
    if (len(str(n13x)) == 2):
        n13x1 = str(n13x)[0]
        n13x2 = str(n13x)[1]
        final_n13 = int(n13x1) + int(n13x2)
        #print(final_n13)
        l = list(newt)
        l[12] = str(final_n13)
        newt2 = ''.join(l)
        #print(newt2)
    else:
        n13r = n13x
        #print(n13r)
        l = list(newt)
        l[12] = str(n13r)
        newt2 = ''.join(l)
        #print(newt2)

    n11x = n11 * 2
    if (len(str(n11x)) == 2):
        n11x1 = str(n11x)[0]
        n11x2 = str(n11x)[1]
        final_n11 = int(n11x1) + int(n11x2)
        #print(final_n11)
        l = list(newt2)
        l[10] = str(final_n11)
        newt3 = ''.join(l)
        #print(newt3)
    else:
        n11r = n11x
        #print(n11r)
        l = list(newt2)
        l[10] = str(n11r)
        newt3 = ''.join(l)
        #print(newt3)

    n9x = n9 * 2
    if (len(str(n9x)) == 2):
        n9x1 = str(n9x)[0]
        n9x2 = str(n9x)[1]
        final_n9 = int(n9x1) + int(n9x2)
        #print(final_n9)
        l = list(newt3)
        l[8] = str(final_n9)
        newt4 = ''.join(l)
        #print(newt4)
    else:
        n9r = n9x
        #print(n9r)
        l = list(newt)
        l[8] = str(n9r)
        newt4 = ''.join(l)
        #print(newt4)

    n7x = n7 * 2
    if (len(str(n7x)) == 2):
        n7x1 = str(n7x)[0]
        n7x2 = str(n7x)[1]
        final_n7 = int(n7x1) + int(n7x2)
        #print(final_n7)
        l = list(newt4)
        l[6] = str(final_n7)
        newt5 = ''.join(l)
        #print(newt5)
    else:
        n7r = n7x
        #print(n7r)
        l = list(newt4)
        l[6] = str(n7r)
        newt5 = ''.join(l)
        #print(newt5)

    n5x = n5 * 2
    if (len(str(n5x)) == 2):
        n5x1 = str(n5x)[0]
        n5x2 = str(n5x)[1]
        final_n5 = int(n5x1) + int(n5x2)
        #print(final_n5)
        l = list(newt5)
        l[4] = str(final_n5)
        newt6 = ''.join(l)
        #print(newt6)
    else:
        n5r = n5x
        #print(n5r)
        l = list(newt5)
        l[4] = str(n5r)
        newt6 = ''.join(l)
        #print(newt6)

    n3x = n3 * 2
    if (len(str(n3x)) == 2):
        n3x1 = str(n3x)[0]
        n3x2 = str(n3x)[1]
        final_n3 = int(n3x1) + int(n3x2)
        #print(final_n3)
        l = list(newt6)
        l[2] = str(final_n3)
        newt7 = ''.join(l)
        #print(newt7)
    else:
        n3r = n3x
        #print(n3r)
        l = list(newt6)
        l[2] = str(n3r)
        newt7 = ''.join(l)
        #print(newt7)

    n1x = n1 * 2
    if (len(str(n1x)) == 2):
        n1x1 = str(n1x)[0]
        n1x2 = str(n1x)[1]
        final_n1 = int(n1x1) + int(n1x2)
        #print(final_n1)
        l = list(newt7)
        l[0] = str(final_n1)
        newt8 = ''.join(l)
        #print(newt8)
    else:
        n1r = n1x
        #print(n1r)
        l = list(newt7)
        l[0] = str(n1r)
        newt8 = ''.join(l)
        #print(newt8)


    code = newt8
    lcode = list(code)

    fn1 = int(lcode[0])
    fn2 = int(lcode[1])
    fn3 = int(lcode[2])
    fn4 = int(lcode[3])
    fn5 = int(lcode[4])
    fn6 = int(lcode[5])
    fn7 = int(lcode[6])
    fn8 = int(lcode[7])
    fn9 = int(lcode[8])
    fn10 = int(lcode[9])
    fn11 = int(lcode[10])
    fn12 = int(lcode[11])
    fn13 = int(lcode[12])
    fn14 = int(lcode[13])
    fn15 = int(lcode[14])
    fn16 = int(lcode[15])


    sum = fn1+fn2+fn3+fn4+fn5+fn6+fn7+fn8+fn9+fn10+fn11+fn12+fn13+fn14+fn15+fn16

    if(sum % 10 == 0):
        print(colorg + 'valid')
        print()
        print(colorg + 'CODE : ' + temp_code)
    else:
        print(colorr + 'invalid')








if __name__ == '__main__':
    create_code()
