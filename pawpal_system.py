"""PawPal+ core system — class skeletons.

Generated from diagrams/uml.mmd. These are stubs only: names, attributes,
and empty method bodies. No scheduling logic yet — that comes next.
"""

from dataclasses import dataclass, field


@dataclass
class Task:
    """A single pet care task (walk, feeding, meds, etc.)."""

    description: str
    time: str
    frequency: str
    duration_minutes: int
    completed: bool = False

    def mark_done(self) -> None:
        """Mark this task as completed."""
        self.completed = True


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


class Scheduler:
    """Builds a daily care plan from a set of tasks and constraints."""

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
