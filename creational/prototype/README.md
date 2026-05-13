# Prototype

The **Prototype** pattern primary goal is to create new objects by copying an existing object, known as the _prototype_. This pattern is particularly useful when object creation is complex or resource-intensive.

At its core, the Prototype pattern relies on the concept of _cloning_. Instead of creating new objects from scratch, we create copies of existing objects. These prototypes serve as templates, allowing us to replicate their structure and attributes. When a new object is needed, we clone the prototype, saving both time and resources.

<img width="640" height="400" alt="prototype" src="https://github.com/user-attachments/assets/dd555e4e-ddd3-44fc-837e-f17dc34cf7f9" />


## Introduction

Say you have an object, and you want to create an exact copy of it. How would you do it? First, you have to create a new object of the same class. Then you have to go through all the fields of the original object and copy their values over to the new object.

There’s one more problem with the direct approach. Since you have to know the object’s class to create a duplicate, your code becomes dependent on that class. Aditionally, sometimes you only know the interface that the object follows, but not its concrete class.

### Cloning: The Key Concept

Cloning involves duplicating the state of an existing object, resulting in a new object with the same properties. The Prototype pattern typically provides two types of cloning: shallow copy and deep copy.

A _shallow copy_ replicates the top-level structure of an object but does not create copies of its nested objects. In contrast, a _deep copy_ replicates both the top-level structure and all nested objects, creating entirely independent copies.

Shallow copying is often faster and more straightforward, but it can lead to shared references within nested objects. Deep copying, on the other hand, ensures complete independence between the original and cloned objects but can be more complex and resource-intensive.

## How to recognize a builder pattern implementation?

- You see a `clone()` or `copy()` method in classes.
- Objects are created by duplicating existing instances rather than calling constructors directly.

### Real world analogy

Think of a document template in Microsoft Word. Instead of writing a document from scratch every time, you open a pre-configured template and make small adjustments. The template acts as the prototype, and each document you create is a clone.

## How to know if you can apply the pattern in your project?

You can apply the **prototype** pattern when your code should not depend on the concrete classes of the objects you need to create. Instead of instantiating new objects directly, you rely on existing instances and produce copies from them. This approach reduces coupling to specific classes and makes your system more adaptable when new object types need to be introduced.

The pattern is also a good fit when an object has a complex initialization process or configuration that would be costly to reproduce each time. By cloning a fully prepared prototype, you avoid repeating the same setup logic and improve performance while keeping object creation consistent.

Another scenario where **prototype** becomes useful is when your design would otherwise require many subclasses that only differ in the way they initialize their objects. Instead of creating separate subclasses for every variation, you can maintain a small number of prototypes with different preset states and clone them as needed, reducing class proliferation and making the codebase easier to manage.

## Key components

The **prototype** pattern typically involves the following components.

- **Prototype**. Defines the common interface for all objects that can be cloned. Usually, it declares a `clone()` method (or equivalent), which ensures that clients can duplicate objects without depending on their concrete classes.
- **Concrete Prototypes**. These are the actual classes that implement the cloning logic. Each concrete prototype overrides the `clone()` method to return a copy of itself. Depending on the needs, this may involve either a shallow copy or a deep copy of its attributes.
- **Prototype Registry (optional)**. A centralized store that holds a set of pre-configured prototypes. Clients can request a prototype from the registry and clone it, which simplifies management of different configurations.

## Benefits and Trade-offs

- ✅ Reduces cost of creating complex objects.
- ✅ Keeps object initialization logic consistent.
- ✅ Allows runtime object configuration and dynamic instantiation.
- ✅ Simplifies object creation when constructors are complicated.
- ❌ Must carefully handle _deep_ vs _shallow_ copy to avoid bugs.
- ❌ Cloning objects with external dependencies can cause issues.

## References

- 📚 [Design Patterns in Python: Prototype](https://medium.com/@amirm.lavasani/design-patterns-in-python-prototype-6aeeda10f41e)
- 📚 [Prototype](https://refactoring.guru/design-patterns/prototype)
- 📼 [What is the Prototype Design Pattern?](https://youtu.be/tqYQqSLLmEo)
