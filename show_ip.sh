#!/bin/bash

sleep 10

IP=$(hostname -I | awk '{print $1}')

lxterminal -e "echo IP Address: $IP; bash"
