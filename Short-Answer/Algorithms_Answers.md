#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

This will take n loops to break the while loop. Therefore this will run in O(n) time.

b)

The outer loop will take n passes to complete. The inner loop with take log n passes. This will run in O(n log n) time

c)

Each call happens O(1) time, and will take n calls to complete. This will run in O(n) time.

## Exercise II


```
function find_f_floor(floors, starting_floor=0)
  # number of unchecked floors
  n_floors = floors - starting_floor
  # pivot
  midpoint = n_floors // 2 + starting_floor

  drop_egg(midpoint)

  if egg broke
    if n_floors equals 1
      return midpoint
    floors = midpoint
  else
    if n_floors equals 1
      return midpoint + 1
    starting_floor = midpoint + 1
  
  return find_f_floor(floors, starting_floor) 
```

this solutions require you to drop only log n eggs in the worst case.

it will run in O(log n) time