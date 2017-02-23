# whoshome
Small tool to poll my home network and find out who's home


## What is it?
whoshome is a python script I smashed together to discover which of my housemate's devices are connected to the home network.
It then creates a basic html file and transfers it to the directory I've set ngnix to serve as a webpage.
Currently I have cron running it every five minutes.

It's basic, ugly as sin, but works.

### Future plans
- get MAC addresses of all housemate's devices
- Make it less shit (the Python code)
- Add css to make it less ugly
- Implement a last seen
  - because mobile devices like to turn off wifi in sleep mode
- Instead of listing each device, create a probability of being home?
