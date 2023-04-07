import random


class Crossover:

    # 순서교차가 이루어지는 메소드
    def order(sol_list1, sol_list2):
        start_idx = random.randint(0, len(sol_list1) - 1)
        end_idx = random.randint(start_idx + 1, len(sol_list1))
        new_list = sol_list1[start_idx:end_idx]
        result_list = []
        tmp_set = set()
        for i in range(len(new_list)):
            tmp_set.add(new_list[i])
        for i in range(len(sol_list2) - end_idx):
            if sol_list2[end_idx + i] not in tmp_set:
                result_list.append(sol_list2[end_idx + i])
        for i in range(end_idx):
            if sol_list2[i] not in tmp_set:
                result_list.append(sol_list2[i])
        front = result_list[0:start_idx]
        back = result_list[start_idx:]
        result_list = front + new_list + back
        return result_list
