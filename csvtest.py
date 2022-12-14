#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from random import randint as ri
import numpy as np
from scipy.optimize import linear_sum_assignment
n=4
def mkgrid():
	G=np.random.randint(0,20,(n,n))
	# ~ rep(G)
	g=G.max()-G
	# ~ rep(g)
	a=g.min(axis=1)
	g=g.T-a
	g=g.T
	a=g.min(axis=0)
	g=g-a
	# ~ rep(g)
	return G,g
def omax(g):
	y=g.max()-g
	a=y.min(axis=1)
	y=y.T-a
	y=y.T
	a=y.min(axis=0)
	y=y-a
	return y
	
def retro(g):
	# ~ print(g)
	nn=len(g)
	t=g.sum()
	r=g.sum(axis=1)
	c=g.sum(axis=0)
	x=g.copy()
	# ~ print (t,r,c)
	for li in range(nn):
		for co in range(nn):
			x[li,co]=4*g[li,co]+t-2*r[li]-2*c[co]
			# ~ print (li,co,x[li,co])
			# ~ input()
	# ~ print(x)
	# ~ y=x.max()-x
	# ~ a=y.min(axis=1)
	# ~ y=y.T-a
	# ~ y=y.T
	# ~ a=y.min(axis=0)
	# ~ y=y-a	
	# ~ print(y)
	return x
# ~ import itertools as it
# ~ reci=0
# ~ recs=n*n*21
# ~ si=""
# ~ ss=""
# ~ for c in it.permutations (list(range(n))):
	# ~ ttl=sum([g[l,c] for l,c in zip (range(n),c)])
	# ~ if ttl >reci:
		# ~ reci=ttl
		# ~ si=(c,[g[l,c] for l,c in zip (range(n),c)])
	# ~ if ttl <recs:
		# ~ recs=ttl
		# ~ ss=(c,[g[l,c] for l,c in zip (range(n),c)])
def rep(g):
	for l in g:
		print(";".join([str(v) for v in l]))
	print()

def mark():
	x=g.copy()
	cycle=0
	while True:
		cycle+=1
		while np.count_nonzero(x==0):
			lc=np.count_nonzero(x==0,axis=1)
			cc=np.count_nonzero(x==0,axis=0)
			full=np.append(lc,cc)
			m=full[np.where(full>0)].min()
			# ~ print(full,m)
			if m in lc:
				row=np.where(lc==m)[0][0]
				col=np.where(x[row]==0)[0][0]
			else:
				col=np.where(cc==m)[0][0]
				row=np.where(x[:,col]==0)[0][0]
			x[row,col]=1000
			x[row][np.where(x[row]==0)]=-1000
			x[:,col][np.where(x[:,col]==0)]=-1000
			# ~ print(x)
	
		squared=np.count_nonzero(x==1000)
		if squared==n:
			# ~ rep(x)
			print("solved",cycle)
			sq=np.where(x==1000)
			print(G[sq])
			a=sum(G[sq])
			ri,ci=linear_sum_assignment(g)
			print(G[ri,ci])
			b=sum(G[ri,ci])
			if a!=b:
				input()
			return
		
		# ~ print("squared :",squared)
		tl=np.count_nonzero(x==1000,axis=1)
		tl=np.where(tl==0)[0]
		# ~ print("TL :",tl)
		# ~ input()
		col=(x[tl,])
		# ~ print(col)
		tc=np.count_nonzero(col==-1000,axis=0)
		tc=np.where(tc>=1)[0]
		# ~ print("TC:",tc)
		# ~ print(x[:,tc])
		changed=True
		while changed:
			changed=False
			ntl=np.count_nonzero(x[:,tc]==1000,axis=1)
			ntl=np.where(ntl>=1)[0]
			# ~ print("ntl:",ntl)
			for l in ntl:
				if l not in tl:
					tl=np.append(tl,l)
					tl.sort()
					changed=True
			col=(x[tl,])
			# ~ print(col)
			ntc=np.count_nonzero(col==-1000,axis=0)
			ntc=np.where(ntc>=1)[0]
			# ~ print("ntc",ntc)
			for c in ntc:
				if c not in tc:
					tc=np.append(tc,c)
					tc.sort()
					changed=True
			# ~ print("TL:",tl)
			# ~ print("TC:",tc)
			# ~ print(x[:,tc])
			# ~ print(changed)
			# ~ print(x)
		# ~ input()
		remain=x[tl,][:,[c for c in range(n) if c not in tc]]
		# ~ print(remain)
		# ~ print(remain.min())
		m=remain.min()
		x[np.where(x==1000)]=0
		x[np.where(x==-1000)]=0
		for l in tl:
			for c in range(n):
				if c not in tc:x[l,c]-=m
		for c in tc:
			for l in range(n):
				if l not in tl:x[l,c]+=m
		# ~ print(x[tl,][:,[c for c in range(n) if c not in tc]])
		# ~ print(x)
		zeroes=np.count_nonzero(x==0,axis=1)
		notfound=True

	# ~ x[(0,1,2),][:,(3,4)]
test=0
while True:
	test+=1
	# ~ print("="*50)
	G,g=mkgrid()
	# ~ print(G)
	# ~ mark()
	ri,ci=linear_sum_assignment(g)
	# ~ print(G[ri,ci])
	b=sum(G[ri,ci])
	# ~ print(b)
	y=retro(G)
	ri,ci=linear_sum_assignment(y)
	# ~ print(G[ri,ci])
	c=sum(G[ri,ci])
	if not test%10000:print(test)
	if b!=c :
		print (G)
		print(b,c)
		input()

# ~ g=g.max()-g
# ~ a=g.min(axis=0)
# ~ g=g-a
# ~ print(g)
# ~ a=g.min(axis=1)
# ~ g=g.T-a
# ~ g=g.T
# ~ print()
# ~ print(g)
# ~ zeroes=np.count_nonzero(g==0,axis=1)
# ~ print (zeroes)
# ~ mark()
# ~ print(reci,si)
print(recs,ss)
