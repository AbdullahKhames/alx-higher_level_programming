#!/usr/bin/python3
read_file = __import__('0-read_file').read_file
wr = __import__('1-write_file').write_file
to_json_string = __import__("3-to_json_string").to_json_string
from_json_string = __import__('4-from_json_string').from_json_string
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
class_to_json = __import__('8-class_to_json').class_to_json
Student = __import__('11-student').Student

s = Student("mohamed", "ahmed", 17)
print(s)


# save_to_json_file(st, "st.json")
dic = load_from_json_file("st.json")
s.reload_from_json(dic)
print(s)