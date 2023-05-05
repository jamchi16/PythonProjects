import time


timer_start = int(input("Set timer length in seconds: "))

print(f'{timer_start}')

time.sleep(1)

while timer_start >> 1:
    timer_start = timer_start - 1
    print(f'{timer_start}')
    time.sleep(1)

print("Beep Beep Beep")

