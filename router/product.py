from fastapi.responses import Response, HTMLResponse, PlainTextResponse

from fastapi import APIRouter

router = APIRouter(
    prefix="/product",
    tags=["product"]
)

products = ["watch", "phone", "laptop"]


@router.get("/all")
def get_all_products():
    data = " ".join(products)
    return Response(content=data, media_type="text/plain")


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
