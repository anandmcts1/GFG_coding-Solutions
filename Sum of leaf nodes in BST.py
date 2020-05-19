
##Structure of node
'''
class Node:
    data=0
    left=None
    right=None

'''
##Complete this function
def sumOfLeafNodes(root):
    temp=None
    q=[]
    s=0
    if not root:
        return 0
    q.append(root)
    while q:
        temp=q.pop(0)
        if not temp.left and not temp.right:
            s+=temp.data
        else:
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
    del q
    return s



#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    data=0
    left=None
    right=None


def createNewNode(value):
    temp=Node()
    temp.data=value
    temp.left=None
    temp.right=None
    return temp
    

def newNode(root,data):
    if(root is None):
        root=createNewNode(data)
    elif(data<root.data):
        root.left=newNode(root.left,data);
    else:
        root.right=newNode(root.right,data)
        
    return root


    
def main():
    testcases=int(input())
    while(testcases>0):
        root=None
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        for i in arr:
            root=newNode(root,i)
        print(sumOfLeafNodes(root))
        testcases-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
