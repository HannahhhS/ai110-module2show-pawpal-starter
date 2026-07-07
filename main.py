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
    rex.add_task(Task("Long walk", "08:30", "daily", 45))
    rex.add_task(Task("Give meds", "09:30", "daily", 5))

    owner.add_pet(mochi)
    owner.add_pet(rex)

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
