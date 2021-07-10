def solution(cacheSize, cities):
    runTime = 0
    cache = []
    
    for city in cities:
        runTime += LRU(cacheSize, cache, city)
    
    return runTime

def LRU(cacheSize, cache, city):    
    # cache hit
    if city in cache:
        cache.pop(cache.index(city))
        cache.append(city)
        
        return 1
    
    # cache miss
    else:
        if len(cache) < cacheSize:
            cache.append(city)
        else:
            if cacheSize != 0:
                cache.pop(0)
                cache.append(city)
                
        return 5

solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])