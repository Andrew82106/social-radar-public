import os
import functools
import pickle
import hashlib
import time

try:
    from database.BaseInfo import BaseInfo
except:
    from BaseInfo import BaseInfo


class Cache(BaseInfo):
    def __init__(self):
        super().__init__()
        self.cache_path = self.cacheName

    def del_cache(self):
        cache_lst = os.listdir(self.cache_path)
        CACHE_LIST = []
        for name in cache_lst:
            cachePath = os.path.join(self.cache_path, name)
            # print(cachePath)
            if '.pkl' not in cachePath:
                continue
            CACHE_LIST.append(cachePath)
        result = []
        for I in CACHE_LIST:
            try:
                os.remove(I)
                print(f"文件 {I} 删除成功")
                result.append(f"文件 {I} 删除成功")
            except OSError as e:
                print(f"删除文件时出错: {e.filename} - {e.strerror}")
                result.append(f"删除文件时出错: {e.filename} - {e.strerror}")
        if len(result) == 0:
            result = '无缓存'
        return self.packetFormat(result)

    def cache_result(self, cache_path=None, refresh=False):
        def decorator(func):
            cache = {}
            cache_loaded = False

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                nonlocal cache_loaded
                if cache_path and not cache_loaded:
                    self.load_cache(cache, cache_path)
                    cache_loaded = True

                # 计算参数的哈希值
                key = hashlib.sha256()
                for arg in args:
                    key.update(str(arg).encode())
                for k, v in sorted(kwargs.items()):
                    key.update(str(k).encode())
                    key.update(str(v).encode())
                key = key.hexdigest()

                if key in cache and refresh is False:
                    return cache[key]
                else:
                    result = func(*args, **kwargs)
                    cache[key] = result
                    if cache_path:
                        self.save_cache(cache, cache_path)
                    return result

            return wrapper

        return decorator

    def save_cache(self, cache, cache_path):
        with open(os.path.join(self.cache_path, cache_path), 'wb') as file:
            pickle.dump(cache, file)

    def load_cache(self, cache, cache_path):
        if os.path.exists(os.path.join(self.cache_path, cache_path)):
            with open(os.path.join(self.cache_path, cache_path), 'rb') as file:
                loaded_cache = pickle.load(file)
                cache.update(loaded_cache)


if __name__ == "__main__":
    cache = Cache()
    cache.del_cache()
    exit()

    @cache.cache_result(cache_path='cache.pkl')
    def expensive_computation(n, kkk=0):
        print("Performing expensive computation...")
        time.sleep(2)
        return n * 2


    for i in range(1, 100, 2):
        print(f"i={i}:{expensive_computation(i)}")
    for i in range(1, 100, 1):
        print(f"i={i}:{expensive_computation(i)}")
    lst = [i for i in range(10)]
    lst1 = [i for i in range(11)]

    print(expensive_computation(lst))
    print(expensive_computation(lst1))
    print(expensive_computation(lst, 1))
    print(expensive_computation(lst1, 1))
    print(expensive_computation(lst, 0))
    print(expensive_computation(lst1, 1))
