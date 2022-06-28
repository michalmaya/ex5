import json
import os
from collections import defaultdict


def names_of_registered_students(input_json_path, course_name):
    with open(input_json_path, 'r') as f:
        tempDict = json.load(f)
    return [student.get("student_name") for student in tempDict.values() if
            course_name in student.get("registered_courses")]


def enrollment_numbers(input_json_path, output_file_path):
    with open(input_json_path, 'r') as fileIn:
        tempDict = json.load(fileIn)
    coursesList = [course.get("registered_courses") for course in tempDict.values()]
    coursesList.sort()
    coursesDict = {}
    for courses in coursesList:
        for course in courses:
            if not course in coursesDict:
                coursesDict[course]= len(names_of_registered_students(input_json_path, course))
    with open(output_file_path, 'w') as fileOut:
        json.dump(coursesDict, fileOut, indent=4)



def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    fileList = os.listdir(json_directory_path)
    finalDict = defaultdict(list)
    for i in fileList:
        if i.endswith(".json"):
            with open(json_directory_path + "/" + i, 'r') as f:
                temp_dict = json.load(f)
                for item in temp_dict:
                    for lecturer in temp_dict[item]["lecturers"]:
                        course = temp_dict[item]["course_name"]
                        if course not in finalDict[lecturer]:
                            finalDict[lecturer] += [course]

    with open(output_json_path, 'w') as f:
        f.write('{\n')
        for key, value in finalDict.items():
            if not key == list(finalDict.keys())[-1]:
                jsonStr = ("    " + json.dumps(key) + ": " + json.dumps(value)+",\n")
            else:
                jsonStr = ("    " + json.dumps(key) + ": " + json.dumps(value)+"\n")
            f.write(jsonStr)
        f.write('}')
