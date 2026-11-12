import json,os,urllib.request
U=os.environ['MAKEFUN_ENV_URL']
def p(x,y):
 r=urllib.request.Request(U+x,data=json.dumps(y).encode(),headers={'content-type':'application/json'})
 return json.load(urllib.request.urlopen(r))
V={'p':1,'n':3,'b':3,'r':5,'q':9,'k':100}
def board(f):
 d={}
 for y,row in enumerate(f.split()[0].split('/')):
  x=0
  for c in row:
   if c.isdigit():x+=int(c)
   else:d['abcdefgh'[x]+str(8-y)]=c;x+=1
 return d
def choose(f,ms):
 d=board(f)
 def rank(m):
  a=d[m[:2]].lower();v=d.get(m[2:4]);v=V[v.lower()] if v else 0
  return(-v,-(V[m[4]] if len(m)>4 else 0),V[a],m)
 return min(ms,key=rank)
while 1:
 g=p('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':g=p('/move',{'game':g['game'],'move':choose(g['fen'],g['legal_moves'])})
print('done',g.get('wins'),g.get('draws'),g.get('losses'))
# deterministic capture-first legal move policy, revision 3
