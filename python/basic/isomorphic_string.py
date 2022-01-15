from typing import Dict


def is_isomorphic(str1: str, str2: str) -> bool:
    mappings: Dict[str, str] = {}

    if len(str1) != len(str2):
        return False

    for i in range(len(str1)):
        if str1[i] in mappings and str2[i] != mappings[str1[i]]:
            return False
        elif str2[i] in mappings and str1[i] != mappings[str2[i]]:
            return False
        else:
            mappings[str1[i]] = str2[i]
            mappings[str2[i]] = str1[i]

    return True


if __name__ == '__main__':
    str1 = "wow"
    str2 = "aaa"
    res = is_isomorphic(str1, str2)
    print(res)
