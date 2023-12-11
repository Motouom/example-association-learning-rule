from test.test_support import *

itemset_type = list[object]
dataset_type = list[list[object]]


def support(itemsets: dataset_type, data_set: itemset_type) -> float:
    """
    To find the frequency of item sets in the dataset.
    """
    return support_value


dataset = [
    ['bread', 'milk'],
    ['bread', 'diaper', 'beer', 'eggs'],
    ['milk', 'diaper', 'beer', 'cola'],
    ['bread', 'milk', 'diaper', 'beer'],
    ['bread', 'milk', 'diaper', 'cola']
]
itemset = ['bread', 'milk']

"""
checking if the dataset is empty or not to defore continue
"""
if len(dataset) != 0:

    item_occurrence = 0
    for items in range(len(dataset)):
        """
    comparing the elements in the itemset to those in the dataset to see the list that satisfies the itemsets
    """

        if itemset[0] in dataset[items] and itemset[1] in dataset[items]:
            item_occurrence = item_occurrence + 1
    """
    throwing an error message if the dataset is empty
    """
else:
    print(f"error:{dataset} is empty")

support = item_occurrence / len(dataset)


print(f"support value for: {itemset} is {support}")
