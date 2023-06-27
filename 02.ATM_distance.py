def get_distances(list_of_distances, k):
    if k == 0: # больше не осталось банкоматов
        return list_of_distances
    if sum(list_of_distances) == 0: # уменьшили растояние максимальным способом (они все стоят друг с другом)
        return list_of_distances
    

    max_value, max_idx = list_of_distances[0], 0
    for curr_idx in range(len(list_of_distances)):
        if list_of_distances[curr_idx] > max_value:
            max_value = list_of_distances[curr_idx]
            max_idx = curr_idx

    list_of_distances = list_of_distances[:max_idx] + [list_of_distances[max_idx] // 2, list_of_distances[max_idx] // 2] + list_of_distances[max_idx + 1:]
    print(f"iter: {list_of_distances}")
    return get_distances(list_of_distances, k - 1)



if __name__ == "__main__":
    #ll = [100, 180, 50, 60, 150]
    #ll = [10, 10, 100000, 10, 10]
    ll = [4, 1, 1, 1, 1]
    print(f"base list: {ll}")
    
    #print(get_distances(ll, 3))
    #print(get_distances(ll, 5))
    print(get_distances(ll, 10000000000))