## What the hell is this
Think of this as hidden InterProcess Communication. This is a reflection/metaprogramming based package that
takes ANY class, WITHOUT knowing ANY details, and creates stubs for its methods that redirects calls to a hidden IPC
backend that uses socket communication to call the endpoints (public function (doesn't start with _)) of each system.

## What do I do with this?
Now you can write code and not have to worry about how your systems communicate. Each class can call the other classes
functions without knowning anything. You just have to 
 
   from ROBOT_API import *

which will allow you to use any function given in your ROBOT_SYSTEMS file. 

## Why does this exist
Let's say three people write three different classes that want to work together. Now you don't have to do any setup
for those systems to work together. You just place them into this system and that will "glue" all of them together.
No constructors, no set up. You just host the classes.