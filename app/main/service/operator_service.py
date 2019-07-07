import redis
import base64
from app.main.model.tour import Tour
from app.main.util.kafka import Producer, Consumer


cache = redis.Redis(host='redis', port=6379)
producer = Producer()
consumer = Consumer()

def save_tours(data):
    for val in data:
        t = Tour(val['id'], val['name'], val['duration'], val['description'], val['availability'])
        tour_cached = cache.get(t.id)
        if tour_cached is None:
            cache.set(t.id, base64.b64encode(t.toJSON().encode('utf-8')))
            producer.send('tour', t.toJSON())
        else:
            if tour_cached != base64.b64encode(t.toJSON().encode('utf-8')):
                cache.set(t.id, base64.b64encode(t.toJSON().encode('utf-8')))
                producer.send('tour', t.toJSON())
    return 'Everything imported', 201

def get_tour():
    return consumer.consume(), 200