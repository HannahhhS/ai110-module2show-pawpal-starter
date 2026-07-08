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
My scheduler considers the time, and preferences such as the start time. If a task is scheduled before the users preferred start time, then it is not includeded. These constraints mattered most becuase it was something the user themselves has specified, so it is important to keep track off. 

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff my scheduler makes is in how it detects conflicts. The find_conflicts method only flags two tasks as conflicting when they start at the exact same time on the same day (same "HH:MM" and same due date). It does not look at each task's duration, so it won't catch two tasks that overlap unless it starts at the same time. For example, a 45-minute walk at 08:30 and a feeding at 09:00 actually overlap in real life, the schedular doesnt mark the conflict. 

I think this tradeoff is reasonable for this scenario because it keeps the logic lightweight and easy to read, and it returns a simple warning message instead of crashing. For a single pet owner planning a day, exact same-time clashes are the most obvious and most common mistake, so catching those covers the main case. A

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
I used the AI tools for refactoring and debugging. At the beginning of the process, I spent time brainstorming on my own without using the AI. I then checked with the AI to see any feedback it gave, and updated some of my plans accordingly. Asking questions about why a peice of code was added or needed helped to improve my understanding of the code the AI gave and the overall process. prompts that were specific and referenced certain files and such also seemed helpful. 

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
When creating the conflict detection method, the AI suggestion for the method originally only checked for conflicts at the same time. This would be flagging things as a conflict even if the tasks were scheduled for different days. I rejected the original AI version and asked it to also check for the same day, as a conflict only occurs on the same day or time. This involved actually examining and testing the code to see what the AI did. I also changed some of what AI did for creating a new task and had it assign the date as todays date instead of an empty date. 

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
The behaviors that i tested were the main scheduling edge cases we built, such as sorting, filtering, conflict detection, and recurring tasks. Other basic tasks incude making sure a pet is correctly added and the count increases, and making sure the code works even with no pets. These tests are important as it actually tests all of the edge case functionality that was built, in order to ensure everything works as anticipated. 

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
I am quite confident that the scheduling works correctly, as I was able to test all of the main features that were implemented. Next time, I would check more with adding a new pet in between the session, and see if there are any conflicts with the time and such if a session is refreshed. 

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I am most satisfied with how the core logic and everything came together. The app works as intended, allowing the user to add multiple pets, multiple tasks for the pet, and viewing the tasks. The UI is also integrated smoothly which is good. 

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
I would want to work on the UI more and make it more user friendly. I also want to be able to add more buttons and things, like a button for the user to easily check off a task, and a button to view completed tasks. 

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
I learned that AI code is very helpful, but it should not be taken as face value. The lead architect always needs to look at and understand the code and make changes as needed. 
