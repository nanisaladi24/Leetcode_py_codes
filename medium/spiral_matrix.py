def go_right(i,j_start,j_end,mat):
    right_mat=[]
    for k in range(j_start,j_end+1):
        right_mat.append(mat[i][k])
    return right_mat
def go_left(i,j_start,j_end,mat):
    left_mat=[]
    for k in range(j_start,j_end-1,-1):
        left_mat.append(mat[i][k])
    return left_mat
def go_up(j,i_start,i_end,mat):
    up_mat=[]
    for k in range(i_start,i_end-1,-1):
        up_mat.append(mat[k][j])
    return up_mat
def go_down(j,i_start,i_end,mat):
    down_mat=[]
    for k in range(i_start,i_end+1):
        down_mat.append(mat[k][j])
    return down_mat


def spiralOrder(myMat):
    myList=[]
    size_hor=len(myMat)
    size_ver=0
    if size_hor>1:
        size_ver=len(myMat[0])
    if size_hor==size_ver==0:
        return []
    if size_hor==size_ver==1:
        return myMat
    curr_border=[0,size_hor-1,0,size_ver-1]
    prev_border=curr_border.copy()
    while(prev_border[0]<=curr_border[1] and prev_border[1]>=curr_border[0] and prev_border[2]<=curr_border[3] and prev_border[3]>=curr_border[2]):
        myList=myList+go_right(curr_border[0],curr_border[2],curr_border[3],myMat)
        myList=myList+go_down(curr_border[3],curr_border[0]+1,curr_border[1],myMat)
        if curr_border[0]!=curr_border[1]:
            myList=myList+go_left(curr_border[1],curr_border[3]-1,curr_border[2],myMat)
        if curr_border[2]!=curr_border[3]:
            myList=myList+go_up(curr_border[2],curr_border[1]-1,curr_border[0]+1,myMat)
        prev_border=curr_border.copy()
        curr_border[0]=curr_border[0]+1
        curr_border[1]=curr_border[1]-1
        curr_border[2]=curr_border[2]+1
        curr_border[3]=curr_border[3]-1

        if curr_border[0]>curr_border[1] or curr_border[2]>curr_border[3]:
            break

        # print (prev_border)
        # print (curr_border)

    return myList



myMat=[[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
#print (myMat)
print (spiralOrder(myMat))
print ("done")

myMat=[[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]
#print (myMat)
print (spiralOrder(myMat))
print ("done")

myMat=[[2,5,8],[4,0,-1]]
#print (myMat)
print (spiralOrder(myMat))
print ("done")