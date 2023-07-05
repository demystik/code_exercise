#!/usr/bin/python3
def word_index(List):
    """word_index that takes one argument,
    a list of strings and returns the index of the longest word in the
    list. If there is no longest word (if all the strings are of the same
            length), the function should return zero (0). For example, the list
    below should return 2.
    """
    copyList = List.copy()
    List.sort(reverse=True)
    for word in range(len(List)):
        if len(List[word]) != len(List[word]):
            return 0
    return  copyList.index(List[0])


words1 = ["Hate", "remorse", "vengeance"]
words2 = ["Love", "Hate"]
print(word_index(words2))
