# to-do-list application

tasks = []  # list of task dictionaries (each dict has: id, task, Status)
next_id = 1  # auto-incrementing id for new tasks

while True:
    # Read a command and normalize it (strip spaces + lowercase).
    user_task = input("Type add/ list/ incomplete/ delete/ quit: ").strip().lower()

    if user_task == "quit":
        break

    elif user_task == "add":
        # Collect task info from the user and store it as a dictionary.
        task = {}
        done_in = False

        to_do = input(f"{next_id}. ")
        done = input("Done? (y/n): ").strip().lower()
        # Turn the user's text into a real boolean (True/False).
        done_in = done in ("y", "yes", "t", "true")

        task = {"id": next_id, "task": to_do, "Status": done_in}
        tasks.append(task)
        next_id += 1

    elif user_task == "list":
        # Show all tasks (done + not done).
        if not tasks:
            print("No tasks")
        else:
            print(f"{'ID':<4}    {'TASK':<30} STATUS")
            for task in tasks:
                # Print Status as text instead of 0/1.
                status_text = "True" if task["Status"] else "False"
                print(f"{task['id']:<4} {task['task']:<30} {status_text:>7}")
        
    elif user_task == "incomplete":
        # Show only tasks where Status is False (not done yet).
        if not tasks:
            print("No pending tasks")
        else:
            print(f"{'ID':<4}    PENDING {'TASK':<30}")
            for task in tasks:
                if task['Status'] == False:
                    print(f"{task['id']:<4} {task['task']:<30} ")

    elif user_task == "delete":
        # Delete all completed tasks (Status == True).
        if not tasks:
            print("No task updated")
        else:
            deleted_count = 0
            # IMPORTANT: delete from the end so list indexes don't shift and skip tasks.
            i = len(tasks) - 1
            while i >= 0:
                if tasks[i]["Status"] == True:
                    del tasks[i]
                    deleted_count += 1
                i -= 1

            print(f"Deleted {deleted_count} completed task(s)")


