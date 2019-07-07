# TourModel

Microservice that simulates data from operators APIs (json, xml), normalizes it on a object and stores it on a topic in kafka, ready to be consumed.

## Run
To run the service:
- docker-compose up 

## Swagger
- http://localhost:5000/

## Checking kafka topics
Install kafkacat to check your topic after calling operators endpoints:
- apt-get install kafkacat

Execute to view topic info
- kafkacat -b localhost:9092 -C -t tour

### Questions we ask you to answer:
1. What problems do you identify in the current setup? Please enumerate them with a brief
description of why you believe they are problems, and what risks they carry.
- I think that the importer service should have a cache to avoid not necessary data.
- The idea of using a DB (Tourfiles) that trigger a message into a queue can be replaced for sending directly the data to kafka.
2. What new architecture would you suggest that optimizes for performance, scalability, and
reliability?
- I would remove the Tourfiles db and produce the data directly to the queue.
- Implement a cache system like redis to obtain only necessary data.
- Develop a microservice that download the images from the operators to resize and upload to S3 avoid operators host.
3. How would you ensure your chosen architecture is working as expected?
- Ensuring that the data from the externals APIs is normalized and can be inserted in Website DB as soon as possible.