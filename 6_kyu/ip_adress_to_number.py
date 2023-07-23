def ip_to_num(ip):
    numbers = ip.split(".")
    num = []
    for i in range(len(numbers)):
        quotient = int(numbers[i])
        nb_binary = []
        while(quotient != 0):
            nb_binary.insert(0, str(quotient%2))
            quotient //= 2
        for i in range(8 - len(nb_binary)):
            nb_binary.insert(0, '0')
        num.append("".join(nb_binary))
    nums = 0
    num = "".join(num)
    for i in range(len(num)):
        nums = nums + int(num[i]) * (2** (len(num)- 1 - i))
    return nums

def num_to_ip(numbers):
    
    quotient = int(numbers)
    nb_binary = []
    while(quotient != 0):
        nb_binary.insert(0, str(quotient%2))
        quotient //= 2
    for i in range (32 - len(nb_binary)):
        nb_binary.insert(0, '0')
    num1, num2, num3, num4 = 0, 0, 0, 0
    for i in range(len(nb_binary)):
        if i < 8:
            num1 = num1 + int(nb_binary[i]) * (2** (7 - i%8))
        if i > 7 and i < 16:
            num2 = num2 + int(nb_binary[i]) * (2** (7 - i%8))
        if i > 15 and i < 24:
            num3 = num3 + int(nb_binary[i]) * (2** (7 - i%8))
        if i > 23:
            num4 = num4 + int(nb_binary[i]) * (2** (7 - i%8))
    
    return f"{num1}.{num2}.{num3}.{num4}"
