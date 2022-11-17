from question.models import Testcase
import os, shutil, platform
from core import utils

# Create your views here.
def scoring_question(session_id, question_seq, question_code):

    testcase_list = Testcase.objects.filter(question_seq=question_seq)

    utils.create_folder(session_id)

    code_file_name = session_id + "/" + question_seq + ".py"
    file = open(code_file_name, "w")
    file.write(question_code)
    file.close()

    total_count = len(testcase_list)
    correct_count = 0

    for testcase in testcase_list:
        input_file_name = session_id + "/" + "in_" + str(testcase.testcase_seq) + ".txt"

        output_file_name = (
            session_id + "/" + "out_" + str(testcase.testcase_seq) + ".txt"
        )

        file = open(input_file_name, "w")
        file.write(testcase.testcase_input)
        file.close()

        if platform.system() == "Windows":
            input_file_name = input_file_name.replace('/','\\')
            code_file_name = code_file_name.replace('/','\\')
            output_file_name = output_file_name.replace('/','\\')


            os.system(f"type {input_file_name} | python {code_file_name} >> {output_file_name}")
        else:
            os.system(f"cat {input_file_name} | python3 {code_file_name} >> {output_file_name}")

        file = open(output_file_name, "r")
        output = file.read().strip()
        file.close()

        if output == testcase.testcase_output:
            correct_count += 1

    shutil.rmtree(session_id)

    return (correct_count / total_count) * 100
