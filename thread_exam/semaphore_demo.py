"""
# @Time    : 2020/8/17 15:27
# @Author  : tmackan
"""

# Semaphore
# 适用对有限资源的限制
# 每次acquire，计数器-1，直到为0, 则阻塞

import threading

# 内部构造了condition
semaphore = threading.Semaphore()
# acquire方法
# 如果信号量非0, 则value--
# 如果信号量为0, 则wait阻塞当前线程
semaphore.acquire()
# release方法
# value++
# notify通知wait阻塞的线程
semaphore.release()




