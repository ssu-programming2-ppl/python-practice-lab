from question.models import Testcase
import os, shutil, platform
from core import utils
import uuid
import subprocess 



def scoring_question(question_seq, question_code):
    """
    문제 채점 함수(모든 테스트케이스로 채점을 진행)
        Args:
            question_seq (int): 문제 번호(시퀀스)
            question_code (str): 문제 풀이 소스코드
        Retruns:
            채점 점수
    """

    testcase_list = Testcase.objects.filter(question_seq=question_seq)

    _, percent = scoring_code(question_code, testcase_list)

    return percent


def excute_question(question_seq, question_code):

    """
    문제 실행 함수(공개된 테스트케이스로만 채점을 진행)
        Args:
            question_seq (int): 문제 번호(시퀀스)
            question_code (str): 문제 풀이 소스코드
        Retruns:
            채점 점수
    """

    testcase_list = Testcase.objects.filter(
        question_seq=question_seq, testcase_open_yn="Y"
    )

    result, _ = scoring_code(question_code, testcase_list)

    return result


def scoring_code(question_code, testcase_list):

    """
    코드 채점 함수
        Args:
            question_code (str): 문제 풀이 소스코드
            testcase_list (Testcase): 테스트케이스 모델 리스트
        Retruns:
            채점 점수
    """

    result = []

    id = str(uuid.uuid4())
    utils.create_folder(id)

    # 풀이 코드 파일 생성
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

        # 채점 진행
        if platform.system() == "Windows":
            input_file_name = input_file_name.replace("/", "\\")
            code_file_name = code_file_name.replace("/", "\\")
            output_file_name = output_file_name.replace("/", "\\")

            os.system(
                f"type {input_file_name} | python {code_file_name} >> {output_file_name}"
            )
        else:
            os.system(
                f"cat {input_file_name} | python3 {code_file_name} >> {output_file_name}"
            )

        file = open(output_file_name, "r")
        output = file.read().strip()
        file.close()

        # 결과 생성
        json = {
            "input": testcase.testcase_input,
            "output": output,
            "answer": testcase.testcase_output,
            "flag": False,
        }

        if output == testcase.testcase_output:
            correct_count += 1
            json["flag"] = True

        result.append(json)

    shutil.rmtree(id)

    return result, int((correct_count / total_count) * 100)


def syntax_check(question_code):

    id = str(uuid.uuid4())
    utils.create_folder(id)

    # 풀이 코드 파일 생성
    code_file_name = f"{id}/source.py"
    file = open(code_file_name, "w")
    file.write(question_code)
    file.close()

    if platform.system() == "Windows":
        code, output = subprocess.getstatusoutput(f"python -m py_compile {id}\source.py")
    else:
        code, output = subprocess.getstatusoutput(f"python -m py_compile {id}/source.py")

    shutil.rmtree(id)

    if code == 0:
        return True, output
    else:
        return False, output
    
def excute_question(question_seq, question_code):

    """
    문제 제출 함수(공개된 테스트케이스로만 채점을 진행)
        Args:
            question_seq (int): 문제 번호(시퀀스)
            question_code (str): 문제 풀이 소스코드
        Retruns:
            채점 점수
    """

    testcase_list = Testcase.objects.filter(
        question_seq=question_seq, testcase_open_yn="Y"
    )

    result, _ = scoring_code(question_code, testcase_list)

    return result
