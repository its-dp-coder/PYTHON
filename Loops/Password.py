#Implement an exponential backoff strategy for retrying a failed operation. The backoff time should double with each retry attempt, starting from 1 second, and should have a maximum limit of 32 seconds. The operation should be retried up to 5 times before giving up.
import time
wait_time=1
max_retries=5
attempts=0
while attempts <max_retries:
    print("Attempt", attempts + 1, "- wait time", wait_time, )
    time.sleep(wait_time)
    wait_time *=2
    attempts +=1