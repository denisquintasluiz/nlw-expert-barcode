from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
class TagCreatorView:
    '''
      responsability for interacting whit http
    '''
    def validate_and_create(self, http_request: HttpRequest):
        #body = http_request.body
        #product_code = body["product_code"]

        # logica de implemntação
        print("Estou na minha casa de noite!")
        print(http_request)
        #retorno
        return HttpResponse(status_code=200, body={"hello": "here"})
