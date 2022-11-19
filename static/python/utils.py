from pyodide.http import pyfetch, FetchResponse
from typing import Optional, Any

async def request(url: str, method: str = "GET", body: Optional[str] = None, headers: Optional[dict[str, str]] = None, **fetch_kwargs: Any) -> FetchResponse:
    """
    request 요청 함수
        Args:
            url (str): 요청 주소
            method (str): 요청 함수
            body (Optional[str]): 요청 바디
            header (Optional[dict[str, str]]): 요청 헤더
        Retruns:
            리턴 값
    """

    default_headers = {"Content-type": "application/json"}
    kwargs = {"method": method, "mode": "cors"} 

    if body and method not in ["GET", "HEAD"]:
        kwargs["body"] = body
    if headers:
        kwargs["headers"] = headers
    else:
        kwargs["headers"] = default_headers

    kwargs.update(fetch_kwargs)

    response = await pyfetch(url, **kwargs)
    return response

def parse_code(code_area):
    """
    py-repl 태그의 코드 파싱 함수
        Args:
            code_area (Element): 코드 구역
        Retruns:
            파싱한 코드
    """
    code = ""

    for c in code_area.select(".cm-content").element.children:
        code += c.textContent + "\n"
    
    return code
    
