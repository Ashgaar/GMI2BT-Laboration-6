import numpy as np
import concurrent.futures
import time
import random
import multiprocessing
import psutil


number = 4294967295
cpu_count = psutil.cpu_count(logical=True)
variable = random.randint(1, number)


# sec_key = np.uint32(variable)
# bara för att testa om man inte vill vänta
sec_key = np.uint32(100000)




def init_globals(key_not_found):
    global KEY_NOT_FOUND
    KEY_NOT_FOUND = key_not_found


def main():
    print(f'Random secret key is: {sec_key}')
    print(f'The cpu count is: {cpu_count}')
    
    
    start_key = []
    end_keys = []
    cpus_list = []
    key_range = int(number/cpu_count)
    
    
    for i in range (0, cpu_count):
        cpus_list.append(i+1)
        start_keys = i * key_range
        start_key.append(start_keys)
        if i == cpu_count - 1:
            end_key = number
        else:
            end_key = (i + 1) * key_range
        end_keys.append(end_key)

    print(f'Start keyspace offsets: {start_key}')
    print(f'End keyspace offsets: {end_keys}')

    key_not_found = multiprocessing.Value('i', True)
    
    start_timer = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers = cpu_count, initializer = init_globals, initargs = (key_not_found,)) as executor:
        for i in executor.map(crack_something, cpus_list, start_key, end_keys):
            print(i)
            executor.shutdown()
    stop_timer = time.perf_counter()
    
    time_spent = stop_timer - start_timer
    keys_tested = sec_key * cpu_count
    whole_keyspace_tested = (number / (keys_tested / time_spent)) * time_spent
    print(f'Finished cracking in {time_spent:0.2f} seconds')
    print(f'Around {keys_tested/time_spent:0.0f} keys per second were tested')
    print(f'To brute for the whole keyspace it would take around {whole_keyspace_tested:0.0f} seconds')
    
    
def crack_something(cpu, cur_key, end_key):
    print(f'CPU: {cpu} keyspace start at {cur_key} and end at {end_key}')
    
    while KEY_NOT_FOUND.value and (cur_key <= end_key):
        if(cur_key == sec_key):
            KEY_NOT_FOUND.value = False
            return f'CPU: {cpu} found the secret key. Current key: {cur_key}. Secret key: {sec_key}'
        else: cur_key = cur_key + 1
    return f'CPU: {cpu} reached key: {cur_key}'
    
    
if __name__=='__main__':
    main()