# to-do-list application

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

fh = logging.FileHandler('todo.log')
fh.setFormatter(f)

logger.addHandler(fh)


tasks = []  # list of task dictionaries (each dict has: id, task, Status)
next_id = 1  # auto-incrementing id for new tasks
logger.info("To-do logging application started")
logger.debug("Initial state set: tasks=%s, next_id=%s", tasks, next_id)

while True:
    # Read a command and normalize it (strip spaces + lowercase).
    user_task = input("Type add/ list/ incomplete/ delete/ quit: ").strip().lower()
    logger.debug("User command received: %s", user_task)

    if user_task == "quit":
        logger.info("Quit command received. Exiting application.")
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
        logger.info(
            "Task added: id=%s, task=%s, status=%s",
            task["id"],
            task["task"],
            task["Status"],
        )
        next_id += 1
        logger.debug("Next task id incremented to %s", next_id)

    elif user_task == "list":
        # Show all tasks (done + not done).
        if not tasks:
            print("No tasks")
            logger.info("List command: no tasks to display")
        else:
            logger.info("List command: displaying %s task(s)", len(tasks))
            print(f"{'ID':<4}    {'TASK':<30} STATUS")
            for task in tasks:
                # Print Status as text instead of 0/1.
                status_text = "True" if task["Status"] else "False"
                print(f"{task['id']:<4} {task['task']:<30} {status_text:>7}")
                logger.debug(
                    "Listed task: id=%s, task=%s, status=%s",
                    task["id"],
                    task["task"],
                    task["Status"],
                )
        
    elif user_task == "incomplete":
        # Show only tasks where Status is False (not done yet).
        if not tasks:
            print("No pending tasks")
            logger.info("Incomplete command: no tasks available")
        else:
            logger.info("Incomplete command: checking pending tasks in %s task(s)", len(tasks))
            print(f"{'ID':<4}    PENDING {'TASK':<30}")
            for task in tasks:
                if task['Status'] == False:
                    print(f"{task['id']:<4} {task['task']:<30} ")
                    logger.debug(
                        "Pending task shown: id=%s, task=%s",
                        task["id"],
                        task["task"],
                    )

    elif user_task == "delete":
        # Delete all completed tasks (Status == True).
        if not tasks:
            print("No task updated")
            logger.info("Delete command: no tasks to update")
        else:
            deleted_count = 0
            # IMPORTANT: delete from the end so list indexes don't shift and skip tasks.
            i = len(tasks) - 1
            while i >= 0:
                if tasks[i]["Status"] == True:
                    logger.debug(
                        "Deleting completed task: id=%s, task=%s",
                        tasks[i]["id"],
                        tasks[i]["task"],
                    )
                    del tasks[i]
                    deleted_count += 1
                i -= 1

            print(f"Deleted {deleted_count} completed task(s)")
            logger.info("Delete command completed: deleted_count=%s", deleted_count)
    else:
        logger.warning("Invalid command entered: %s", user_task)


