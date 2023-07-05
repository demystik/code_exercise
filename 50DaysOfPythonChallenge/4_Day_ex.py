#!/usr/bin/python3
def word_index(List):
    copyList = List.copy()
    List.sort(reverse=True)
    for word in range(len(List)):
        if len(List[word]) != len(List[word]):
            return 0
    return  copyList.index(List[0])


words1 = ["Hate", "remorse", "vengeance"]
words2 = ["Love", "Hate"]
print(word_index(words2))
