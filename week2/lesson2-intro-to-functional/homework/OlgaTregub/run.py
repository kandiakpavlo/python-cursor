from utils.task_1 import members
from utils.task_2 import transform_uppercase_names
from utils.task_3 import add_age_load
from utils.task_4 import select_with_o
from utils.task_5 import sum_youngest_oldest
from utils.task_6 import sort_by_name_length


if __name__ == "__main__":
    import copy

    print(members, "\n")

    # Task 2
    uppercase_members=copy.deepcopy(members)
    print (transform_uppercase_names(uppercase_members), "\n")

    # Task 3
    load_age_members = copy.deepcopy(members)
    print(add_age_load(load_age_members), "\n")

    # Task 4
    with_o_members = copy.deepcopy(members)
    print(select_with_o(with_o_members), "\n")

    # Task 5
    age_members = copy.deepcopy(members)
    print(sum_youngest_oldest(age_members), "\n")

    # Task 6
    length_name_members = copy.deepcopy(members)
    print(sort_by_name_length(length_name_members), "\n")








