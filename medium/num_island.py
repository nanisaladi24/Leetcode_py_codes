def rec_start(i,j,A,B,dim):
    # print "bef"
    #print B
    # print i,j
    # print B[i]
    # B[i][j]=2
    # print B[i][j]
    # print B
    B[i][j]=1
    # print "st"
    # print B
    # print "hey"
        #row shifts
    if (i-1)!=-1:
        #print B
        if B[i-1][j]==None and A[i-1][j]=="1":
            B=rec_start(i-1,j,A,B,dim)
    if (i+1)!=dim[0]:
        #print B
        if B[i+1][j]==None and A[i+1][j]=="1":
            B=rec_start(i+1,j,A,B,dim)
        #col shifts
    if (j-1)!=-1:
        #print B
        if B[i][j-1]==None and A[i][j-1]=="1":
            B=rec_start(i,j-1,A,B,dim)
    if (j+1)!=dim[1]:
        #print B
        if B[i][j+1]==None and A[i][j+1]=="1":
            B=rec_start(i,j+1,A,B,dim)
    #print B
    return B
    
    
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #self.A=grid
        
        if grid==[]:
            return 0
        
        #self.B=[[0]*len(grid[0])]*len(grid)
        self.B = [[None]*len(grid[0]) for _ in range(len(grid))]
        
        #print self.B
        myI=0
        i_max=len(grid)
        j_max=len(grid[0])
        dim=[i_max,j_max]
        for i in range(dim[0]):
            for j in range(dim[1]):
                #print grid[i][j]
                if grid[i][j]=="1":
                    if self.B[i][j]==None:
                        #print "hello"
                        self.B=rec_start(i,j,grid,self.B,dim)
                        myI=myI+1
        #print self.B
        return myI
                        