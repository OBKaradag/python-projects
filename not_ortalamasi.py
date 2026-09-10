'''import keyword
from keyword import kwlist'''

'''import keyword
keyword.kwlist
print(kwlist)'''

print("ÖBK Not Sistemine Hoşgeldiniz...")
vize=int(input('Vize:'))
vizeNot=float(vize*0.4)
print('Vize Notunuz:',vizeNot)
final=int(input('Final:'))
finalNot=float(final*0.6)
print('Final Notunuz:',finalNot)
TopNot=float(finalNot+vizeNot)
print("Toplam Not=",TopNot)
if TopNot<50:
    print("FF")
    print("kaldın...")
elif 50<=TopNot<60:
    print("DC")
    print("şartlı geçme durumu...")
if 60<=TopNot<68:
    print("CC")
    print("Geçtiniz...")
if 68<=TopNot<75:
    print("CB")
    print("Geçtiniz...")
if 75<=TopNot<82:
    print("BB")
    print("Geçtiniz...")
if 82<=TopNot<88:
    print("BA")
    print("Geçtiniz...")
if 88<=TopNot<100:
    print("AA")
    print("Bravo geçtiniz...")
#if else kullanımı ile detaysız hali
"""if TopNot>=60:
    print("geçtin")
else:
    print("kaldın")"""




