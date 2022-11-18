# PPL(python-practice-lab) :: 온라인 코딩테스트 서비스

## WHAT? 
Python, Java, C언어 기반의 예제 문제 풀이 및 제작 가능한 코딩 테스트 서비스

## WHO? 
1) 파이썬 언어를 교육 과목으로 배우는 청소년
2) 파이썬으로 기업 코딩테스트를 준비하는 개발자


[`service link`](http://http://ssuppl.tk/)

# Skill-set

* Python (Django)
* Pyscript
* Postgresql

## index /
- /question
    - [`POST /execute`](#POST-questionexecute)
    - [`POST /scoring`](#POST-questionscoring)
- /board
    - [`GET /block`](#GET-apicoreblock)
    - /channel
        - [`POST /create`](#POST-apicorechannelupdateanchor)




## `POST /question/execute`
코드 실행  API
### request

```json
request body

{
    "question_seq": "1",
    "question_code": "print('test')"
}
```

### response

- on success

```json
{
    "code": "0000",
    "data": [
        {
            "input" : "zz1", // 입력값
            "ouput" : "zz1", // 출력값
            "answer" : "zz1", //정답
            "flag" : true // 성공 여부
        },
        {
            "input" : "zz2",
            "ouput" : "zz2",
            "answer" : "zz2", 
            "flag" : true
        },
        {
            "input" : "zz2",
            "ouput" : "zz3",
            "answer" : "zz1", 
            "flag" : false
        }
    ],
    "message": "코드 실행 성공",
    "flag": true
}
```
- on failure

```json
{
    "code": "9999",
    "data": null,
    "message": "error message",
    "flag": false
}
```

## `POST /question/scoring`
문제 채점  API
### request

```json
request body

{
    "question_seq" : "1",
    "question_code" : "print('test')",
    "question_start_time" :"2022-11-18 9:38:06.533823"

}
```

### response

- on success

```json
{
    "code": "0000",
    "data": 100, // 점수
    "message": "채점 성공",
    "flag": true
}
```
- on failure

```json
{
    "code": "9999",
    "data": null,
    "message": "error message",
    "flag": false
}
```



## `POST /question/create`
문제 생성  API
### request

```json
request body

{
    "question_title": "title",
    "question_level": "상",
    "question_lang": "Python",
    "question_text": "문제 설명",
    "question_code": "정답코드",
    "testcase_list" : [
        {
            "testcase_input": "input1",
            "testcase_output": "output1",
            "testcase_open_yn": "Y"
        },
        {
            "testcase_input": "input2",
            "testcase_output": "output2",
            "testcase_open_yn": "Y"
        }
    ]
}
```

### response

- on success

```json
{
    "code": "0000",
    "data": null,
    "message": "succes",
    "flag": true
}
```
- on failure

```json
{
    "code": "9999",
    "data": null,
    "message": "error message",
    "flag": false
}
```

## `POST /board/create`
게시판 생성  API
### request

```json
request body

{
    "board_title": "제목",
    "board_link": "링크",
    "board_division": "구분"
}
```

### response

- on success

```json
{
    "code": "0000",
    "data": null,
    "message": "succes",
    "flag": true
}
```
- on failure

```json
{
    "code": "9999",
    "data": null,
    "message": "error message",
    "flag": false
}
```
