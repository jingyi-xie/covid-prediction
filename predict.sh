#!/usr/bin/env bash

# POST method predict
curl -d '{  
   "day":"400",
   "total":"1232995"
}'\
     -H "Content-Type: application/json" \
     -X POST https://covid-prediction-311000.uc.r.appspot.com/predict