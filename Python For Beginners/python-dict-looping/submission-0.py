from typing import Dict, List # this adds type hints for List and Dict

def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    l_n = []
    for t in age_dict:
        l_n.append(t)
    return l_n

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    l_a = []
    for t in age_dict:
        l_a.append(age_dict[t])
    return l_a

# do not modify below this line
dict_1 = {"John": 25, "Doe": 30, "Jane": 22}
dict_2 = {"NeetCode": 24, "NeetCode2": 25, "NeetCode3": 26}

print(get_dict_keys(dict_1))
print(get_dict_keys(dict_2))

print(get_dict_values(dict_1))
print(get_dict_values(dict_2))
