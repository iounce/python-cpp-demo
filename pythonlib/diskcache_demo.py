from diskcache import Cache
import time

if __name__ == "__main__":
    cache = Cache('cache')
    cache.set('name', 'Jack')
    cache.set('name', 'Jack2')
    name = cache.get('name')
    print(name)
    
    cache.set('id', 123, expire=3)
    value = cache.get('id')
    print('before expire: ', value)
    time.sleep(3)
    value = cache.get('id')
    print('after expire: ', value)
    
    cache.set('price', 6.66)
    value = cache.get('price')
    print('before expire: ', value)
    cache.touch('price', expire=2)
    time.sleep(3)
    value = cache.get('price')
    print('after expire: ', value)
    
    cache.delete('id')
    cache.clear()