import itertools


def get_max(gigits_list):
    concatination_list =[]
    for item in itertools.permutations(gigits_list):
        item = int("".join(item))
        concatination_list.append(item)
    return max(concatination_list)


if __name__ == "__main__":
    #count_of_numbers = int(input())
    #[input() for i in range(count_of_numbers)]
    gigits_list = ["11", "234", "005", "89"]
    print(get_max(gigits_list))

