from typing import List

def compute_budget(total_budget: float, citizen_votes: List[List[float]]) -> List[float]:
    num_citizens = len(citizen_votes)
    num_items = len(citizen_votes[0])

    def linear_increasing_function(i, t):
        return total_budget * min(1,(i + 1) * t)

    def generalized_median(votes, fixed_votes):
        all_votes = sorted(votes + fixed_votes)
        n = len(all_votes)
        if n % 2 == 1:
            median_index = n // 2
        else:
            median_index = (n - 1) // 2
        return all_votes[median_index]

    def binary_search(low, high, epsilon=1e-6):
        while high - low > epsilon:
            mid = (low + high) / 2
            fixed_votes = [linear_increasing_function(i, mid) for i in range(num_citizens - 1)]
            item_budgets = [generalized_median([citizen_votes[i][j] for i in range(num_citizens)], fixed_votes)
                            for j in range(num_items)]
            if sum(item_budgets) < total_budget:
                low = mid
            else:
                high = mid
        return high

    t_star = binary_search(0, 1)
    fixed_votes = [linear_increasing_function(i, t_star) for i in range(num_citizens - 1)]
    budget_allocation = [round(generalized_median([citizen_votes[i][j] for i in range(num_citizens)], fixed_votes), 2)
                         for j in range(num_items)]

    return budget_allocation
total_budget =30
citizen_votes = [
    [0, 0, 30],
    [15, 15, 0],
    [15, 15, 0]
]
budget = compute_budget(total_budget, citizen_votes)
print("Budget allocation (example 1):", budget)

total_budget =100
citizen_votes = [
    [100, 0, 0],
    [0, 0, 100]
    ]
budget = compute_budget(total_budget, citizen_votes)
print("Budget allocation (example 2):", budget)
