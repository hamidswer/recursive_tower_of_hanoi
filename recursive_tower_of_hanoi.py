a = "a"
b = "b"
c = "c"
counter = 0
def recursive_tower_of_hanoi(n, a, b, c):
    global counter
    if (n==0):
        counter += 1
        print(f"Number {counter}: Go from {a} to {c}")
    else:
      recursive_tower_of_hanoi(n-1, a, c, b)
      counter += 1
      print(f"Number {counter}: Go from {a} to {c}")
      recursive_tower_of_hanoi(n-1, b, a, c)


recursive_tower_of_hanoi(2, a, b, c)
# Number 1: Go from a to c
# Number 2: Go from a to b
# Number 3: Go from c to b
# Number 4: Go from a to c
# Number 5: Go from b to a
# Number 6: Go from b to c
# Number 7: Go from a to c
