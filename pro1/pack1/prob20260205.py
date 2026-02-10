class Machine:
    def __init__(self):
        self.coinin = CoinIn() #<- 이게 핵심
    def showData(self):
        print('---------------------------')
        coin = input('동전을 입력하세요 : ')
        cupCount = input('몇 잔을 원하세요? : ')
        a = self.coinin.calc(coin, cupCount)
        if a < 0:
            print('금액이 부족합니다.')
        else:
            print(f'커피{cupCount}잔과 잔돈{a}')


class CoinIn:
    def calc(self, coin, cupCount):
        change = int(coin) - 200 * int(cupCount)
        return change

coin = 0
cupCount = 0
if __name__ == '__main__':
    machine = Machine()
    machine.showData()