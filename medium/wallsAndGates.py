#BFS problem

def wallsAndGates(rooms):
    """
    :type rooms: List[List[int]]
    :rtype: None Do not return anything, modify rooms in-place instead.
    """

    
    if rooms==[]:
        return []
    
    if len(rooms[0])==1 and len(rooms)==1:
        return rooms

    m = len(rooms)
    n = len(rooms[0])

    myQueue = []
    
    visited = set()
    
    for i in range(m):
        for j in range(n):
            if rooms[i][j]==0:
                myQueue.append([i,j])
                visited.add(str(i)+"-"+str(j))
            elif rooms[i][j]==-1:
                visited.add(str(i)+"-"+str(j))
    
    #print visited
    #print myQueue
    
    while(len(myQueue)>0):
        #print myQueue
        curr = myQueue[0]
        val = rooms[curr[0]][curr[1]]
        myQueue = myQueue[1:]


        p = curr[0]
        q = curr[1]
        if 0<=(q-1):
            g = str(p)+"-"+str(q-1)
            if g in visited:
                pass
            else:
                visited.add(g)
                myQueue.append([p,q-1])
                rooms[p][q-1]=val+1
        if 0<=(p-1):
            g = str(p-1)+"-"+str(q)
            if g in visited:
                pass
            else:
                visited.add(g)
                myQueue.append([p-1,q])
                rooms[p-1][q]=val+1
        if n>(q+1):
            g = str(p)+"-"+str(q+1)
            if g in visited:
                pass
            else:
                visited.add(g)
                myQueue.append([p,q+1])
                rooms[p][q+1]=val+1
        if m>(p+1):
            g = str(p+1)+"-"+str(q)
            if g in visited:
                pass
            else:
                visited.add(g)
                myQueue.append([p+1,q])
                rooms[p+1][q]=val+1
    return rooms

rooms = [[2147483647,0,2147483647,2147483647,0,2147483647,-1,2147483647]]

#print rooms

print (wallsAndGates(rooms))