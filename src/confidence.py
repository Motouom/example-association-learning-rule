from typing import List, Tuple
from support import support

dataset_type = List[List[object]]
rule_type = Tuple[List[object], List[object]]


def confidence(dataset: dataset_type, rule: rule_type) -> float:
    """
    measuring  occurrence of an item set given that we have another item set that exists.
    """

    antecedent, consequent = rule
    total_items = len(dataset)
    matched_antecedent_items = 0
    matched_rule_items = 0

    for itemset in dataset:
        if all(item in itemset for item in antecedent):
            matched_antecedent_items += 1
            if all(item in itemset for item in consequent):
                matched_rule_items += 1

    if matched_antecedent_items == 0:
        return 0  # to Avoid any division division by zero

    confidence_value = matched_rule_items / matched_antecedent_items
    return confidence_value