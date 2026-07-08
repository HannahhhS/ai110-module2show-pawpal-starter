"""Tests for PawPal+ core classes.

Run from the project root with:  pytest
"""

import sys
from datetime import date, timedelta
from pathlib import Path

# Let this test (inside tests/) import pawpal_system.py from the project root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pawpal_system import Pet, Scheduler, Task


def test_task_completion():
    """Calling mark_done() should flip the task's completed status to True."""
    task = Task("Morning walk", "08:00", "daily", 20)
    assert task.completed is False  # starts incomplete

    task.mark_done()

    assert task.completed is True


def test_adding_task_increases_pet_task_count():
    """Adding a task to a Pet should grow that pet's task list by one."""
    pet = Pet("Mochi", 3, "cat")
    assert len(pet.tasks) == 0  # starts with no tasks

    pet.add_task(Task("Morning feeding", "08:00", "daily", 10))

    assert len(pet.tasks) == 1


def test_pet_with_no_tasks_returns_empty_list():
    """A brand-new pet has no tasks, so list_tasks() returns an empty list."""
    pet = Pet("Luna", 2, "dog")

    assert pet.list_tasks() == []


def test_sort_by_time_returns_chronological_order():
    """sort_by_time() should return tasks earliest-first by their start time."""
    evening = Task("Evening walk", "18:00", "daily", 30)
    morning = Task("Morning walk", "07:30", "daily", 20)
    noon = Task("Lunch feeding", "12:00", "daily", 10)

    ordered = Scheduler.sort_by_time([evening, morning, noon])

    assert [t.time for t in ordered] == ["07:30", "12:00", "18:00"]


def test_marking_daily_task_complete_schedules_next_day():
    """Completing a daily task adds a fresh copy due the following day."""
    pet = Pet("Mochi", 3, "cat")
    task = Task("Morning walk", "08:00", "daily", 20)
    pet.add_task(task)

    upcoming = pet.mark_task_complete(task)

    # Original is done; a new incomplete task now sits alongside it.
    assert task.completed is True
    assert len(pet.tasks) == 2
    # The new task is dated for tomorrow (computed the same way the code does).
    tomorrow = (date.today() + timedelta(days=1)).isoformat()
    assert upcoming is not None
    assert upcoming.completed is False
    assert upcoming.due_date == tomorrow


def test_find_conflicts_flags_duplicate_times():
    """Two tasks at the same time on the same day produce one conflict warning."""
    # Both default to today's due_date, so they land on the same day.
    walk = Task("Walk", "08:00", "daily", 20)
    feed = Task("Feed", "08:00", "daily", 10)

    warnings = Scheduler.find_conflicts([walk, feed])

    assert len(warnings) == 1
