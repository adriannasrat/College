# Data Storage and Management Technologies

This course focused on core concepts of modern data storage, relational databases, spatial data modeling, scripting in Linux environments, and graph databases using Neo4j. The course included a mix of practical labs and assignments, both individual and in groups.

---

## Completed Assignments & Labs

### `Assignment`
- 	Wrote a group research report exploring five core concepts in data science and data storage:
	  1.	Differences between structured, semi-structured, and unstructured data and how they map to SQL/NoSQL systems
	  2.	Comparison of ACID, BASE, and CAP philosophies and their impact on database design
	  3.	Distinctions between Databases, Data Warehouses, Data Lakes, and Data Marts
	  4.	The role of metadata in modern data architectures
	  5.	The Inmon vs Kimball debate on Data Warehouse design
-	Included search strategy with keyword tables and database sources to ensure reproducibility
-	Report length: ~2,500–3,000 words, formatted in APA 7
-	Delivered with a recorded 10-minute group presentation summarizing findings using 8–10 slides
-	All group members contributed equally to research, writing, and presentation delivery

---

### `Lab 1 - PL/SQL Packages/`
- Developed a **PL/SQL package** in Oracle LiveSQL for secure customer management:
  - `add_customer(username, password)` – hashes password before insert
  - `get_login(username, password)` – returns 1/0 based on login success
  - `change_password(username, old_pw, new_pw)` – validates and updates password
- Packaged all logic into a `customer_security` package (spec + body)
- Submitted working code + video demo showing functionality

---

### `Lab 2 - Spatial Data/`
- Created an **information model** for spatial data using StarUML and Crow’s Foot notation
- Modeled entities such as `Route`, `Turn`, `Link`, `Node`, and spatial POIs (schools, shops, etc.)
- Coordinates stored in WGS84 format
- Delivered as an ER diagram image + video explanation

---

### `Lab 3 - Linux Lab/`
- **Part 1:** Manually created users, groups, and directories for 3 departments (HR, Sales, Engineering)
  - Set permissions, ownership, and access rules as per role
- **Part 2:** Automated the same via a **bash script** that:
  - Creates users/groups interactively
  - Sets permissions and directory ownership securely
  - Prevents duplicates and enforces logic flow
- Submitted report with screenshots, script, and explanatory video

---

### `Neo4j Lab/`
- Built a **graph database project** using Neo4j Sandbox and Cypher
  - Defined custom nodes and relationships relevant to the chosen domain
  - Wrote queries to answer real-world questions
  - Visualized the graph model and tested functionality
- Submitted full code, screenshots, and video walkthrough of model design and queries

---

## Skills Practiced

- Relational database design (ER modeling, normalization)
- SQL, PL/SQL procedures, functions, packages
- Graph modeling with Neo4j and Cypher
- Linux user/group administration & shell scripting
- UML modeling for spatial/geographic data

---

> All assignments were completed and approved. This course offered a comprehensive overview of both traditional and modern data storage technologies.
