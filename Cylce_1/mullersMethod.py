def fn(x):
  return x**3-13*x-12

def Muller(x0, x1, x2, iter):
  icount=0
  for i in range(0, iter):

    f0=fn(x0)
    f1=fn(x1)
    f2=fn(x2)

    h0=x1-x0
    h1=x2-x1

    d0=(f1-f0)/(x1-x0)
    d1=(f2-f1)/(x2-x1)

    a=(d1-d0)/(h0+h1)
    b=a*h1+d1
    c=f2

    d=((b**2)-(4*a*c))**0.5
    r1=b+d
    r2=b-d

    if r1>r2:
      r=r1
    elif r2>r1:
      r=r2

    x3=x2-((2*c)/r)
    E=((x3-x2)/x3)*100
    icount=icount+1

    print("x0 = ",x0)
    print("x1 = ",x1)
    print("x2 = ",x2)
    print("The resultant x3 = ",x3)
    print("Error = ", abs(E))
    print("Iteration: ", icount)
    print("")

    x0=x1
    x1=x2
    x2=x3


iter=5
x0=4.5
x1=5.5
x2=5

Muller(x0, x1, x2, iter)
