# new module imported

import marketdata
print('program 2 started')

if __name__ == '__main__':
    new_list = [7, 8, 9, 10, 11, 12]
    print('entered inside main of market data 2')
    result = marketdata.new_func(new_list)

    print(result[1], result[2])
