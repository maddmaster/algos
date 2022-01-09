from typing import List, Dict


def group_anagrams(words: List[str]) -> List[List[str]]:
    groups: Dict[str, List[str]] = {}
    for word in words:
        id = "".join(sorted(word))
        if id in groups:
            groups[id].append(word)
        else:
            groups[id] = [word]
    return list(groups.values())


if __name__ == '__main__':
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(words)
    print(result)


'''
if we sort all the letters of each word, then any word that results 
in the same sorted letters belongs to the same anagram group
'''