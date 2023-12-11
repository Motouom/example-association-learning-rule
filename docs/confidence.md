# Support

In association rules mining, the confidence help to measure the 
likelihood of occurrence of an itemset given another itemset.

## More Information

- https://en.wikipedia.org/wiki/Association_rule_learning#Confidence

## Pseudocode

```text
Algorithm: Calculate_Confidence
Input: Dataset (D), Rule (A -> B)
Output: Confidence value for Rule

1. Support_AB = Calculate_Support(D, A ∪ B)
2. Support_A = Calculate_Support(D, A)
3. If Support_A is not 0:
    a. Confidence = Support_AB / Support_A
   Else:
    a. Confidence = 0
4. Return Confidence
```

The function initializes the counters matched_antecedent_items and matched_rule_items to keep track of the number of itemsets that match the antecedent and the rule, respectively.

It then iterates over each itemset in the dataset. If the itemset matches the antecedent, the matched_antecedent_items counter is incremented. If the itemset also matches the rule, the matched_rule_items counter is also incremented.

The function then checks if the number of matched antecedent items is zero. If it is, the function returns zero to avoid division by zero.

Finally, the function calculates the confidence value as the ratio of the number of matched rule items to the number of matched antecedent items. This confidence value is returned by the function.

This alternative approach to calculating the confidence of a rule in a dataset has the same efficiency as the previous one, with a time complexity of O(n), where n is the number of itemsets in the dataset. However, the counting of matched itemsets is performed in a single pass through the dataset, which can be slightly more efficient in some cases.

The confidence value calculated by this alternative code can be used in the same way as in the previous code. For example, it can be used to filter the rules that meet a certain minimum threshold, which can help in identifying the most likely relationships between items in the dataset.