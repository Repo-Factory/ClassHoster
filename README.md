# Generic Service/Client API System

## Description
This is an extremely easy to use IPC strategy using sockets that can facilitate request/response architectures between various programs.
It provides a flexible way of sending requests and recieving responses between processes and provides a generic "protocol" to communicate with a universal request type. In other words, it's a way to glue various systems together without separate systems having to plan for it. It's a generic way to connect various pieces (components) into one system (robot).

## Explanation
This uses python sockets for IPC and the pickle package for dynamic serialization of requests/responses. The generic server uses python reflection and expanded dictionary args (kwargs) to make a dynamic API. 

The basic idea is that we want to make a generic request to some port, and have the server hosting that port run a specific piece of code for us. The way we can do this is base our server around a class. Every python class has a getattr function which allows us to get any function attached to that class. Then we can pass in any number of keyword arguments. 

This allows us to "host" different robotic systems on different ports. So we could say, 
    
    sensor X ---> port 5000, 
    motor control ---> port 5001
    camera ---> port 5002
    
Then if we want to ask one of those systems to perform a task, we just send a generic request (so always the same type of request) to the associated port, and it will call the appropriate code. We don't have to plan those systems at all beforehand to work with this system, it uses python's builtin tools to "host" a python class on a port. The generic request looks something like this

    call_service(port=1000, // You should give this a system name instead of port number in the config file
                request=GenericRequest(
                    function="move", 
                    args={"distance": 1}
    ))

This is assuming some kind of control system is on port 1000 which has a function called move that takes a distance parameter. This would tell the system to move 1 meter for example. The generic server will receive the request and call control_system.move(distance=1) using reflection.

## Purpose
If you still don't see why this is so useful, consider that this allows you to

    - Communicate between processes without thinking about the details
    - "Convert" ANY class to a running process/service (it's generic!)
    - Have BUILT-IN instantiation or "startup" due the constructor of the class
    - Access functionality of services on system GLOBALLY

## How Does It Work
This is the very simple code for processing a generic request

    def generic_callback(request: GenericRequest, object): 
        function_call = getattr(object, request.function)
        return function_call(**request.args)

As you can see this will always return whatever the function call returns, and because of python's dynamic typing you can get a response from any of the requests without any extra work. For example, if you had a service that added three numbers, you could send it 10, 20, 30 and it will send you back 60. You don't have to worry about how the IPC sends/receives this. You're welcome.

## File Layout

In the main directory, you'll find [client.py](main/client.py) and [server.py](main/server.py) which are the two main files you want to pay attention to. The server is run and "hosts" a callback function. If the call_service function in [client.py](main/client.py) is run, it will send a request to the server, which will cause the server call the assigned callback function with the request as a parameter and return the response to the caller. Defaults were set up so this can be seen without any setup. Run the [server.py](main/server.py) and then call it with [client.py](main/client.py) in a another terminal to see this in action.

Another very important file is the [gen_srv.py](main/gen_srv.py) which is the way to make a class use this server/client architecture with a generic request. You can set up your own class with the generic server using this code 

    #!/usr/bin/env python3

    from custom_system import CustomSystem 
    from services import ServiceNames, ServicePorts
    from gen_srv import start_generic_server

    if __name__ == "__main__":
        start_generic_server(ServiceNames.CUSTOM, ServicePorts[ServiceNames.CUSTOM], CustomSystem) 

Fill this with the details of your custom service

The other files like [defaults.py](utility/types/defaults.py) and [req_resp.py](utility/types/req_resp.py) are more to ease the use or provide an example of how things may be used. Use the [services.py](tools/host_cls_client.py) file to define your own custom layout of services in your project. For example, think high level components of your system you want to offer on separate processes. This is like a config file that will say which port each service is run on.

## Author
[Conner Sommerfield](https://github.com/repo-factory)