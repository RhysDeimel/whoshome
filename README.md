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
- Make it less shit (the Python code)
- Add css to make it less ugly
- Instead of listing each device, create a probability of being home?

*So this has problems with apple devices because they like to turn their wifi off and not respond to ping. Need to figure out a work around. Maybe another script to keep them alive?*
