import redis
r = redis.Redis(host="192.168.10.125",port=6379,password="Citory2022",db=6)
r.lpush("mfw:start_urls","https://www.mafengwo.cn/hotel/8299351.html?iMddid=10099")
