'''
    Timer. 11/29/19
    Count the time between presses of the ENTER key.
    Show the total time counted by the timer 
    and amount of times the timer was started
'''

import time 

print("timer. made by me(timothy). ")
print("press CTRL + C to quit.")
print("")

times_started = 0
total_time = 0


try:
    while True:
        
        if times_started < 1:
            None
        elif times_started == 1:
            print("timer started 1 time.")
        else:
            print("timer started " + str(times_started) + " times.  total time is " + \
            str(round(total_time, 2)) + " seconds")
        
        key = input("press ENTER to start timer.")
        if key == "":
            times_started+=1
            key = "pressed enter"
            start_time = time.time()
            print("")
            print("timer started.")
            print("")
        else: 
            None
         
        if key == "pressed enter":
            key = input("press ENTER to stop timer.")
            if key == "":
                end_time = time.time()
                time_elapsed = round(end_time - start_time, 2)
                total_time += time_elapsed
                print("")
                print("timer stopped.")
                print("time elapsed: " + str(time_elapsed) + " seconds")
                print("")
            else: 
                None
                
except KeyboardInterrupt:
    print("")
    print("quitting...")