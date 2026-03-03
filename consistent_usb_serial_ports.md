## Basics
The so_follower and so_leader each connect to the controlling computer via usb. Your computer will assign each one of these a port, which can be found with the LeRobot helper script lerobot-find-ports.

## Problem
Order that the ports are assigned can change.  You can boot your computer and find the leader arm on /dev/ttyACM1 one day, and /dev/ttyACM0 the next.  Getting them wrong can lead to wasted time and unnecessary debugging.

## Solution (Linux)
Try this on your command line (with at least one of the arms plugged in to usb):
```shell
ls /dev/serial/by-id
```
This uses the unique device ID's to index the serial devices.  The device id's are long and ugly, but the upshot is that they don't change.  So you can do this one time and throw them into your scripts, or in environment variables to be set in a bash startup script, for example.
