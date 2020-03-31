from time import sleep
print('\033[33m*-*' * 10)
print('{:^30}'.format('FIM DE ANO'))
print('*-*' * 10)
sleep(2)
print('\033[1;36mPrepare-se para assistir um show de fogos de artifícios!')
sleep(3)
print('\033[1;35mCONTAGEM REGRESSIVA!')
sleep(2)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[1;33mBUM! BUM! POOW! \nFELIZ ANO NOVO!')
