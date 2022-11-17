from pyodide.http import pyfetch, FetchResponse
from typing import Optional, Any

async def request(url: str, method: str = "GET", body: Optional[str] = None, headers: Optional[dict[str, str]] = None, **fetch_kwargs: Any) -> FetchResponse:
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
