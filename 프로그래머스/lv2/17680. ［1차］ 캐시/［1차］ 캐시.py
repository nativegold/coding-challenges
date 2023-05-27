def solution(cacheSize, cities):
    running_time: int = 0
    cache_hit: int = 1
    cache_miss: int = 5
    cache = []

    for city in cities:
        city_lower = city.lower()

        if city_lower in cache:     # 캐시에 있을 경우
            running_time = running_time + cache_hit

            cache.remove(city_lower)
            cache.append(city_lower)
        else:   # 캐시에 없을 경우
            running_time = running_time + cache_miss

            if cacheSize != 0:
                if len(cache) == cacheSize:     # 캐시가 가득 찼을 경우
                    cache.pop(0)

                cache.append(city_lower)

    return running_time