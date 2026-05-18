---
title: Creational Patterns
nav_order: 1
has_children: true
---

# Creational Patterns

![Category](https://img.shields.io/badge/category-creational-blue)

Creational patterns deal with **how objects are created**. At first glance, instantiating a class with `ClassName()` seems trivial. As systems grow, hardcoding which class gets created and how it gets configured leads to rigid, tightly-coupled code that is hard to test and even harder to extend.

Creational patterns solve this by moving the responsibility of object creation behind an interface. The rest of your code just asks for an object without needing to know the exact class, the construction steps, or whether it is getting a fresh instance or a shared one. This separation makes it straightforward to swap implementations, introduce new variants, or control resource-heavy instantiation without touching the code that uses those objects.

- [Builder](./builder/) — Construction of complex or multi-representational objects
- [Singleton](./singleton/) — Only one existing instance of a class
- [Prototype](./prototype/) — Create new objects by copying an existing object
- [Factory Method](./factory-method/) — Delegate object creation to subclasses via a factory method
