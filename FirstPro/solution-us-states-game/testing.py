student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for(key, value) in student_dict.items():
#     print(value)
#     print(key)

import pandas

student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)

# loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)
#     print(key)

# loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    if row.student == "Angela":
        print(row.score)
