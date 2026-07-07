"""Tests for PawPal+ core classes.

Run from the project root with:  pytest
"""

import sys
from pathlib import Path

# Let this test (inside tests/) import pawpal_system.py from the project root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pawpal_system import Pet, Task


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
