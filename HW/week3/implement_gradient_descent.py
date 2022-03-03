#import matplotlib.pyplot as plt
def revenue_derivative(tax):
    return (100*(1/(tax+1)-2*(tax-0.2)))

thresshold = 0.0001
maximum_iterations = 100000
keep_going = True
iterations = 0
step_size = 0.001 
current_rate = 0.7

def revenue_derivative_flipped(tax):
    return (0-revenue_derivative(tax))

while(keep_going):
    rate_change = step_size * revenue_derivative_flipped(current_rate)
    current_rate = current_rate - rate_change
    print(current_rate,rate_change)
    #print(current_rate,rate_change)
    if abs(rate_change)<thresshold:
        keep_going = False
    if iterations >=maximum_iterations:
        keep_going = False
    iterations = iterations +1

#xs = [x/1000 for x in range(1001)]
#ys = [revenue_derivative_flipped(x) for x in xs]
#plt.plot(xs,ys)
#plt.title('the tax/revenue curve-flipped')
#plt.xlabel('current tax rate')
#plt.ylabel('revenue - flipped')
#plt.show()