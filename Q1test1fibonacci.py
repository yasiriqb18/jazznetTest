# This function gives you the Fibonacci sequence certain value. 
def findfib(fn):
    if fn < 1:
        print("wrong number")
    elif fn == 0:
        return 0
    elif fn == 1:
        return 1
    else:
        return (findfib(fn-1) + findfib(fn-2))
print ("give you the certain fib number ->",findfib(10)) #change the fn value to know the Fibonacci value in the sequence
################################################

fn = [1,2]
while fn[-1] < 100:
    fn.append(fn[-1] + fn[-2])
print(fn)
evenf = []
for n in fn:
    if n % 2 ==0:
        evenf.append(n)
print(evenf)

sum =0
for n in evenf:
    sum += n
print(sum)
