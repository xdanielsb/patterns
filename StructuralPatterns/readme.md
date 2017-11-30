# Structural   Patterns
  - Deal with delegating responsibilities to other objects.  

  * [Adapter](abstract_factory/readme.md)
    - Allows the conversion of the interface of a class to another interface that client expects. Communicate incompatible interfaces.

  * [Bridge](builder/readme.md)
    - Allows the separation of an abstract interface from its implementation.

  * [Chain of responsability](factory_method/readme.md)
    - Avoid coupling a (request) sender object to a receiver object. Allows a sender object to pass its request along a chain of objects without having any knowledge about which object will handle the request.

  * [Decorator](object_pool/readme.md)
    - Extends the functionality of an objects in a manner that is transparent to its clients without using inheritance.

  * [Facade](prototype/readme.md)
    - Provide a higher level interface to a subsystem of classes, making the subsystem easier to use.

  * [Proxy](singleton/readme.md)
    - Allows a separate object to be used as a substitute to provide controlled access to an object that is not accessible by normal means.
      - Virtual proxy: Helps to create objects on demand (until required)
      - Counting proxy: To provide some kind of audit mechanism before executing a method on a target object.
