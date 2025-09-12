from typing import List
from sortedcontainers import SortedDict


def remove_keys(
    sorted_dict: SortedDict[str, int], keys: List[str]
) -> SortedDict[str, int]:
    output = sorted_dict
    for key in keys:
        if key in output:
            output.pop(key)
    return output


def get_values_before_target(
    sorted_dict: SortedDict[str, int], target: str
) -> List[int]:
    output = []
    for key in sorted_dict:
        if key == target:
            break
        else:
            output.append(sorted_dict[key])
    return output


# do not modify below this line
print(remove_keys(SortedDict({"Alice": 25, "Bob": 30, "Charlie": 35}), ["Bob"]))
print(
    remove_keys(
        SortedDict({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}),
        ["Bob", "David"],
    )
)
print(
    remove_keys(
        SortedDict({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40, "Eve": 45}),
        ["Alice", "Eve"],
    )
)

print(
    get_values_before_target(SortedDict({"Alice": 25, "Bob": 30, "Charlie": 35}), "Bob")
)
print(
    get_values_before_target(
        SortedDict({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}), "David"
    )
)
print(
    get_values_before_target(
        SortedDict({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}), "Charlie"
    )
)
print(
    get_values_before_target(
        SortedDict({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}), "Bob"
    )
)
print(
    get_values_before_target(
        SortedDict({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}), "Alice"
    )
)
