maze=[]
for i in range(10):
  a=[]
  x=input().split()
  for j in x:
    a.append(int(j))
  maze.append(a)

x=1
y=1
maze[1][1]=9


while maze[x][y]!=2:
    if maze[x][y+1]==0:
        maze[x][y+1]=9
        y+=1
    elif maze[x][y+1]==1 and maze[x+1][y]==0:
        maze[x+1][y]=9
        x+=1

    elif maze[x][y+1]==2:
        maze[x][y]=9
        maze[x][y+1]=9
        break
    elif maze[x+1][y]==2:
        maze[x][y]=9
        maze[x+1][y]=9
        break

    elif x==8 and y==8:
        break

for i in maze:
  for j in i:
    print(j, end=' ')
  print()