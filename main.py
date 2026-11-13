import json,os,urllib.request as r
H=os.getenv("MAKEFUN_ENV_URL")
def P(a,b):
 q=r.Request(H+a,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 with r.urlopen(q) as x:return json.load(x)
V=[0,100,320,330,500,900,0]
N=(-33,-31,-18,-14,14,18,31,33);K=(-17,-16,-15,-1,1,15,16,17);D=(-17,-15,15,17);R=(-16,-1,1,16);Q=D+R;I=(0,0,N,D,R,Q,K)
Z={4:3,0:2,7:1,116:12,112:8,119:4}
b=[0]*128;w=0;z=0;n=0;T=50000;U=[]
X=StopIteration
def F(f):
 global w,z,o
 a=f.split();b[:]=[0]*128;i=112
 for c in a[0]:
  if c=="/":i-=24
  elif c.isdigit():i+=int(c)
  else:b[i]="PNBRQK".index(c.upper())+1+8*(c.islower());i+=1
 w=a[1]!="w";z=("K"in a[2])|("Q"in a[2])<<1|("k"in a[2])<<2|("q"in a[2])<<3
 o=(int(a[3][1])-1)*16+ord(a[3][0])-97 if a[3]!="-"else-1
def A(s,v):
 for d in N+K:
  t=s+d
  if t&0x88:continue
  q=b[t]
  if q==(2 if v else 10) and d in N or q==(6 if v else 14) and d in K or q==(1 if v else 9) and d in((-15,-17)if v else(15,17)):return 1
 for d in Q:
  t=s+d
  while not(t&0x88):
   q=b[t]
   if q and(q&8)==(0 if v else 8)and((q&7)==5 or(q&7)==(3 if d in D else 4)):return 1
   if q:break
   t+=d
 return 0
J=lambda v:b.index(14-8*v)
def G():
 m=[];u=8*w;t=8-u
 def h(s,a):
  q=a>>4
  if q in(0,7):
   for f in(5,4,3,2):m.append(s|(a<<7)|(f<<14))
  else:m.append(s|(a<<7))
 for s in range(128):
  if s&0x88:continue
  p=b[s]
  if not p or(p&8)!=u:continue
  v=p&7
  if v==1:
   d=16-32*w;a=s+d
   if not(a&0x88)and b[a]==0:
    h(s,a)
    if(s>>4)==1+5*w:
     c=s+2*d
     if b[c]==0:m.append(s|(c<<7))
   for d in(d-1,d+1):
    a=s+d
    if a&0x88:continue
    q=b[a]
    if q and(q&8)==t:h(s,a)
    elif a==o:m.append(s|(a<<7))
  else:
   for d in I[v]:
    a=s+d
    while not(a&0x88):
     q=b[a]
     if not q:m.append(s|(a<<7))
     else:
      if(q&8)==t:m.append(s|(a<<7))
      break
     if v==2 or v==6:break
     a+=d
 for f,t,g,p in((4,6,1,7),(4,2,2,0),(116,118,4,119),(116,114,8,112)):
  if z&g and b[p]==4+8*w and all(b[s]==0 for s in range(min(f,p)+1,max(f,p)))and all(not A(s,w==1)for s in(f,(f+t)//2,t)):m.append(f|(t<<7))
 return m
def M(m):
 global z,o,w
 U.append((b[:],z,o,w))
 f=m&127;t=(m>>7)&127;g=(m>>14)&7
 d=b[f]
 if(d&7)==1 and t==o:b[t-16+32*w]=0
 b[t]=g+8*w if g else d
 b[f]=0
 if(d&7)==6 and abs(t-f)==2:b[f+1 if t>f else f-1]=b[f+3 if t>f else f-4];b[f+3 if t>f else f-4]=0
 for s in(f,t):z&=~Z.get(s,0)
 o=(f+t)//2 if(d&7)==1 and abs(t-f)==32 else-1
 w^=1
def W():
 global z,o,w
 b[:],z,o,w=U.pop()
def L():
 o=[]
 for m in G():
  M(m)
  if not A(J(w==1),w==0):o.append(m)
  W()
 return o
def E():
 s=0
 for q in range(128):
  if q&0x88:continue
  p=b[q]
  if not p:continue
  t=p&7;f=q&7;r=q>>4;v=not(p&8);a=r if v else 7-r
  c=7-(abs(f-3.5)+abs(a-3.5))
  h=(0,0,4,3,1,2,-4)[t]*c
  if t==1:h=6*a+2*(3.5-abs(f-3.5))
  s+=(V[t]+h)*(2*v-1)
 return s if w==0 else-s
def O(v):return sorted(v,key=lambda m:-((10*V[b[(m>>7)&127]&7])if b[(m>>7)&127]else 0)-(900 if(m>>14)&7 else 0))
def Y(a,z):
 global n
 n+=1
 if n>T:raise X
 s=E()
 if s>=z:return z
 if s>a:a=s
 m=[m for m in G() if b[(m>>7)&127]]
 l=[]
 for x in m:
  M(x)
  if not A(J(w==1),w==0):l.append(x)
  W()
 for x in O(l):
  M(x)
  try:s=-Y(-z,-a)
  finally:W()
  if s>=z:return z
  if s>a:a=s
 return a
def S(d,a,z):
 global n
 n+=1
 if n>T:raise X
 if d<=0:return Y(a,z)
 m=O(L())
 if not m:return-100000-d if A(J(w==0),w==1)else 0
 e=-99999
 for x in m:
  M(x)
  try:s=-S(d-1,-z,-a)
  finally:W()
  if s>e:e=s
  if e>a:a=e
  if a>=z:break
 return e
def v(m):
 f=m&127;t=(m>>7)&127;g=(m>>14)&7
 s="abcdefgh"[f&7]+str((f>>4)+1)+"abcdefgh"[t&7]+str((t>>4)+1)
 if g:s+="nbrq"[g-2]
 return s
def C(f,l):
 global n
 F(f)
 m=O(L())
 k=m[0];n=0
 for d in(2,3):
  o=[k]+[x for x in m if x!=k] if d>2 else m
  q=None;e=-99999
  try:
   for x in o:
    M(x)
    try:s=-S(d-1,-1000000,1000000)
    finally:W()
    if s>e:e,q=s,x
  except X:break
  if q is not None:k=q
 return v(k)if v(k)in l else l[0]
while H and(g:=P("/game",{}))["status"]!="done":
 while g["status"]=="your_move":
  g=P("/move",{"game":g["game"],"move":C(g["fen"],g["legal_moves"])})
