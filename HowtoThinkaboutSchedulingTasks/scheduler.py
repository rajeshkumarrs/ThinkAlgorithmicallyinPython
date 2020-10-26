from itertools import permutations


number_of_hours_in_a_day = 8

max_allowed_free_time=1

tasks = {
    'email' : [4,4],
    'meeting': [1,1],
    'project1': [2,2],
    "project2" : [1,2],
    "documentation" : [2,3],
    "status_report": [1,2]

}

def get_task_timing(tasks):
    new_task={}
    for k,v in tasks.items():
        new_task[k]={'chunks':v[0],'total_time_of_task':v[1],'time_per_chunk':v[1]/v[0]}

    return new_task

def create_subset_task(tasks):
    subtasks=[]
    for i in  permutations(tasks,3):
        subtasks.append(i)
    return subtasks

def admissible_task_list(tasks,subtasks):
    admissible_subtasks=[]
    for subtask in subtasks:
        task_names=[]
        all_subtask_total_time=0
        free_time=0
        for indv_task in subtask:
            all_subtask_total_time += tasks[indv_task]['total_time_of_task']
            task_names.append(indv_task)
            free_time = number_of_hours_in_a_day - all_subtask_total_time
        if(all_subtask_total_time<=number_of_hours_in_a_day and free_time<=max_allowed_free_time):
            subtask_dict={'tasks':task_names,'total_time':all_subtask_total_time,'free_time':free_time}
            admissible_subtasks.append(subtask_dict)
    return admissible_subtasks

if __name__ == '__main__':
    new_tasks=get_task_timing(tasks)
    subtasks=create_subset_task(new_tasks)
    admissible_subtasks = admissible_task_list(new_tasks,subtasks)
    for subtask in admissible_subtasks:
        print(subtask)