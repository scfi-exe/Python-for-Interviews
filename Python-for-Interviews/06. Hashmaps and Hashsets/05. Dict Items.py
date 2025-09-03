# if we wanted all the keys in a dictionary, we can loop over the dict and append all the keys to a list, but python offers a more compact way to achieve this
# the myDict.keys() method returns all of the keys in a dict in a list
# similarly, we can get all of the values using myDict.values()
# lastly, we can get key:value pairs by unpacking and using myDict.items() -> most commonly used when we want to loop over the keys AND vals in a dictionary

from typing import Dict, List, Tuple


# takes a dictionary of names and ages, and returns a list of tuples where each tuple contains a name and age
def get_dict_items(age_dict: Dict[str, int]) -> List[Tuple[str, int]]:
    output = []
    for name, age in age_dict.items():
        output.append((name, age))
    return output


# do not modify below this line
print(get_dict_items({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_items({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))
print(get_dict_items({"Bob": 30, "David": 40, "Charlie": 35, "Alice": 25, "Eve": 45}))
print(
    get_dict_items(
        {"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40, "Eve": 45, "Frank": 50}
    )
)
