def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if len(grid)==0:
        return 0
    if len(grid)==1 and len(grid[0])==1:
        if grid[0][0]==str(1):
            return 1
        else:
            return 0
    
    m = len(grid)
    n = len(grid[0])

    visited = [[0]*n for _ in range(m)]
    
    ct = 0
    
    
    for i in range(m):
        for j in range(n):
            if ((grid[i][j]==str(1)) and (visited[i][j]==0)):

                myQueue=[]
                myQueue.append([i,j])
            
                visited[i][j]=1


                ct=ct+1
                

                
                while(len(myQueue)!=0):
                    k = myQueue[0]
                    myQueue= myQueue[1:]
                    p = k[0]
                    q = k[1]

                    if 0<=(q-1):
                        if visited[p][q-1]==1:
                            pass
                        else:
                            if grid[p][q-1]==str(1):
                                visited[p][q-1]=1
                                myQueue.append([p,q-1])
                    if 0<=(p-1):
                        if visited[p-1][q]==1:
                            pass
                        else:
                            if grid[p-1][q]==str(1):
                                visited[p-1][q]=1
                                myQueue.append([p-1,q])
                    if n>(q+1):
                        if visited[p][q+1]==1:
                            pass
                        else:
                            if grid[p][q+1]==str(1):
                                visited[p][q+1]=1
                                myQueue.append([p,q+1])
                    if m>(p+1):
                        if visited[p+1][q]==1:
                            pass
                        else:
                            if grid[p+1][q]==str(1):
                                visited[p+1][q]=1
                                myQueue.append([p+1,q])
    
    return ct


