"""
Suzuki is the master monk of his monastery so it is up to him to ensure the kitchen is operating at full capacity
to feed his students and the villagers that come for lunch on a daily basis. This week there was a problem with
his deliveries and all the vegetables became mixed up. There are two important aspects of cooking in his kitchen,
it must be done in harmony and nothing can be wasted. Since the monks are a record keeping people the first order
of business is to sort the mixed up vegetables and then count them to ensure there is enough to feed all the
students and villagers.

You will be given a string with the following vegetables:
"cabbage", "carrot", "celery", "cucumber", "mushroom", "onion", "pepper", "potato", "tofu", "turnip"

Return a list of objects (tuple in Python, array in JavaScript, table in COBOL) with the count of each vegetable
in descending order. If there are any non vegetables mixed in discard them. If the count of two vegetables is the
same sort in reverse alphabetical order (Z->A).

(119, "pepper"),
(114, "carrot"),
(113, "turnip"),
(102, "onion"),
(101, "tofu"),
(100, "cabbage"),
(93, "mushroom"),
(90, "cucumber"),
(88, "potato"),
(80, "celery")
"""


def count_vegetables(string):
    vegetable_dict = {}
    vegetable_list = []
    for vegetable in string.split():
        if vegetable in ["cabbage", "carrot", "celery", "cucumber", "mushroom", "onion", "pepper", "potato", "tofu", "turnip"]:
            vegetable_dict[vegetable] = vegetable_dict.get(vegetable, 0) + 1
    
    for vegetable, counter in vegetable_dict.items():
        vegetable_list.append((counter, vegetable))
    
    
    return sorted(vegetable_list)[::-1]

print(count_vegetables('potato tofu cucumber cabbage turnip pepper onion carrot celery mushroom potato tofu cucumber cabbage'))