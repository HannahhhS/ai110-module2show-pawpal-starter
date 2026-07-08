"""PawPal+ core system — class skeletons.

Generated from diagrams/uml.mmd. These are stubs only: names, attributes,
and empty method bodies. No scheduling logic yet — that comes next.
"""

from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class Task:
    """A single pet care task (walk, feeding, meds, etc.)."""

    description: str
    time: str
    frequency: str
    duration_minutes: int
    completed: bool = False
    # ISO "YYYY-MM-DD" the task is due. Defaults to today; pass an explicit
    # date to schedule a task for a future day. default_factory (not a plain
    # default) so each task gets the *current* day at creation time, not the
    # day this module was first imported.
    due_date: str = field(default_factory=lambda: date.today().isoformat())

    def mark_done(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def next_occurrence(self) -> "Task | None":
        """Build the next repeat of this task, or None if it doesn't repeat.

          daily  -> due today + 1 day
          weekly -> due today + 7 days
          anything else (e.g. "monthly", one-off) -> None

        timedelta does the date math so month/year rollovers are handled
        for us (e.g. 2026-07-31 + 1 day -> 2026-08-01). The new task is a
        fresh, incomplete copy with its due_date moved forward.
        """
        if self.frequency == "daily":
            step = timedelta(days=1)
        elif self.frequency == "weekly":
            step = timedelta(weeks=1)
        else:
            return None

        next_date = date.today() + step
        return Task(
            description=self.description,
            time=self.time,
            frequency=self.frequency,
            duration_minutes=self.duration_minutes,
            completed=False,
            due_date=next_date.isoformat(),
        )


@dataclass
class Pet:
    """A pet and the care tasks that belong to it."""

    name: str
    age: int
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a care task to this pet."""
        self.tasks.append(task)

    def list_tasks(self) -> list[Task]:
        """Return this pet's tasks."""
        return self.tasks

    def mark_task_complete(self, task: Task) -> "Task | None":
        """Mark a task done and auto-schedule its next occurrence.

        For a daily/weekly task this creates a fresh copy dated for the
        next time and adds it to this pet's list, so recurring care never
        falls off the schedule. Returns the new task (or None if the task
        doesn't repeat).
        """
        task.mark_done()
        upcoming = task.next_occurrence()
        if upcoming is not None:
            self.add_task(upcoming)
        return upcoming


@dataclass
class Owner:
    """A pet owner, their preferences, and the pets they own."""

    name: str
    preferences: dict = field(default_factory=dict)
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner."""
        self.pets.append(pet)

    def set_preference(self, key: str, value) -> None:
        """Set a single owner preference."""
        self.preferences[key] = value

    def all_tasks(self) -> list[Task]:
        """Return every task across all of this owner's pets.

        This is how the Scheduler gets its data: instead of reaching into
        each pet's task list itself, it asks the Owner for one flat list.
        """
        tasks: list[Task] = []
        for pet in self.pets:
            tasks.extend(pet.tasks)
        return tasks

    def tasks_for_pet(self, pet_name: str) -> list[Task]:
        """Return just one pet's tasks — the "filter by pet name" view.

        Walks the owner's pets, and when it finds the one whose name
        matches, hands back that pet's task list. Returns an empty list
        if no pet has that name.
        """
        for pet in self.pets:
            if pet.name == pet_name:
                return pet.tasks
        return []


class Scheduler:
    """Builds a daily care plan from a set of tasks and constraints."""

    @staticmethod
    def sort_by_time(tasks: list[Task]) -> list[Task]:
        """Return the tasks ordered earliest-first by their start time.

        Uses sorted() with a lambda key that pulls each task's `time`.
        Zero-padded "HH:MM" strings compare in chronological order as
        plain text (e.g. "08:00" < "09:30"), so no conversion is needed.
        sorted() returns a new list and leaves the input untouched.
        """
        return sorted(tasks, key=lambda t: t.time)

    @staticmethod
    def find_conflicts(tasks: list[Task]) -> list[str]:
        """Return a warning for every pair of tasks sharing the same time.

        Lightweight and non-crashing: it compares each task with the ones
        after it and, when two land on the same day AND the same "HH:MM",
        adds a plain-text warning to the list. Matching the day matters —
        an 08:30 task today and an 08:30 task tomorrow don't clash. An
        empty list means no conflicts. Because it runs on a flat task list,
        it catches clashes whether the tasks belong to the same pet or to
        different pets.
        """
        warnings: list[str] = []
        for i, first in enumerate(tasks):
            for second in tasks[i + 1:]:
                same_day = first.due_date == second.due_date
                if same_day and first.time == second.time:
                    warnings.append(
                        f"Conflict at {first.time}: "
                        f"'{first.description}' overlaps with '{second.description}'."
                    )
        return warnings

    def build_plan(self, tasks: list[Task], available_minutes: int, start_time: str) -> list[Task]:
        """Choose and order tasks into a day's plan within the time budget.

        Rules:
          1. Skip tasks that are already completed — no need to plan them.
          2. Only include tasks scheduled at or after `start_time`.
          3. Do earlier tasks first (sorted by their `time`).
          4. Add tasks until the time budget runs out; skip ones that don't fit.

        `time` and `start_time` are expected as 24-hour "HH:MM" strings
        (e.g. "08:00"), which sort correctly as plain text.

        Returns the ordered list of tasks that made it into the plan.
        """
        # Rules 1 & 2: only plan tasks that still need doing and aren't too early.
        pending = [t for t in tasks if not t.completed and t.time >= start_time]

        # Rule 3: earlier tasks first.
        pending.sort(key=lambda t: t.time)

        # Rule 4: greedily fit tasks into the available time budget.
        plan: list[Task] = []
        remaining = available_minutes
        for task in pending:
            if task.duration_minutes <= remaining:
                plan.append(task)
                remaining -= task.duration_minutes

        return plan
