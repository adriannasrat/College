# Personalregister – Digital Personnel Register

This project was developed as part of the *Object-Oriented Design and Problem Solving* course.  
The task was to design and implement a **digital personnel register** for a company with more than **500,000 worker ants**.

---

## Project Description

The client requested a system to manage their large workforce of ants.  
The requirements were:

- Ability to **add, remove, search, and update** personnel records  
- Simulation of **lifespans**: ants live for only 2 weeks, but more ants are born every week  
- Storage in a **non-RDBMS** format (e.g., JSON, in-memory) because of security concerns with traditional databases  
- Extensibility to later include **bees** as employees  

---

## Implementation Highlights

- **Abstract Factory Pattern**:  
  - One factory for creating **ants**  
  - One factory for creating **bees**  
  - Each species is encapsulated in its own class hierarchy, making the system easy to extend

   ![Factory Method Design Pattern](./Projekt/factory-method-design-pattern-.webp)

- **SOLID Principles Applied**:  
  - Classes have single, clear responsibilities  
  - The design is open for extension (new species) but closed for modification  
  - Consistent use of interfaces ensures flexibility  

- **Persistence Layer**:  
  - Data is stored in **JSON files** for durability and simplicity  
  - Avoids the risks of conventional RDBMS while ensuring fast access  

- **Simulation Features**:  
  - Weekly lifecycle management: births and deaths are automatically handled  
  - More ants are always born than die, ensuring the workforce grows  

---

## Conclusion

Thanks to the **Abstract Factory Pattern** and proper object-oriented design, this system is:  

- Scalable (new species can be added easily)  
- Maintainable (clear separation of concerns)  
- Robust (persistent storage without relying on vulnerable RDBMS)  

It showcases how **design principles and patterns** can solve complex, real-world inspired problems.
