import math 
import matplotlib.pyplot as plt
#revenue 
def revenue(tax):
    return(100*(math.log(tax+1)-(tax-0.2)**2+0.04))

def revenue_flipped(tax):
    return 0-revenue(tax)

xs = [x/1000 for x in range(1001)]
ys = [revenue_flipped(x) for x in xs]
plt.plot(xs,ys)
current_rate = 0.7
plt.plot(xs,ys)
plt.title('thr tax/revenue curve -flipped ')
plt.xlabel('current tax rate')
plt.ylabel('revenue-Flipped')
plt.show()