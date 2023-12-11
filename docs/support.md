# Support

In association rules mining, the support of a rule is the proportion of 
transactions that contain the premise and the conclusion of the rule. 
The support of a rule is an indication of how frequently the rule occurs 
in the dataset.

## More Information

- https://en.wikipedia.org/wiki/Association_rule_learning#Support

## Pseudocode

```text
Algorithm: Calculate_Support
Input: Dataset (D), Itemset (I)
Output: Support value for Itemset

1. Initialize count = 0
2. For each transaction T in Dataset D:
    a. If Itemset I is a subset of Transaction T:
        i. Increment count by 1
3. Support = count / Total number of transactions in Dataset D
4. Return Support
```

--In this code [LINK TEXT](../src/support.py), the function support is used to find the frequency of a given item set in a given dataset.

--Firstly, it checks if the dataset is empty. If it is, it throws an error message.

--If the dataset is not empty, it initializes a variable item_occurrence to keep track of the number of occurrences of the item set in the dataset.

--Next, it iterates through each list (itemset) in the dataset.

--Inside the loop, it checks if the elements of the given item set are present in the current list (itemset).

--If both elements are present, it increments the item_occurrence variable by 1.

--After iterating through all the lists in the dataset, it calculates the support value by dividing the item_occurrence variable by the total number of lists in the dataset.

--Hence, it prints the support value for the given item set.

--This code provides an alternative approach to finding the support value of a given item set in a dataset using a different approach than the support function provided in the question.



