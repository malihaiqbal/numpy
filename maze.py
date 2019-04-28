#program 1
print("CUBE: ")
n=int(input("enter number"))
def cube(n):
    return n**3
xyz=cube(n)
print(xyz)


#program 2
print("fact")
def factorial(n):
    if n==1:
         return 1
    return n*factorial(n-1)   
    
fact=factorial(n)
print(fact)

#program 3
print("string\0")
string = 'ababcdab'
pattern = 'ab'
count=0
pattern_len = len(pattern)
def cpattern(pattern,string):
    count = 0
    for i in range(len(string)):
        
        if string[i:i+pattern_len] == pattern:
            
            count+=1
    return (count)
number=cpattern('on','kwonjiyong')
print(number)

    
#program 4
def maze_user(maze):
   i=0
   j=0
   temp=1
   while i<=4 and j<=6 and i>=0 and j>=0:
    choice = input("Enter l for left r for right u for up d for down :\n")   
    if(choice=='r'):
        temp=maze[i][j+1]
        j=j+1
    elif (choice=='l'):
        temp=maze[i][j-1]
        j=j-1
    elif choice=='u':
         temp=maze[i-1][j]
         i=i-1
    elif(choice=='d'):
         temp=maze[i+1][j]
         i=i+1
    if temp==1 or temp==3: 
         break

   if temp==3:
    print("You Won")
   else:
    print("You Lost")

maze=[[2,0,1,0,0,0,1],[1,0,1,0,1,0,1],[1,0,1,0,1,0,1],[1,0,1,0,1,0,1],[1,0,0,0,1,0,3]]
maze_user(maze)

def maze_auto(maze):
  i=0
  j=0
  print("Path : ")

  while i<=4 and j<=6 and i>=0 and j>=0:
  
   if(j+1 <= 6 and maze[i][j+1]==0   and j>=0  or maze[i][j+1]==3):
        if(maze[i][j+1]==3):
          print(print("Right-->End :)"))
          break
        j=j+1  
        maze[i][j]=2
        print("Right-->",end=(''))

   elif (maze[i][j-1]==0 and i>=0 and j-1 >=0 or maze[i][j-1]==3):
        if(maze[i][j-1]==3):
          print(print("Left-->End :)"))
          break
        j=j-1  
        maze[i][j]=2
        print("Left-->",end=(''))

   elif maze[i-1][j]==0 and i-1>=0 and j >=0 or maze[i-1][j]==3:
         if(maze[i-1][j]==3):
          print(print("Up-->End :)"))
          break
         i=i-1 
         maze[i][j]=2
         print("Up-->",end=(''))
         
   elif(maze[i+1][j]==0 and i+1 <= 4 and j <=6 or maze[i+1][j]==3):
         if(maze[i+1][j]==3):
          print(print("Down-->End :)"))
          break
         i=i+1 
         maze[i][j]=2
         print("Down-->",end=(''))

maze_auto(maze)
