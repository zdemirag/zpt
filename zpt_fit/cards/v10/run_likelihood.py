import os 

name=10
for i in range(0,6):
    command = "combine -M MultiDimFit zpt_multidim.root -P r_zcat"+str(i)+" --floatOtherPOIs=1 --algo=grid --points 2000 -m "+ str(i)+" -t -1 --expectSignal=1 --robustFit=1 & "
    print command 
    #os.system(command)
    #number = 5000
    #command2 = "combine -M MultiDimFit zpt_multidim.root -P r_zcat"+str(i)+" --floatOtherPOIs=1 --algo=grid --points "+str(number)+" -m "+ str(name)+str(i)+" -t -1 --expectSignal=1 --robustFit=1 --fastScan &"
    #print command2 
    #os.system(command2)
    
