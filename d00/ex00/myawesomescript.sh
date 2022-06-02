#!/bin/sh

curl -# -I $1 | grep "location: " | cut -c 11-
