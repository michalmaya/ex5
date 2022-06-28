import json
import os



def names_of_registered_students(input_json_path, course_name):
    with open (input_json_path, 'r') as f:
        tempDict = json.load(f)
    return [tempDict["student_name"] for tempDict["student_name"] in tempDict if course_name in tempDict["registered_courses"]]






def enrollment_numbers(input_json_path, output_file_path):
    with open(input_json_path, 'r') as f:
        tempDict = json.load(f)
    coursesList = [course for course in tempDict.value]
    coursesDict = {}
    for course in coursesList:
        if course not in coursesDict.keys():
            coursesDict[course]= names_of_registered_students(input_json_path, course).len



def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    pass



