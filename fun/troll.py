def rootiply(a1,b1,a2,b2,c):
	''' multipy a1+b1*sqrt(c) and a2+b2*sqrt(c)... return a,b'''
	return a1*a2 + b1*b2*c, a1*b2 + a2*b1

def rootipower(a,b,c,n):
	''' raise a + b * sqrt(c) to the nth power... returns the new a,b and c of the result in the same format'''
	ar,br = 1,0
	while n != 0:
		if n%2:
			ar,br = rootiply(ar,br,a,b,c)
		a,b = rootiply(a,b,a,b,c)
		n /= 2
	return ar,br

def rootipowermod(a,b,c,k,n):
	''' compute root powers, but modding as we go'''
	ar,br = 1,0
	while k != 0:
		if k%2:
			ar,br = rootiply(ar,br,a,b,c) 
			ar,br = ar%n,br%n
		a,b = rootiply(a,b,a,b,c)
		a,b = a%n, b%n
		k /= 2
	return ar,br

def fib(k):
	''' the kth fibonacci number'''
	a1,b1 = rootipower(1,1,5,k)
	a2,b2 = rootipower(1,-1,5,k)
	a = a1-a2
	b = b1-b2
	a,b = rootiply(0,1,a,b,5)
	# b should be 0!
	assert b == 0
	return a/2**k/5

def powermod(a,k,n):
	''' raise a**k, modding as we go by n'''
	r = 1
	while k!=0:
		if k%2:
			r = (a*r)%n
		a = (a**2)%n
		k/=2
	return r

def mod_inv(a,n):
	''' compute the multiplicative inverse of a, mod n'''
	t,newt,r,newr = 0,1,n,a
	while newr != 0:
		quotient = r / newr
		t, newt = newt, t - quotient * newt
		r, newr = newr, r - quotient * newr
	if r > 1: return "a is not invertible"
	if t < 0: t = t + n
	return t

def fibmod(k,n):
	''' compute the kth fibonacci number mod n, modding as we go for efficiency'''
	a1,b1 = rootipowermod(1,1,5,k,n)
	a2,b2 = rootipowermod(1,-1,5,k,n)
	a = a1-a2
	b = b1-b2
	a,b = rootiply(0,1,a,b,5)
	a,b = a%n,b%n
	assert b == 0
	return (a*mod_inv(5,n)*mod_inv(powermod(2,k,n),n))%n

if __name__ == "__main__":
	assert rootipower(1,2,3,3) == (37,30) # 1+2sqrt(3) **3 => 13 + 4sqrt(3) => 39 + 30sqrt(3)
	assert fib(10)==55
	#print fib(10**15)%(10**9+7) # takes forever because the integers involved are REALLY REALLY REALLY BIG
	print (fibmod(10**8,10**9+7)) # much faster because we never deal with integers bigger than 10**9+7