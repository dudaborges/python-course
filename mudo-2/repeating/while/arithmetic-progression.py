print("\033[1;32;40mAP Generator\33[m")
print("-=" * 20)
firstTerm = int(input("First Term: "))
reason = int(input("AP Reason: "))
count = 0
repeating = 10
add = 0
while repeating != 0:
    add += repeating
    while count <= add:
        print(f"{firstTerm} -> ", end='')
        firstTerm += reason
        count += 1
    print("\033[1;31;40mPaused!\33[m")
    repeating = int(input("how many terms do you want to show more?"))

print("\033[1;31;40mFinished!\33[m")

