# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```
=== Today's Schedule ===
  08:00  Morning feeding (10 min)
  08:15  Litter box scoop (5 min)
  08:30  Long walk (45 min)
  09:30  Give meds (5 min)

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
py -m pytest

# Run with coverage:
pytest --cov
These tests cover core logic of the system, including scheduling tasks, adding pets, etc. It checks for conflict detection, sorting, filtering. It ensures the core functions work as expected, including edge cases, like no pets. 
```

Sample test output:

```
# collected 6 items                                                                                                                                              

tests\test_pawpal.py ......                                                                                                                              [100%]

====================================================================== 6 passed in 0.05s ======================================================================
Confidence label of 4. 
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | Scheduler.sort_by_time()| sort by time, in increasing order |
| Filtering | Owner.tasks_for_pet() | filter tasks by pet name, so person can view tasks for just one pet in time order|
| Conflict handling |Scheduler.find_conflict() | flag a conflict warning of 2 tasks start at same time and day |
| Recurring tasks | Task.next_occurance() | automatically create another task due the next day for repeating tasks|

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

UI has sectuons to add a pet, add a test, and build a schedule. 

Scheduling behavuors, such as conflict detection, are shown as a flag feature before generating the schedule. Results from the generate schedule are automatically sorted. 

Sample main.py

=== Conflict check ===
  WARNING: Conflict at 08:30: 'Playtime' overlaps with 'Long walk'.
=== Rex's tasks only ===
  08:30  Long walk
  09:30  Give meds
=== Mochi's tasks only ===
  08:00  Morning feeding
  08:15  Litter box scoop
  08:30  Playtime
=== Complete Rex's daily walk ===
  Marked 'Long walk' done: True
  Auto-created next 'Long walk' due 2026-07-08
=== Rex's tasks after completion ===
  [done] 08:30  Long walk  (due 2026-07-07)
  [todo] 09:30  Give meds  (due 2026-07-07)
  [todo] 08:30  Long walk  (due 2026-07-08)
=== Today's Schedule ===
  08:00  Morning feeding (10 min)
  08:15  Litter box scoop (5 min)
  08:30  Playtime (15 min)
  08:30  Long walk (45 min)
  09:30  Give meds (5 min)

1. <!-- User firsts adds their name, and a pet. User can add details like the name, age and species for a pet -->
2. <!-- User can choose a specific pet, and schedule a task for that pet.  -->
3. <!-- User can then generate a schedule that includes all the tasks for all the pets. This is displayed in a table.   -->
4. <!-- User views the completed table that is sorted aoccrding to time. -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
