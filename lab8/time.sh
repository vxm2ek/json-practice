#!/bin/bash

URL="https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85"

curl -s "$URL" > "times.json"

jq -r '.[].receiptTime' "times.json" | head -n 6

