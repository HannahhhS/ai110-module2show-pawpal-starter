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
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
```

## 📐 Smarter Scheduling

PawPal+ adds four pieces of scheduling logic on top of the basic data classes. Each is a small, focused method:

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Orders tasks earliest-first by their `time` |
| Filtering | `Owner.tasks_for_pet()`, `Scheduler.build_plan()` | By pet name; completed tasks are skipped inside `build_plan` |
| Conflict handling | `Scheduler.find_conflicts()` | Flags tasks booked at the same day + time |
| Recurring tasks | `Task.next_occurrence()`, `Pet.mark_task_complete()` | Completing a daily/weekly task auto-creates the next one |

**Sorting behavior — `Scheduler.sort_by_time()`**
Returns a new list of tasks ordered earliest-first. It uses `sorted()` with a lambda key (`key=lambda t: t.time`); because times are zero-padded 24-hour `"HH:MM"` strings, they sort chronologically as plain text with no conversion needed.

**Filtering behavior — `Owner.tasks_for_pet()` and `Scheduler.build_plan()`**
`tasks_for_pet(pet_name)` filters tasks down to a single pet, returning an empty list if no pet matches (so the UI never crashes on a bad name). Filtering by completion status happens inside `build_plan()`, which skips any task whose `completed` flag is `True`.

**Conflict detection — `Scheduler.find_conflicts()`**
Compares each task against the ones after it and returns a list of plain-text warnings for any pair that shares both the same day (`due_date`) and the same start `time`. It returns a warning list rather than raising an error, so the program never crashes. Because it runs on a flat task list, it catches clashes within one pet or across different pets. (Tradeoff: it checks exact start times, not overlapping durations — see reflection.md §2b.)

**Recurring task logic — `Task.next_occurrence()` and `Pet.mark_task_complete()`**
`next_occurrence()` builds a fresh, incomplete copy of a task dated for its next repeat using `timedelta` (daily → +1 day, weekly → +7 days), and returns `None` for non-repeating frequencies. `mark_task_complete()` ties it together: it marks the task done and, if a next occurrence exists, adds it to the pet's task list so recurring care never falls off the schedule.

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
