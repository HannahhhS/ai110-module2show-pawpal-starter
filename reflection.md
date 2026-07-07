# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
3 core actions a user shiuld be able to perform include adding a pet to the database, adding a new task and viewing those tasks, and scheduling and organizing things like walks, meds, appointments, etc. 
Pet - name, age, species. Can complete a walk, "eat" a meal, etc
Owner - name, preferences. Can add a pet
Task - walks, feedings, meds
Scheduler - schedule a walk, meal schedule, med schedule
- What classes did you include, and what responsibilities did you assign to each?
The classes that I included for this are Owner, Pet, Task, and Scheduler. The Owner has the ability to add a pet and set any preferences. The Pet class is abke to add a task that is specific to that pet, and return a list of tasks for that pet. Task includes attributes like description, time frequency, and duration. This has a mark_done responsiblity to mark the task as done. The scheduler is able to build a schedule plan based on tasks and available time. 

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
I did make design changes, especially when planning out the classes and attributes. Originally, i had kept the tasks in pet very specific, so it had methods like complete walk and eat meal. In the scheduler, I had metjods like "schedule walk" and schedule meal. Based on AI feedback, I made a build_plan in schedular to build a plan based on any task. The Tasks in pet are not specific tasks like eat or walk, but rather there is space for a description of what the task is. Any task, wether eat, walk, or meds, can be added using add_task for that pet, insread of scheduling things individually. 

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
