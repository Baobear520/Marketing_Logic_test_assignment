import random
import math

class GroupAssignment:
    """ A class to represent group assingment """

    def __init__(self, num_people=20, group_size=10):
        self.num_people = num_people
        self.group_size = group_size
        self.group1 = []
        self.group2 = []

    def assign_groups(self):
        """Randomly assigns people into two groups."""
        
        people = list(range(1, self.num_people + 1))
        random.shuffle(people)
        self.group1 = people[:self.group_size]
        self.group2 = people[self.group_size:]

    def check_same_group(self, person1, person2):
        """Checks if person1 and person2 are in the same group."""
        
        return (person1 in self.group1 and person2 in self.group1) or (person1 in self.group2 and person2 in self.group2)


class ProbabilityChecker:
    """ A class to represent results of probability checks """

    def __init__(self, group_assignment, trials=10000):
        self.group_assignment = group_assignment
        self.trials = trials

    def run_simulation(self, person1=19, person2=20):
        """Runs simulation to estimate the probability."""
        
        success_count = 0
        for _ in range(self.trials):
            self.group_assignment.assign_groups()
            if self.group_assignment.check_same_group(person1, person2):
                success_count += 1
        probability = success_count / self.trials
        return probability


    def calculate_theoretical_probability(self):
        """Calculates theoretical probability using combinatorics."""
        
        total_combinations = math.comb(self.group_assignment.num_people, self.group_assignment.group_size)
        favorable_combinations = math.comb(self.group_assignment.num_people - 2, self.group_assignment.group_size - 2)
        probability = 2 * favorable_combinations / total_combinations
        return probability


    def compare_probabilities(self, person1=19, person2=20):
        """Compares simulation and theoretical probabilities."""
        
        simulation_prob = self.run_simulation(person1, person2)
        theoretical_prob = self.calculate_theoretical_probability()
        return simulation_prob, theoretical_prob



if __name__ == "__main__":
    # Create an instance of GroupAssignment
    group_assignment = GroupAssignment()

    # Create an instance of ProbabilityChecker and run the checks
    checker = ProbabilityChecker(group_assignment, trials=10000)

    # Compare probabilities
    simulated_probability, theoretical_probability = checker.compare_probabilities()
    print(f"Simulated probability: {simulated_probability:.4f}")
    print(f"Theoretical probability: {theoretical_probability:.4f}")
