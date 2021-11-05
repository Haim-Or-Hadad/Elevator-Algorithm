# Ex1_py
##Elevator Problem
###Understanding and planning of the problem: 
In this task we need to get a calls list and find elevator for any call in the optimal way , before we will begin to write the algoritem , we want to present and explain the elevator problem .
###There are some problems:
1.The calls list includes calls of people that want to go down , and calls of people that want to go up.
2.The building may have a many floors.
3.there are maybe many elevators and we need to use them.
4.every elevator has a different speed and "close/ope door time ".
5.we need to fill the calls in the optimal way , but we need to understand what is it the optimal way .
###we will write some example and suggestions that can improve and take us to the optimal way do this calls list:
we wil want 
1.every person will wait the little time that we can .
2.that the algoritem do as mush as possible of calls in every moment .
3.that one person not wait a long time in relation to other person .
4.if all the elevators will work and this good for the algoritem it's excellent .
 In offine algoritem we start to perform the calls after we get all of them.
 #Our algorithm:
 * some define - f=floors in the building.
                 ll=list of calls (for example).
                 el=number of elevators.
 -if we have one elevators so:
                      we check if there is up call and we searce the close up call.
                      we take all the up calls and if there is in our stop people that want to go down we take them.
                      after we finish the up calls we check if there is down call above us .
                      if there is down call we go up and take this call.
                      we do this until we don't have a down call above us .
                      now we take all the poeple that want to go down to there destination.
 -else :if we have two or more elevators :
                      first of all we count the number of down and up calls separately.
                      if both of then equal Approximately , we send *el*1/2 (half of elevators) to the tallest calls for down ,and half of them to lowest calls for up .
                      after that , we will do same actions like the one's elevator algoritem.
                      we send the closest elevators that in the same path of the call until we finish the list of calls .
