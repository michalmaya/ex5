import json
import os
from collections import defaultdict


def names_of_registered_students(input_json_path, course_name):
    with open(input_json_path, 'r') as f:
        tempDict = json.load(f)
    return [tempDict["student_name"] for tempDict["student_name"] in tempDict if
            course_name in tempDict["registered_courses"]]


def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    pass


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
        json.dump(finalDict, f, indent=4)
