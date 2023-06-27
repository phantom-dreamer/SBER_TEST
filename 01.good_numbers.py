import re

PATTERN = "\D\d{2,4}\\\\\d{2,5}\D"

def get_good_nums(base_string):
    compiled_pattern = re.compile(PATTERN)
    similar_lines_list = compiled_pattern.findall(base_string) #list with similar lines
    for idx in range(len(similar_lines_list)):
        similar_lines_list[idx] = re.sub(r'[^0-9\\\\]', '', similar_lines_list[idx]) #find valid line
        left_part, right_part = similar_lines_list[idx].split('\\')
        similar_lines_list[idx] = left_part.zfill(4) + '\\' + right_part.zfill(5) #transformation to good number
    return similar_lines_list


if __name__ == "__main__":
    base_string = input()
    print(*get_good_nums(base_string), sep='\n')