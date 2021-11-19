# Ex1_py
## Elevator Problem
### Understanding and planning of the problem: 
In this task we received 2 folders that include a json elevator call list and json building file that include the building details and the elevators details. <br />
We need to find an elevator for any call in the optimal way , before we begin to write the algorithm , we want to present and explain the elevator problem .
### There are some problems:
**1.** The calls list includes calls of people that want to go down , and calls of people that want to go up. <br />
**2.** The building may have many floors which can affect the waiting time of each call.<br />
**3.** Useage and supervision of many elevators in some cases. <br />
**4.** every elevator has a different speed and "delay time". <br />
**5.** We need to fill the calls in the optimal way , but we need to understand what is it the optimal way according to the problems above.
### we will write some example and suggestions that can improve and take us to the optimal way do this calls list:
Our main targets in this algorithm: <br />
**1.** Every person waiting time will be minimal . <br />
**2.** Maximum handling of calls every moment . <br />
**3.** All calls waiting time will be equal with no relation to the call type. <br />
**4.** Maximum usage of all the elevators for minimal number of uncompleted calls. <br />
 In offine algoritem we start to perform the calls after we get all of them.
 # Our algorithm:
 * some define - f=floors in the building.
                 ll=list of calls (for example).
                 el=number of elevators.
 ### if we have one elevators so:
 * We check if there is calls to go "up" and we assign the closest up call to the elevator.
 * We take all the calls "up" and if there people in our stops that want to go down we take them.
 * After we finish the calls "up" we check if there is down call above us .
 * If there is a call down we go up and take the call.
 * We do this until we don't have a calls to go down above us .
 * Now we take all the poeple that want to go down to their destination.
 ### else :if we have two or more elevators :
 * First of all we count the number of calls down and calls up separately.
 * Each elevator update her status according to the direction she's heading.(1 going up, -1 going down , 0 idle)
 * If both of then equal approximately , we send *el*1/2 (half of elevators) to highest down calls ,and half of them to lowest up calls .
 * After that , we will do same actions like the one's elevator algoritem.
 * Each call have a status 1 for up -1 for down.
 * We send the closest elevators in the same path as the call until we finish all the call in the list .


![image](https://user-images.githubusercontent.com/74299935/142682760-c202c7da-f100-4a30-9d70-fd63440f2fff.jpeg)
