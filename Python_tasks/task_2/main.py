import random

class Group:
    def __init__(self, group_id):
        self.group_id = group_id
        self.members_list = []
    
    def add_member(self, member):
        self.members_list.append(member)
        
    def print_members(self):
        print(f"Group {self.group_id} members: {self.members_list}")

class Person:
    def __init__(self, id):
        self.id = id

    def __repr__(self) -> str:
        return f"Member №{self.id}"

class Selection:
    def __init__(self, number_of_people, number_of_groups):
        self._number_of_people = number_of_people
        self._number_of_groups = number_of_groups

    def create_objects(self, number, cls):
        return [cls(n) for n in range(1, number + 1)]
    
    def setup(self):
        participants = self.create_objects(self._number_of_people, Person)
        groups = self.create_objects(self._number_of_groups, Group)
        return participants, groups

    def seed_participants(self):
        participants, groups = self.setup()
        group_size = len(participants) // len(groups)  
        
        for group in groups:
            while len(group.members_list) < group_size and participants:
                member = participants.pop(random.randint(0, len(participants) - 1))
                group.add_member(member)

        return groups

def is_in_the_same_group(member_id1, member_id2, groups):
    for group in groups:
        member_ids = [member.id for member in group.members_list]
        if member_id1 in member_ids and member_id2 in member_ids:
            return True
    return False

def run_simulation(trials, number_of_participants, number_of_groups):
    success_count = 0

    for _ in range(trials):
        selection = Selection(number_of_participants, number_of_groups)
        groups = selection.seed_participants()

        # Use the IDs 19 and 20 directly
        if is_in_the_same_group(19, 20, groups):
            success_count += 1

    probability = success_count / trials
    return probability

if __name__ == "__main__":
    number_of_participants = 20
    number_of_groups = 2
    trials = 10000  # Number of simulation trials
    probability = run_simulation(trials,number_of_participants,number_of_groups)
    print(f"Probability that 19 and 20 are in the same group: {probability}")


    
            
                
        





