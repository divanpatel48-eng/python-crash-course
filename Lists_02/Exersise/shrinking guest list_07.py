guest = ['vivan','alex','ruby','drove']

print ("\nGood news! I found a bigger table!\n")

guest.insert(0, "Alice")
guest.insert(2, "dalen")
guest.append("Charlie")

print("\nSorry, I can only invite two people for dinner.\n")

removed1 = guest.pop()
print(f"Sorry {removed1}, I cant invite you.")

removed2 = guest.pop()
print(f"Sorry {removed2}, I cant invite you.")

removed3 = guest.pop()
print(f"Sorry {removed3}, I cant invite you.")

removed4 = guest.pop()
print(f"Sorry {removed4}, I cant invite you.")

removed5 = guest.pop()
print(f"Sorry {removed5}, I cant invite you.")

print(f"\n{guest[0]}, you are still invited.")
print(f"{guest[1]}, you are still invited.")

del guest [0]
del guest [0]

print("\nFinal list:", guest)


