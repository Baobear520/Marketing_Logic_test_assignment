import random

class Group:
    def __init__(self,group_id) -> int:
        self.group_id = group_id

    members_list = []

class Person:
    def __init__(self,id) -> int:
        self.id = id

    def __repr__(self) -> str:
        return f"Member №{self.id}"
    
class Selection:
    def __init__(self,number_of_people,number_of_groups):
        self.number_of_people = number_of_people + 1
        self.number_of_groups = number_of_groups + 1

    def seed_participants(self):
        participants = []
        for n in range(1,self.number_of_people):
            obj = Person(n)
            participants.append(obj)
        return participants
    
    def seed_groups(self):
        groups = []
        for n in range(1,self.number_of_groups):
            obj = Group(n)
            groups.append(obj)
        return groups

    def setup(self):
        participants = self.seed_participants()
        groups = self.seed_groups()
        return participants, groups


    def select_member(self):
        setup = self.setup()
        member = random.choice(setup[0])
        group = random.choice(setup[1])
        group.members_list.append(member)
        print(f"A person {member} is added to Group {group.group_id}")
        print(f"Current list of members in the group - {group.members_list}")

if __name__ == "__main__":
    res = Selection(20,2)
    res.select_member()




