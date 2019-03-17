import threading
import time
from queue import Queue

clients = []

def messageLogger(worker):
	time.sleep(0.5)
	with print_lock:
		print(threading.current_thread().name, worker)
		clients.append(str(threading.current_thread().name))
				
def threader():
	while True:
		worker = q.get()
		messageLogger(worker)
		q.task_done()

print_lock = threading.Lock()

q = Queue()
for x in range(10):
	t = threading.Thread(target=threader, daemon=True)
	t.name = "Thread" + str(x) 
	t.start()

start = time.time()
for worker in range(20):
	q.put(worker)
q.join()

print('Entire job took: ', time.time() - start)
for client in clients:
	print(client)
#thread1 =  threading.Thread(target=func1, name='func1', daemon=True)
#thread2 =  threading.Thread(target=func2, name='func2')
#thread1.start()
#thread2.start()
#thread1.join()
#thread2.join()

