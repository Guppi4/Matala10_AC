# Budget Allocation Algorithm

## Overview
This Python script implements a budget allocation algorithm based on generalized median voting combined with a linear increasing function. The algorithm takes the total budget and a list of citizen votes as input and returns the budget allocation for each item in a fair and truthful manner.

## Algorithm Description
The budget allocation algorithm combines the principles of generalized median voting and a linear increasing function to achieve a fair and efficient allocation of resources. The key components of the algorithm are as follows:

1. Generalized Median Voting: The algorithm uses the generalized median voting mechanism to find a fair allocation of resources among multiple parties with potentially conflicting preferences. It considers the preferences of all citizens and aims to maximize the overall satisfaction.

2. Linear Increasing Function: The algorithm introduces a linear increasing function that assigns "fixed votes" to each citizen based on their index and a parameter t. The fixed votes are added to the citizen votes to compute the generalized median for each item. The parameter t is determined through a binary search to ensure that the budget constraint is satisfied.

3. Pareto Efficiency: The algorithm guarantees Pareto efficiency, meaning that no citizen can be made better off without making another citizen worse off. It achieves this by considering the preferences of all citizens and finding an allocation that maximizes the overall satisfaction.

4. Truthfulness: The algorithm is truthful or strategy-proof, ensuring that no citizen has an incentive to misreport their true preferences. The linear increasing function and the generalized median mechanism make it difficult for any individual citizen to manipulate the outcome in their favor.

5. Budget Constraint Satisfaction: The algorithm employs a binary search to find the optimal value of the parameter t that satisfies the budget constraint. It ensures that the sum of the allocated budgets for each item is as close as possible to the total budget, preventing overspending or underspending.

## Usage
To use the budget allocation algorithm, follow these steps:

1. Make sure you have Python installed on your system.
2. Save the script to a file with a .py extension (e.g., budget_allocation.py).
3. Open a terminal or command prompt and navigate to the directory where the script is saved.
4. Run the script using the command: python budget_allocation.py.
5. The script will execute and display the budget allocation for the provided examples.

## Function
The main function in the script is compute_budget, which takes the following parameters:
- total_budget (float): The total budget available for allocation.
- citizen_votes (List[List[float]]): A list of lists representing the votes of each citizen for each item.

The function returns a list of floats representing the budget allocation for each item.

## Examples
The script includes two examples:

1. Example 1:
   - Total budget: 30
   - Citizen votes: [[0, 0, 30], [15, 15, 0], [15, 15, 0]]
   - Expected output: [12.0, 12.0, 6.0]

2. Example 2:
   - Total budget: 100
   - Citizen votes: [[100, 0, 0], [0, 0, 100]]
   - Expected output: [50.0, 0.0, 50.0]

## Algorithmic Complexity
The algorithmic complexity of the budget allocation algorithm is as follows:
- Time complexity: O(m * n log n * log t_max), where m is the number of items, n is the number of citizens, and t_max is the upper bound of the binary search range.
- Space complexity: O(m * n), as it requires storing the citizen votes and the allocated budgets for each item.

## Potential Applications
The budget allocation algorithm has potential applications in various domains, including government budgeting, resource allocation in organizations, and collaborative decision-making processes where multiple stakeholders with different preferences need to reach a fair and truthful allocation of resources.

## Note
The script assumes that the total budget is a positive float value and the citizen votes are provided as a list of lists of floats. Make sure to format the input data correctly before running the script.

## Conclusion
This budget allocation algorithm provides a fair, truthful, and Pareto efficient solution for allocating resources based on the preferences of multiple parties. By combining generalized median voting with a linear increasing function and employing a binary search to satisfy the budget constraint, the algorithm offers a robust and efficient approach to budget allocation problems.

