# Project-Based System Development (GIK2PG) – Escape Room

This folder contains my work and reflections from the *Project-Based System Development* course within the System Science program at Dalarna University. The course was conducted as a live development project in collaboration with **Trafikverket** (The Swedish Transport Administration).

**[Click here to access the final project repository with all source code](https://github.com/5umic/escapeRoom)**

---

## Project Description
The objective was to design and develop a digital "Escape Room" tailored for Trafikverket's educational and career fair events. The purpose of the application was to engage students and spread knowledge about Trafikverket’s operations through various mini-games and quizzes. 

The game was divided into two main tracks: one tailored for university students and one for high school students. I was part of the development team responsible for building and structuring the **high school version**.

### Technical Stack
* **Frontend:** React (JavaScript) / HTML5 / CSS3
* **Backend:** C# / .NET Web API
* **Database:** Entity Framework Core
* **Tools:** GitHub (Version Control), Trello (Backlog/Agile Planning), Miro (UI/UX Sketches), Zoom (Collaboration/Pair Programming).

---

## My Individual Contributions & Features
In this project, I took on the role of **software developer and programmer**, focusing particularly on building a robust, cheat-proof game engine and a flexible administrator interface.

My main technical contributions include:

### 1. Robust Game Engine & Timer (`useGameTimer`)
* **Global Time Tracking:** Implemented a central React hook to handle game time and synchronize it across all mini-games.
* **Penalty Time System:** Built logic that automatically adds penalty seconds to the player's total time upon incorrect answers, creating the intended game mechanics and element of stress.
* **Anti-Cheat ("The Caretaker"):** Developed a session-based restriction using `sessionStorage`. If a player attempts to manipulate the game by going back, refreshing the page, or typing in URL paths directly to later stages, the broken session is detected, and the player is redirected back to the start screen.

### 2. Smart JSON Editors in Admin Dashboard
* To allow Trafikverket’s staff to manage complex sorting games without any programming knowledge, I refactored the raw JSON text box into a user-friendly form.
* The admin inputs categories and words through simple text fields and buttons, while the frontend automatically validates and "packs" the data into a perfectly formatted JSON string in the background before saving it to the database.

### 3. Integrated Media Library (`ImageGallery.jsx`)
* Developed a dedicated gallery page for administrators.
* Implemented functionality to upload new files, list existing images via API endpoints in .NET, delete incorrect files from the server, and created a "click-to-copy" feature that immediately copies the exact image URL to the clipboard for smoother content management.

---

## Lessons Learned & Reflections
This project provided invaluable insight into how software development works in practice and how to handle scope changes based on client feedback. 

Technically, I gained a deeper understanding of state management in React, version control and merge conflict resolution in Git, and the importance of strict data validation between client and server. The project also proved that good communication and daily syncs within the development team are absolutely vital for successfully integrating different subsystems in the final stages.
