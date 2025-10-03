#!/bin/bash
amount=$(find /etc -type f | wc -l)
echo "The amount of files is: $amount"
