from http.client import responses
from typing import Optional, List

from fastapi.responses import Response, HTMLResponse, PlainTextResponse
from fastapi import Header, Cookie, Form
from fastapi import APIRouter
from custom_log import log

router = APIRouter(
    prefix="/product",
    tags=["product"]
)

products = ["watch", "phone", "laptop"]


"""
The Form(...) in the function parameter is used to indicate 
that the name parameter should be taken from form data in a POST request. 
The ellipsis (...) is used to indicate that this parameter is required.
"""
@router.post("/new")
def create_product(name: str = Form(...)):
    products.append(name)
    return products


@router.get('/all')
def get_all_products():
  log("MyAPI", "Call to get all products")
  # return products
  data = " ".join(products)
  response = Response(content=data, media_type="text/plain")
  response.set_cookie(key="test_cookie", value="test_cookie_value")
  return response


@router.get("/withheader")
def get_products(
        response: Response,
        custom_header: Optional[List[str]] = Header(None),
        test_cookie: Optional[str] = Cookie(None)
):
    if custom_header:
        response.headers["custom_response_header"] = ", ".join(custom_header)
    return {
        "data": products,
        "custom_header": custom_header,
        "my_cookie": test_cookie
    }


@router.get("/{id}", responses={
    200: {
        "description": "Returns HTML for object",
        "content": {
            "text/html": {
                "example": "<div>Product</div>"
            }
        }
    },
    404: {
        "description": "A clear text error message",
        "content": {
            "text/plain": {
                "example": "Product not available"
            }
        }
    }
})
def get_product(id: int):
    if id >= len(products):
        out = "Product not available"
        return PlainTextResponse(content=out, media_type="text/plain", status_code=404)
    else:
        product = products[id]
        out = f"""
                <head>
                  <style>
                   .product {{
                    width: 500%;
                    height: 30%;
                    border: 2px inset green;
                    background-color: lightblue;
                    text-align: center;
                  }}
                  </style>
                </head>
                <div class="product">{product}</div>
                """
        return HTMLResponse(content=out, media_type="text/html")
