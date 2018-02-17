import redis
import config as cfg

redis_client = redis.StrictRedis(host=cfg.redis['host'], port=cfg.redis['port'], db=0)
