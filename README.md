*New version as of 26/02/17. Need to update this properly.*


# whoshome
Small tool to poll my home network and find out who's home.

See the action [here](http://rhysdeimel.ddns.net)


## What is it?
whoshome is a python script I smashed together to discover which of my housemate's devices are connected to the home network.
It then creates a basic html file and transfers it to the directory I've set ngnix to serve as a webpage.
Currently I have cron running it every five minutes.

It's basic, ugly as sin, but kinda works.

### Future plans
- get MAC addresses of all housemate's devices
- Make it less shit (the Python code)
- Add css to make it less ugly
- Implement a last seen
  - because mobile devices like to turn off wifi in sleep mode
- Instead of listing each device, create a probability of being home?

*So this has problems with mobile devices that turn off wifi when they sleep. I'm going to have to rewrite this using ping because that seems to wake them up*
