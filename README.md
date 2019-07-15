# SimpleModel

Microservice that simulates data from external APIs (json, xml), standarize it on a object and stores it on a topic in kafka, ready to be consumed.

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
