def closedPaths(number):
    num=str(number)
    closed=False
    closed8=False
    path=0
    path8=0
    dig_num=list(num)
    
    
    print(dig_num)
    for sdig in dig_num:
        dig=int(sdig)
        print(dig)
        if dig == 0:
            closed=True
            
            print('path')
        elif dig == 4:
            closed=True
            
            print('path')
        elif dig == 6:
            closed=True
            
            print('path')
        elif dig == 9:
            closed=True
            
            print('path')
        elif dig == 8:
            closed8=True
            
            print('path2')
        else:
            closed=False         
            closed8=False 
       
        if closed==True:
            path+=1
        elif closed8==True:
            path8=2
            path+=path8
        
    print('pathfinal:',path)
        
       
        

closedPaths(88805189014)