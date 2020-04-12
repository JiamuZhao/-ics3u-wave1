a = int(input())

toonies = a // 200
loonies = a % 200 // 100
quarters = (a - toonies * 200 - loonies * 100) // 25
dimes = (a - toonies * 200 - loonies * 100 - quarters * 25) // 10
nickes = (a - toonies * 200 - loonies * 100 - quarters * 25 - dimes * 10) // 5
pennies = a - toonies * 200 - loonies * 100 - quarters * 25 - dimes * 10 - nickes * 5

print(toonies, "toonies, ", loonies, "loonies, ", quarters, "quarters, ",
      dimes, "dimes, ", nickes, "nickes, ", pennies, "pennies, ", sep='')