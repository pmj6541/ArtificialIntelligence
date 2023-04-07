import random

class Mutation:

    # 변이를 실행할지 안 할지를 판별하는 메소드
    def do_or_not():
        if random.random() <= 0.1:
            return True
        else:
            return False

    # 임의의 두 인덱스의 값을 서로 교환하는 변이를 일으키는 메소드
    def exchange(sol_list):
        if(Mutation.do_or_not()):
            idx1 = random.randint(0, len(sol_list) - 1)
            idx2 = random.randint(0, len(sol_list) - 1)
            while(idx1 == idx2):
                idx2 = random.randint(0, len(sol_list) - 1)
            tmp = sol_list[idx1]
            sol_list[idx1] = sol_list[idx2]
            sol_list[idx2] = tmp
            return sol_list
        else:
            return sol_list
    
    # k개의 연속된 유전자를 취하여 값을 뒤집어 변이를 일으키는 메소드
    def reverse(sol_list):
        if(Mutation.do_or_not()):
            start_idx = random.randint(0, len(sol_list) - 2)
            end_idx = random.randint(start_idx + 2, len(sol_list))
            new_list = sol_list[start_idx:end_idx]
            new_list.reverse()
            front = sol_list[0:start_idx]
            back = sol_list[end_idx:]
            sol_list = front + new_list + back
            return sol_list
        else:
            return sol_list