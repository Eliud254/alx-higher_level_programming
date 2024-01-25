#!/bin/bash
# script that takes in a URL, sends a request to that URL
curl -sI "$1" | awk '/Content-Length/{print $2}'
