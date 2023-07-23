list = [1,2,3,4,5,6,7,8,9]
n = 9

pos = -1
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos'] = i
            return True
        i = i+1
    return False
            
if search(list,n):
    print("Element found at", + pos)
else:
    print("Not Found!")
    
    
    
#the end