import time

wait_time = 1

max_retries = 5

attempts = 0

while attempts < max_retries:
       
    print("Attempt", attempts + 1, "- wait times  ", wait_time)
    time.sleep(wait_time)
    wait_time +=2
    attempts += 1
    if attempts == max_retries:
        print("Maximum retries reached. Exiting.")
        break
    
    
    
    
    
