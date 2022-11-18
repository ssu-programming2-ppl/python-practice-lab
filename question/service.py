from question.models import Testcase
import os, shutil, platform
from core import utils
import uuid

# Create your views here.
def scoring_question(question_seq, question_code):

    testcase_list = Testcase.objects.filter(question_seq=question_seq)

    _, percent = test(question_code, testcase_list)

    return percent

def excute_question(question_seq, question_code):

    testcase_list = Testcase.objects.filter(question_seq=question_seq, testcase_open_yn='Y')

    result, _ = test(question_code, testcase_list)

    return result

def test(question_code, testcase_list):

    result = []

    id = str(uuid.uuid4())
    utils.create_folder(id)

    code_file_name = f"{id}/source.py"
    file = open(code_file_name, "w")
    file.write(question_code)
    file.close()

    total_count = len(testcase_list)
    correct_count = 0

    for testcase in testcase_list:
        input_file_name = f"{id}/in_{testcase.testcase_seq}.txt"

        output_file_name = f"{id}/out_{testcase.testcase_seq}.txt"

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

        # 결과 생성
        json = {
            "input": testcase.testcase_input,
            "output" : output,
            "answer" : testcase.testcase_output,
            "flag": False
        }

        if output == testcase.testcase_output:
            correct_count += 1
            json["flag"] = True
        
        result.append(json)
        
    shutil.rmtree(id)

    return result, (correct_count / total_count) * 100
