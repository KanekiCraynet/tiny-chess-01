import json,os,sys,urllib.request as u,urllib.error as e,random
E=os.getenv("MAKEFUN_ENV_URL")or sys.exit("no MAKEFUN_ENV_URL")
random.seed(int(os.getenv("MAKEFUN_TRIAL_SEED")or 0))
V=[0,100,320,330,500,900,20000]
P=[0]*64
for i in range(64):
 r,f=divmod(i,8)
 if r in(1,6):P[i]+=10
 if f in(3,4)and r in(3,4):P[i]+=5
def p(p_,s):
 if abs(p_)==1:return P[s]if p_>0 else-P[63-s]
 if abs(p_)==2:return 5if s in(18,21,42,45)else 0
 if abs(p_)==3:return 3if s in(27,28,35,36)else 0
 return 0
def z(F):
 b=[0]*64
 for i,r in enumerate(F.split()[0].split('/')):
  f=0
  for c in r:
   if c.isdigit():f+=int(c)
   else:b[56-8*i+f]=(' PNBRQK'.index(c.upper())if c.isupper()else-' PNBRQK'.index(c.upper()));f+=1
 return b,F.split()[1]=='w'
def m(b,w):
 d={1:[(8,1),(16,2),(7,1),(9,1)],2:[(17,1),(15,1),(10,1),(6,1),(-17,1),(-15,1),(-10,1),(-6,1)],3:[(9,1),(-9,1),(7,1),(-7,1)],4:[(8,1),(-8,1),(1,1),(-1,1)],5:[(8,1),(-8,1),(1,1),(-1,1),(9,1),(-9,1),(7,1),(-7,1)],6:[(8,1),(-8,1),(1,1),(-1,1),(9,1),(-9,1),(7,1),(-7,1)]}
 r=[];K=b.index(6 if w else-6)
 for i,p_ in enumerate(b):
  if not p_ or(p_>0)!=w:continue
  a=abs(p_)
  if a==1:
   D=8 if w else-8
   if 0<=i+D<64 and not b[i+D]:r.append((i,i+D,5if(i+D)//8 in(0,7)else 0))
   if(w and i>=48)or(not w and i<16):
    if 0<=i+2*D<64 and not b[i+2*D]:r.append((i,i+2*D,0))
   for C in(D-1,D+1):
    if 0<=i+C<64 and b[i+C]*(-1if w else 1)>0:r.append((i,i+C,5if(i+C)//8 in(0,7)else 0))
  elif a in(2,3,4,5,6):
   for D,L in d[a]:
    j=i
    for _ in range(L if a<5 else 7):
     j+=D
     if not 0<=j<64 or(a in(3,4,5,6)and abs((i%8)-(j%8))>1 and abs((i//8)-(j//8))>1):break
     if not b[j]:r.append((i,j,0))
     elif b[j]*p_<0:r.append((i,j,0));break
     else:break
 return r
def M(b,mv):
 f,t,pr=mv
 p_,b[f]=b[f],0
 b[t]=pr if pr else p_
 return p_
def U(b,mv,c,p_):
 f,t,_=mv
 b[f],b[t]=p_,c
def ev(b,w):
 s=0
 for i,p_ in enumerate(b):
  if p_:s+=(V[abs(p_)]+p(p_,i))*(1if p_>0else-1)
 K=b.index(6 if w else-6)
 if K<8 and w or K>=56 and not w: s+=50
 if w and K<8: s+=20
 if not w and K>=56: s+=20
 return s if w else-s
def o(mv,b,t,k1,k2):
 def s_(mv):
  if mv[:2]in t:return 10000
  f,t_=mv[:2]
  p_=abs(b[f])
  c=abs(b[t_])if b[t_]else 0
  if c:return 9000+V[c]-V[p_]
  if mv[:2]==k1 or mv[:2]==k2:return 8000
  return 0
 return sorted(mv,key=s_,reverse=True)
def s(b,w,d,a,B,n,t,k1,k2):
 if not n[0]:return None,ev(b,w)
 n[0]-=1
 if d==0:return None,ev(b,w)
 mv=m(b,w)
 if not mv:return None,-20000 if w else 20000
 bst=None
 for mv_ in o(mv,b,t,k1,k2):
  c=M(b,mv_)
  _,sc=s(b,not w,d-1,-B,-a,n,t,k2,k1)
  sc=-sc
  U(b,mv_,c,b[mv_[0]]if mv_[2]==0 else b[mv_[1]])
  if sc>a:
   a,bst=sc,mv_
   if a>=B:
    if not c:k1,k2=mv_[:2],k1
    break
 return bst,a
g=k1=k2=''
t={}
while 1:
 g_=json.load(u.urlopen(u.Request(E+'/game',b'{}',{'content-type':'application/json'})))
 if g_['status']=='done':break
 g=g_['game']
 while g_['status']=='your_move':
  b,w=z(g_['fen'])
  n=[50000]
  bst=None
  for d in range(1,20):
   mv_,_=s(b,w,d,-1e9,1e9,n,t,k1,k2)
   if mv_:bst=mv_
   if not n[0]:break
  if not bst:bst=m(b,w)[0]
  uci='abcdefgh'[bst[0]%8]+str(8-bst[0]//8)+'abcdefgh'[bst[1]%8]+str(8-bst[1]//8)+('qrbn'[bst[2]-1]if bst[2]else'')
  g_=json.load(u.urlopen(u.Request(E+'/move',json.dumps({'game':g,'move':uci}).encode(),{'content-type':'application/json'})))
  print(f'game {g_["game"]}: {g_["outcome"]} by {g_["reason"]}',file=sys.stderr)
 print(f'done: {g_.get("wins")} won, {g_.get("draws")} drawn, {g_.get("losses")} lost',file=sys.stderr)