from hashlib import md5

criteria_met = False

if __name__ == '__main__':
    # key = 'abcdef'
    # print(md5((key + str(609043)).encode()).hexdigest())
    key = 'ckczppom'
    # data = open('input.txt', 'r')
    # secret = data.read()
    for i in range(1000000000):
        output = md5((key + str(i)).encode()).hexdigest()
        if output[:5] == '00000':
            print(output)
            print(i)
            break
