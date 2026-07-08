import streamlit as st

from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

# --- Owner (persisted in the session so it survives every re-run) ---
owner_name = st.text_input("Owner name", value="Jordan")

if "owner" not in st.session_state:
    st.session_state.owner = Owner(owner_name)

owner = st.session_state.owner
owner.name = owner_name  # keep the owner's name in sync with the input

st.subheader("Add a Pet")
with st.form("add_pet_form"):
    pet_name = st.text_input("Pet name", value="Mochi")
    pet_age = st.number_input("Age", min_value=0, max_value=40, value=3)
    pet_species = st.selectbox("Species", ["dog", "cat", "other"])
    if st.form_submit_button("Add pet"):
        owner.add_pet(Pet(pet_name, int(pet_age), pet_species))
        st.success(f"Added {pet_name}!")

if owner.pets:
    st.write("Current pets:")
    for pet in owner.pets:
        st.write(f"- **{pet.name}** ({pet.species}, age {pet.age}) — {len(pet.tasks)} task(s)")
else:
    st.info("No pets yet. Add one above.")

st.divider()

st.subheader("Add a Task")
if not owner.pets:
    st.info("Add a pet first, then you can give it tasks.")
else:
    with st.form("add_task_form"):
        # Choose which pet this task belongs to.
        pet_names = [pet.name for pet in owner.pets]
        chosen_pet_name = st.selectbox("For which pet?", pet_names)

        description = st.text_input("Task description", value="Morning walk")
        col1, col2, col3 = st.columns(3)
        with col1:
            task_time = st.text_input("Time (HH:MM)", value="08:00")
        with col2:
            frequency = st.selectbox("Frequency", ["daily", "weekly", "monthly"])
        with col3:
            duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)

        if st.form_submit_button("Add task"):
            # Find the chosen pet object, then let it add its own task.
            chosen_pet = next(pet for pet in owner.pets if pet.name == chosen_pet_name)
            chosen_pet.add_task(Task(description, task_time, frequency, int(duration)))
            st.success(f"Added '{description}' to {chosen_pet_name}!")

st.divider()

st.subheader("Build Schedule")
col_a, col_b = st.columns(2)
with col_a:
    start_time = st.text_input("Day starts at (HH:MM)", value="08:00")
with col_b:
    available_minutes = st.number_input(
        "Time available (minutes)", min_value=1, max_value=1440, value=120
    )

if st.button("Generate schedule"):
    scheduler = Scheduler()
    plan = scheduler.build_plan(owner.all_tasks(), int(available_minutes), start_time)

    st.markdown("### Today's Schedule")
    if not plan:
        st.warning("Nothing fits the plan. Add tasks, or increase the time available.")
    else:
        for task in plan:
            st.write(f"**{task.time}** — {task.description} ({task.duration_minutes} min)")
