# coding: utf-8

import glob, os
import json
import time


os.chdir("./Orders")


Newlatestfile=''
Placed=0
Accepted=0
Cancelled=0
while True:
   

    list_of_files = glob.glob("*.json")

    if list_of_files:
        latest_file = max(list_of_files, key=os.path.getctime)
        
        if latest_file != Newlatestfile:
            
            for file in glob.glob("*.json"):
               
                
                with open(file) as f:
                    for line in f:
                       
                        while True:
                            try:
                                jfile=json.loads(line)
                                if jfile['Type'] == 'OrderPlaced':
                                    Placed+=1
                                if jfile['Type'] == 'OrderAccepted':
                                    Accepted+=1
                                if jfile['Type'] == 'OrderCancelled':
                                    Cancelled+=1
                          
                                break
                            except ValueError:
                                line += next(f)
                
		
                os.rename(file, "./Orders_history/"+file)
            
        #print(jsons)
        print("OrderCancelled: " +str(Cancelled))
        print("OrderAccepted: " +str(Accepted))
        print("OrderPlaced: " +str(Placed))
        print('\n\n')
        list_of_files = glob.glob("*.json")
        if list_of_files:
            latest_file = max(list_of_files, key=os.path.getctime)
            Newlatestfile=latest_file
   
    
    time.sleep(5)


            
