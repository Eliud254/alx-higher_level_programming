#!/bin/bash
# Sends the  request to a URL passed as an argument.
curl -s -o /dev/null -w "%{http_code}" "$1"#!/bin/bash
