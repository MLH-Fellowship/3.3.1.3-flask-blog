#!/bin/bash

#get the status code 
curl -i https://jobegiar99.duckdns.org | head -n 1 | grep " \w* " -o | grep -o  "\w*" > httpStatusCode.txt

$(sudo ./endpointTestHelper "https://jobegiar99.duckdns.org" "homepage" )
