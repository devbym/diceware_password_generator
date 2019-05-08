# DICEWARE password generator

from random import randint

li = []

def gen_round(turns=5):
    round_result = ''
    _li = []
    while turns > 0:
        turns = turns - 1
        _li.append(str(randint(1,6)))
    round_result = ''.join(map(str, _li))
    return round_result

def wordpicker():
    w = open(r'diceware/diceware_list.txt',  'r')
    number = gen_round()
    for line in w.readlines():
        if number in line:
            word = line[6:].capitalize()
            li.append(word)
            return word.strip()
    w.close()

def appender(li):
    op = open(r'diceware/generated.txt', 'a')
    for word in li:
        op.write(word)
    op.close()

def writer(li):
    op = open(r'diceware/generated.txt', "x")
    for word in li:
        op.write(word)
    op.close()

def main():
    amt = int(input('How many words?: '))
    while amt > 0:
        amt = amt - 1
        wordpicker()
    try:
        writer(li)
    except FileExistsError:
        appender(li)
    print(''.join(li))


if __name__ == '__main__':
        main()
