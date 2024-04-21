import multiprocessing as mp
import time

"""function f(x)"""

def f(x):
    time.sleep(6)
    res = x > 0
    return res

"""function g(x)"""

def g(x):
    time.sleep(7)
    res = x < 0
    return res

"""Main"""

if __name__ == '__main__':
    pool = mp.Pool(processes=2)
    resx = pool.apply_async(f, args=(6,))
    resg = pool.apply_async(g, args=(-1,))
    finished_x = False
    finished_g = False
    dont_ask = False
    ask_time = 5
    last_ask_time = time.time()
    while True:
        """Ask user if he wants to continue"""
        if not dont_ask and time.time() - last_ask_time > ask_time:
            last_ask_time = time.time()
            answer = input("Do you want to continue? [ y / n / d(don't ask me again) ]")
            if answer == 'n':
                print('Program stopped by user')
                pool.terminate()
                break
            if answer == 'd':
                print('Program will not ask again')
                dont_ask = True
                
        """&&"""
        if finished_x and finished_g:
            print('Program returned True')
            break
        
        """Check result f(x)"""
        if not finished_x and resx.ready():
            finished_x = True
            if not resx.get():
                print('Program returned False')
                pool.terminate()
                break
            
        """Check result g(x)"""
        if not finished_g and resg.ready(): 
            finished_g = True
            if not resg.get():
                print('Program returned False')
                pool.terminate()
                break