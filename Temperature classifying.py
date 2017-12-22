# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 13:27:13 2017

@author: mikkopos
"""

temperatures= [1.5, 3.0, 4.5, -3.0, 16.0, 5.0]
cold = []
comf = []

for temp in temperatures:
    if temp < -2:
        cold.append(temp)
    elif temp >= - 2 and temp < 2:
        comf.append(temp)
        
        list_count = len(cold)
        print (cold)
        
        
        
        #cold = []
#slippery = []
#comfortable = []
#warm = []

 # cold = below -2 degrees
 # Slippery = between -2 and +2
 # Comfortable = between +2 and +15
 # warm = over 15
 # iterate over values using for loop
 for temp in temperatures:
     if temp > 2:
         print ("that")
     if temp < -2:
         print ("this")
         #cold.append(temp)
   # elif temp >= -2 and temp < 2:
    #    slippery.append(temp)
   # elif temp >= 2 and < 15:
     #   comfortable.append(temp)
   # elif temp >= 15:
      #  warm.append(temp)
            
    # print the answers
    #slippery_times = len(slippery)temperatures = [1.5, 3.0, 4.5, -3.0, 16.0, 5.0]
    #print ('In April it was slippery', slippery_times, "times.")
    
    #comfortable_times = len(comfortable)
    #print ('In April it was comfortable' comfortable_times, 'times'.)
    
    
        
        