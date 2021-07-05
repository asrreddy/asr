
# decorators(normal)
def div(a,b):
    if a<b:
        a,b=b,a
    print(a/b)

div(4,2)

# decorators (inside the main function)
def div(a,b):
    print(a/b)
def smartdiv(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div1=smartdiv(div)    # decorator
div1(2,4)

def xxx(x,y):
    print(x+y)
def yyy(func,x,y):
    return(func(x,y))
z=yyy(xxx,2,3)

# another form of decorater

def smartdiv(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
@smartdiv    #decorator
def div(a,b):
    print(a/b)

div(2,4)

# different approach
def smartdiv(func):
    def inner(a,b):
        print('hii')
        if a<b:
            a,b=b,a
        func(a,b)       #dont code return here
        print('bye')
    return inner

@smartdiv   # decorator
def div(a,b):
    print(a/b)      #use print only..return not working
div(2,4)

# to return the original name of function the code is
def div(a,b):
    print(a/b)
def smartdiv(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div1=smartdiv(div)    # decorator
div1(2,4)
print(div1.__name__) # =>op is inner...if want real name
#
import functools
def div(a,b):
    print(a/b)
def smartdiv(func):
    @functools.wraps(func)
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div1=smartdiv(div)    # decorator
div1(2,4)
print(div1.__name__) #op is div..this is the original name of function
# squares and cubes using functions

def squares(numbers):
    res=[]
    for i in numbers:
        res.append(i*i)
    return res
numbers=range(10)
print(squares(numbers))

def cubes(numbers):

    res=[]
    for i in numbers:
        res.append(i*i*i)
    return res
numbers=range(20)
print(cubes(numbers))

# squres and qubes using time
import time
def squares(numbers):
    start=time.time()
    res=[]
    for i in numbers:
        res.append(i*i)
    end=time.time()
    print('time squares take '+str((end-start)*1000)+' mil sec')
    return res
numbers=range(10)
print(squares(numbers))

def cubes(numbers):
    start=time.time()
    res=[]
    for i in numbers:
        res.append(i*i*i)
    end=time.time()
    print('time squares take '+str((end-start)*1000)+' mil sec')
    return res
numbers=range(20)
print(cubes(numbers))

# squares,cubes using decorators
import time
def subtime(func):
    def inner(*args,**kwargs):
        start=time.time()
        end=time.time()
        print(func.__name__+' takes '+ str((end-start)*1000)+' mil sec')
        return func(*args, **kwargs)
    return inner
@subtime     # decorator
def squares(numbers):
    res=[]
    for i in numbers:
        res.append(i*i)
    return res
numbers=range(10)
print(squares(numbers))
@subtime
def cubes(numbers):
    res=[]
    for i in numbers:
        res.append(i*i*i)
    return res
numbers=range(10)
print(cubes(numbers))

# decorator
def xxx(func):
    def inner(*args):
        print('%s' %func)
        return func(*args)
    return inner
@xxx
def spam(a,b,c):
    return a+b+c
print(spam(1,2,3))
print(spam('a','b','c'))

# decorator
class tracer:
    def __init__(self,func):
        self.calls=0
        self.func=func
    def __call__(self, *args):
        self.calls+=1
        print('call %s to %s'%(self.calls,self.func.__name__))
        return self.func(*args)
@tracer
def spam(a,b,c):
    return a+b+c
print(spam(1,2,3))
print(spam('a','b','c'))
# function decorator (*args,**kwargs)
class tracer:
    def __init__(self,func):
        self.calls=0
        self.func=func
    def __call__(self, *args,**kwargs):
        self.calls+=1
        print('call %s to %s'%(self.calls,self.func.__name__))
        return self.func(*args,**kwargs)
@tracer
def spam(a,b,c):
    return a+b+c
print(spam(c=1,b=2,a=3))    #take care by **kwargs
print(spam(5,6,4))  #take care by *args

# decorator of classes apply to other class not work
class tracer:
    def __init__(self,func):
        self.calls=0
        self.func=func
    def __call__(self, *args,**kwargs):
        self.calls+=1
        print('call %s to %s'%(self.calls,self.func.__name__))
        return self.func(*args,**kwargs)
class place:
    @tracer
    def spam(self,a,b,c):
        return a+b+c
a=place()
print(a.spam(10,20,30))     #error...so use bellow one

# function decorator used in class
def xxx(func):
    def inner(*args):
        inner.calls+=1
        print('call %s to %s ' %(inner.calls ,func.__name__))
        return func(*args)
    inner.calls=0
    return inner
class tracer:
    @xxx
    def spam(self,a,b,c):
        return a+b+c
a=tracer()
print(a.spam(1,2,3))
print(a.spam('a','b','c'))
print(a.spam('a','b','c'))
print(a.spam.call)

# without decorator
calls=0
def tracer(func,*args):
    global calls
    calls+=1
    print('calls %s to %s'%(calls,func.__name__))
    func(*args)
def spam(a,b,c):
    print(a+b+c)
a=tracer(spam,1,2,3)
b=tracer(spam,5,7,9)
# 2
calls=0
def tracer(func):
    def inner(*args,**kwargs):
        global calls
        calls+=1
        print('call %s to %s'%(calls,func.__name__))
        return func(*args,**kwargs)
    return inner
@tracer
def spam(a,b,c):
    return a+b+c
print(spam(c=1,b=2,a=3))
print(spam(5,6,4))
# nonlocal

def tracer(func):
    calls = 0      #nonlocal
    def inner(*args,**kwargs):
        nonlocal calls      #global not work
        calls+=1
        print('call %s to %s'%(calls,func.__name__))
        return func(*args,**kwargs)
    return inner
@tracer
def spam(a,b,c):
    return a+b+c
print(spam(c=1,b=2,a=3))
print(spam(5,6,4))

# decorator (chapter 38)
class person:
    def __init__(self,name):
        self._name=name
    @property
    def name(self):
        'name property docs'
        print('fetch...')
        return self._name
    @name.setter
    def name(self,value):
        print('change...')
        self._name=value
    @name.deleter
    def name(self):
        print('remove...')
        del self._name
x=person('sathi')
print(x.name)
x.name='suma'
print(x.name)
del x.name
print(person.name.__doc__)

#  error come from class
class tracer:
    def __init__(self,func):
        self.calls=0
        self.func=func
    def __call__(self, *args, **kwargs):
        self.calls+=1
        print('calls %s to %s'%(self.calls,self.func.__name__))
        return self.func(*args,**kwargs)
class person:
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay
    @tracer
    def xxx(self,percent):
        self.pay+=(1.0+percent)
    @tracer
    def yyy(self):
        return self.name.split()[-1]
print('methods...')
a=person('satish',10000)
print(a.name,a.pay)
print(a.xxx(0.1))

# using function..no error
def tracer(func):
    calls=0
    def inner(*args):
        nonlocal calls
        calls+=1
        print('calls %s to %s'%(calls,func.__name__))
        return func(*args)
    return inner
class person:
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay
    @tracer
    def xxx(self,percent):
        self.pay*=(1.0+percent)
    @tracer
    def yyy(self):
        return self.name.split()[-1]
print('methods...')
a=person('edla satish',10000)
b=person('edla reddy',20000)
print(a.name,a.pay)
a.xxx(0.1)
b.xxx(0.2)
print(a.pay)
print(b.pay)
print(a.yyy(),b.yyy())

# using class ,to get op the code is
class tracer:
    def __init__(self,func):
        self.calls=0
        self.func=func
    def __call__(self, *args, **kwargs):
        self.calls+=1
        print('calls %s to %s'%(self.calls,self.func.__name__))
        return self.func(*args,**kwargs)
    def __get__(self,instance,owner):
        return wrapper(self,instance)
class wrapper:
    def __init__(self,desc,subj):
        self.desc=desc
        self.subj=subj
    def __call__(self, *args, **kwargs):
        return self.desc(self.subj,*args,**kwargs)

class person:
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay
    @tracer
    def xxx(self,percent):
        self.pay*=(1.0+percent)
    @tracer
    def yyy(self):
        return self.name.split()[-1]
a=person('edla reddy',30000)
b=person('edla satish',10000)
b.xxx(0.1)
print(b.pay)
print(a.yyy())
print(b.yyy())

or
class tracer:
    def __init__(self,func):
        self.calls=0
        self.func=func
    def __call__(self, *args, **kwargs):
        self.calls+=1
        print('calls %s to %s'%(self.calls,self.func.__name__))
        return self.func(*args,**kwargs)
    def __get__(self,instance,owner):
        def wrapper(*args, **kwargs):
            return self(instance,*args,**kwargs)
        return wrapper
class person:
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay
    @tracer
    def xxx(self,percent):
        self.pay*=(1.0+percent)
    @tracer
    def yyy(self):
        return self.name.split()[-1]
a=person('edla reddy',30000)
b=person('edla satish',10000)
b.xxx(0.1)
print(b.pay)
print(a.yyy())
print(b.yyy())

or
class tracer(object):
    def __init__(self,meth):
        self.calls=0
        self.meth=meth
    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            self.calls+=1
            print('calls %s to %s'%(self.calls,self.meth.__name__))
            return self.meth(instance,*args,**kwargs)
        return wrapper
class person:
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay
    @tracer
    def xxx(self,percent):
        self.pay*=(1.0+percent)
    @tracer
    def yyy(self):
        return self.name.split()[-1]
a=person('edla reddy',30000)
b=person('edla satish',10000)
b.xxx(0.1)
print(b.pay)
print(a.yyy())
print(b.yyy())

# function,class decorator page no 1312

from __future__ import print_function
registry={}
def register(obj):
    registry[obj.__name__]=obj
    return obj
@register
def xxx(n):
    return n**3
@register
class yyy:
    def __init__(self,x):
        self.x=x**4
    def __str__(self):
        return str(self.x)
print('Registry:')
for i in registry:
    print(i,'=>',registry[i],type(registry[i]))
print('\nmanual calls:')
print(xxx(2))
x=yyy(2)
print(x)

print('\nregistry calls:')
for i in registry:
    print(i,'=>',registry[i](2))

print(registry)
