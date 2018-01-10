
# coding: utf-8

# In[79]:

import string
import random
import datetime
import json
import argparse
import time



class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)

def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



def savejson(orders,batch,hour,placed,accepted,interval,directory):


    numoffiles=int((orders/batch))*2
    if orders%batch != 0:
        numoffiles+=2
    
    #print ('numoffiles: ' +str(numoffiles))
    count=0
    for i in range(0,numoffiles,2):
        
        if count+batch >= numoffiles:
            batch=orders%batch
            #print('batch: '+str(batch))
        if i!=0:
            time.sleep(interval)
        with open(str(directory)+'orders_placeds'+str(hour)+'_'+str(i)+'.json', 'a') as placedfile:
            for j in range(0,(batch)):
                
                placedfile.write(placed[count+j]+'\n')
        time.sleep(interval)  
        with open(str(directory)+'orders_results'+str(hour)+'_'+str(i+1)+'.json', 'a') as acceptedfile:
            for j in range(0,(batch)):
                
                acceptedfile.write(accepted[count+j]+'\n')
        count+=batch
        #print('count: ' +str(count))
            

def data(orders):
    orders=1
    cent=1
    listofaccepted=[]
    listofplaced=[]
     
    for i in range(0,args.orders):
        
        typeOrder=['OrderPlaced','OrderAccepted','OrderCancelled']
        if cent<=4:
            hour=datetime.datetime.now().strftime('%Y'+'-'+'%m'+'-'+'%d'+'T'+'%H'+':'+'%M'+':'+'%S'+'Z')
            
            me = Object()
            me.Type = typeOrder[0]
            me.Data = Object()
            myid=(id_generator(8)+'-'+id_generator(4)+'-'+id_generator(4)+'-'+id_generator(4)+'-'+id_generator(12))
            me.Data.OrderId = myid
            me.Data.TimestampUtc=hour
            listofplaced.append(me.toJSON())
            

            #typeOrder=['OrderPlaced','OrderAccepted','OrderCancelled']
            me_1 = Object()
            me_1.Type = typeOrder[1]
            me_1.Data = Object()
            me_1.Data.OrderId = myid
            me_1.Data.TimestampUtc=hour
            listofaccepted.append(me_1.toJSON())
            
            cent=cent+1
            #print(cent)
        else:
            
            hour=datetime.datetime.now().strftime('%Y'+'-'+'%m'+'-'+'%d'+'T'+'%H'+':'+'%M'+':'+'%S'+'Z')
         
            #typeOrder=['OrderPlaced','OrderAccepted','OrderCancelled']
            me = Object()
            me.Type = typeOrder[0]
            me.Data = Object()
            myid=(id_generator(8)+'-'+id_generator(4)+'-'+id_generator(4)+'-'+id_generator(4)+'-'+id_generator(12))
            me.Data.OrderId = myid
            me.Data.TimestampUtc=hour
            listofplaced.append(me.toJSON())
            


            #typeOrder=['OrderPlaced','OrderAccepted','OrderCancelled']
            me_1 = Object()
            me_1.Type = typeOrder[2]
            me_1.Data = Object()
            me_1.Data.OrderId = myid
            me_1.Data.TimestampUtc=hour
            cent=1
            listofaccepted.append(me_1.toJSON())

    return listofplaced,listofaccepted,hour



parser = argparse.ArgumentParser()
parser.add_argument("-o","--orders", type=int, help='Number of orders to generate which will each produce two events.')
parser.add_argument("-bs","--batch", type=int, help='Batch size of events per file.')
parser.add_argument("-i","--interval", type=int, help='Interval in seconds between each file being created.')
parser.add_argument("-d","--directory", type=str, help='Output directory for all created files.')

args = parser.parse_args()


listofplaced,listofaccepted,hour = data(args.orders)
savejson(args.orders,args.batch,hour,listofplaced,listofaccepted,args.interval,args.directory)



            
# In[ ]:


