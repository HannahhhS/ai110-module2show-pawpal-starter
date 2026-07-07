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
        pass


@dataclass
class Pet:
    """A pet and the care tasks that belong to it."""

    name: str
    age: int
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a care task to this pet."""
        pass

    def list_tasks(self) -> list[Task]:
        """Return this pet's tasks."""
        pass


@dataclass
class Owner:
    """A pet owner, their preferences, and the pets they own."""

    name: str
    preferences: dict = field(default_factory=dict)
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner."""
        pass

    def set_preference(self, key: str, value) -> None:
        """Set a single owner preference."""
        pass


class Scheduler:
    """Builds a daily care plan from a set of tasks and constraints."""

    def build_plan(self, tasks: list[Task], available_minutes: int, start_time: str) -> list[Task]:
        """Choose and order tasks into a day's plan within the time budget."""
        pass
