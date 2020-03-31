m = float(input('\033[4;34mUma distância em metros:\033[m '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('\033[1;31mA medida de {}m corresponde a: \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm.'.format(m, km, hm, dam, dm, cm, mm))
