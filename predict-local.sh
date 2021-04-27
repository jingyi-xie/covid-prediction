#!/usr/bin/env bash

PORT=8080
echo "Port: $PORT"

# POST method predict
curl -d '{  
   "day":"400",
   "total":"1232995"
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict
