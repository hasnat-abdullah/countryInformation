from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_200_OK, HTTP_400_BAD_REQUEST
)
from django.shortcuts import HttpResponse
import os


class LogAPIView(APIView):
    '''
    To see desired dates log
    '''

    def get(self, request, date_n_type):

        if '.log' not in date_n_type:
            file_name= date_n_type+".log"
        else:
            file_name=date_n_type
        try:
            ROOT_DIR = os.path.abspath(os.path.dirname(__name__))  # This is your Project Root
            text = open( os.path.join(ROOT_DIR, 'log_files',file_name), 'r')
            return HttpResponse(text.read(),content_type="text/plain",
                    status=HTTP_200_OK
                )
        except Exception as ex:
            return HttpResponse("File does not exist.", status=HTTP_400_BAD_REQUEST)


