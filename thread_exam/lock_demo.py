"""
# @Time    : 2020/8/17 11:03
# @Author  : tmackan
"""
import threading
import urllib3

http = urllib3.PoolManager()


class FetchUrls(threading.Thread):
    def __init__(self, urls, output, lock):
        super(FetchUrls, self).__init__()
        self.urls = urls
        self.output = output
        self.lock = lock

    def run(self):
        while self.urls:
            url = self.urls.pop()
            try:
                req = http.urlopen("GET", url)
            except Exception as e:
                print("URL %s failed %s" % url, e)
                return
            # 获取不到锁, 则阻塞等待释放
            self.lock.acquire()
            print('lock acquired by %s' % self.name)
            msg = "URL %s fetched by %s\n" % (url, self.name)
            self.output.write(msg)
            print("URL %s fetched by %s" % (url, self.name))
            self.lock.release()
            print('lock release by %s' % self.name)


def main():
    urls1 = ["http://www.baidu.com"]
    urls2 = ["http://www.weibo.com"]
    f = open('output.txt', 'w+')
    lock = threading.Lock()
    rlock = threading.RLock()

    t1 = FetchUrls(urls1, f, lock)
    t2 = FetchUrls(urls2, f, lock)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    f.close()


if __name__ == "__main__":
    main()
