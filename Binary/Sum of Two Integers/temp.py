def getSum(a=-6, b=30):
    a_string = bin(a & 0xFFF)[2::][::-1]
    b_string = list(bin(b & 0xFFF)[2::][::-1])
    for _ in range(12-len(b_string)):
        b_string.append('0')

    def add_rev_strings(a_string, b_string):
        for i, bit in enumerate(a_string):
            if bit == '1':
                if b_string[i] == '0':
                    b_string[i] = '1'
                else:
                    for j in range(i, len(b_string)):
                        if b_string[j] == '0':
                            b_string[j] = '1'
                            break
                        else:
                            b_string[j] = '0'
        return b_string

    b_string = add_rev_strings(a_string, b_string)

    if b_string[-1] == '1':  # negative
        b_string = add_rev_strings('111111111111', b_string)
        b_string = b_string[::-1]
        b_string = ''.join(['0b', *b_string])
        b_string = -(int(b_string, 2) ^ 0xFFF)
    else:
        b_string = b_string[::-1]
        b_string = ''.join(['0b', *b_string])
        b_string = int(b_string, 2)

    return b_string
