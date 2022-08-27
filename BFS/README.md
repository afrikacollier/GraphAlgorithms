# Breadth First Search
Implementing breadth first search... involves taking into consideration the nearest edges before going deeper.                                                                                           
For instance consider the points

<img src="https://i.imgur.com/rgMwkIW.png" style="width=100%; object-fit:contain;">
_Using bread first search we print out the nearest points before going for the deeper points.
We get the following points using breadth first search...
Suppose we set 0 as our starting point..  Then we have_
`0 1 4 2 3...`
## Explanation...
To use breadth first search we use a queue system... because in a queue.. the First element that go
es in will the first to go out which is the perfect method we need to solve this problem since we need to account for the nearest elements before the deeper ones                                          Demonstrating the idea.. from the Example below..

* We instanstiate a queue. and the points( which contains the list of points)
```
 Queue = []                                                                                      
 Points = []  
```
* Starting from 0.. we visit the point 0..
which is enqueued into the Queue...
* Now we have Queue = [0]
* Then we pop 0 out since we are following the Queueing rules..(FIFO)
thus the Queue goes empty and we now have Queue = []
* Since we popped a value we enlist the popped value into the Points array now we have Points = [0]
* Now we go for the the neighbors of 0 which was just popped  out... The two neigbors of 0 are 1 and 4 then we push those to values into the queue... now we have                                         `Queue = [1, 4]`
* we pop out the first as usual following the Queueing rules..(FIFO)
and we enlist into points... we now have
`Queue = [4] and Points = [0, 1]`
* Since 1 was just dequeued we then check for the neighbors of 1 and enqueue them.. The neighbors of
1 are 2 and 3 we enqueue them too                                                                    now we have `Queue = [4, 2, 3]`
* we pop out 4 and we add into Points                                                                `Points = [0, 1, 4] and Queue = [2, 3]`
* Then we check for the neighbors of 4 which are 0 1 3 but we realize that they've already been enlisted or queued.. so we don't do anything.                                                      
* We do the same thing for 2 and 3... and their neighbors have already been enlisted or queued thus w
e have                                                                                               `Queue = [] and Points = [0, 1, 4, 2, 3]`
