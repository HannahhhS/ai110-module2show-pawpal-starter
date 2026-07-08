"""Quick manual test driver for PawPal+.

Builds an owner with a couple of pets and some tasks, then prints the
day's schedule to the terminal. Run with:  python main.py
"""

from pawpal_system import Owner, Pet, Task, Scheduler


def main() -> None:
    # 1. Create an owner.
    owner = Owner("Jordan")
    owner.set_preference("day_start", "08:00")

    # 2. Create two pets.
    mochi = Pet("Mochi", 3, "cat")
    rex = Pet("Rex", 5, "dog")

    # 3. Add tasks with different times to the pets.
    mochi.add_task(Task("Morning feeding", "08:00", "daily", 10))
    mochi.add_task(Task("Litter box scoop", "08:15", "daily", 5))
    mochi.add_task(Task("Playtime", "08:30", "daily", 15))  # same time as Rex's walk!
    rex.add_task(Task("Long walk", "08:30", "daily", 45))
    rex.add_task(Task("Give meds", "09:30", "daily", 5))

    owner.add_pet(mochi)
    owner.add_pet(rex)

    # Quick check: detect tasks booked at the same time (across pets too).
    print("=== Conflict check ===")
    conflicts = Scheduler.find_conflicts(owner.all_tasks())
    if conflicts:
        for warning in conflicts:
            print(f"  WARNING: {warning}")
    else:
        print("  No conflicts. You're all set!")

    # Quick check: filter tasks by pet name.
    print("=== Rex's tasks only ===")
    for task in owner.tasks_for_pet("Rex"):
        print(f"  {task.time}  {task.description}")

    print("=== Mochi's tasks only ===")
    for task in owner.tasks_for_pet("Mochi"):
        print(f"  {task.time}  {task.description}")

    # Quick check: completing a daily task auto-schedules the next one.
    walk = rex.tasks[0]  # Rex's "Long walk" (daily)
    print("=== Complete Rex's daily walk ===")
    upcoming = rex.mark_task_complete(walk)
    print(f"  Marked '{walk.description}' done: {walk.completed}")
    print(f"  Auto-created next '{upcoming.description}' due {upcoming.due_date}")

    print("=== Rex's tasks after completion ===")
    for task in rex.tasks:
        status = "done" if task.completed else "todo"
        print(f"  [{status}] {task.time}  {task.description}  (due {task.due_date or 'n/a'})")

    # 4. Build and print today's schedule.
    scheduler = Scheduler()
    plan = scheduler.build_plan(
        owner.all_tasks(),
        available_minutes=90,
        start_time="08:00",
    )

    print("=== Today's Schedule ===")
    if not plan:
        print("  Nothing scheduled.")
    for task in plan:
        print(f"  {task.time}  {task.description} ({task.duration_minutes} min)")


if __name__ == "__main__":
    main()
