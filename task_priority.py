def get_priority(task):
    return task['priority']

sample_tasks = [
    {'task': 'Task 1', 'priority': 3},
    {'task': 'Task 2', 'priority': 1},
    {'task': 'Task 3', 'priority': 2}
]

sorted_tasks = sorted(sample_tasks, key=get_priority)

print("Sorted tasks by priority:")
for task in sorted_tasks:
    print(task)
