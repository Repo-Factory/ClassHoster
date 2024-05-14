# Generic Service/Client

## Description
This is an extremely easy to use IPC strategy using sockets that can facilitate request/response architectures between various programs.
It takes advantage of dynamic typing in python to allow a flexible way of sending requests and recieving responses without having to predefine data fields.
This can be dangerous but is extremely helpful for a quick way to connect multiple processes. It also provides a generic "protocol" to communicate between these services/clients with a universal request type.


## Purpose
If you still don't see why this is so useful, consider that this allows you to

    - Communicate between processes without thinking about the details
    - "Convert" ANY class to a running process/service (it's generic!)
    - Have BUILT-IN instantiation or "startup" due the constructor of the class
    - Access functionality of services on system GLOBALLY

## How Does It Work


## File Layout

In the main directory, you'll find [client.py](main/client.py) and [server.py](main/server.py) which are the two main files you want to pay attention to. The server is run and "hosts" a callback function. If the call_service function in [client.py](main/client.py) is run, it will send a request to the server, which will cause the server call the assigned callback function with the request as a parameter and return the response to the caller. Defaults were set up so this can be seen without any setup. Run the [server.py](main/server.py) and then call it with [client.py](main/client.py) in a another terminal to see this in action.

The other files like [defaults.py](utility/defaults.py) and [req_resp.py](utility/req_resp.py) are more to ease the use or provide an example of how things may be used. Use the [services.py](config/services.py) file to define your own custom layout of services in your project. For example, think high level components of your system you want to offer on separate processes. This is like a config file that will say which port each service is run on.
