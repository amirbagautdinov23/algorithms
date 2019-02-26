from collections import deque

graph = dict()
graph = {
    "kompot": ["krot", "ilon"],
    "krot": ["ilon", "kompot"],
    "ilon": ["krot", "kompot", "nick", "jack"],
    "jack": ["joe", "mask", "ilon"],
    "nick": ["ilon", "john"],
    "mask": ["jack", "joe"],
    "john": ["nick", "joe"],
    "joe": ["john", "jack", "mask"]
}


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []  # проверенные имена
    if name == "john":
        print(name + " is who we need")
        return True
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person == "amir":
                print(person + " is who we need")
                return True
            else:
                print(person + " is not amir")
                # print(f"searching in {person}'s friends")
                search_queue += graph[person]
                searched.append(person)
    print("we do not find him")
    return False


# search("krot")
search("john")
