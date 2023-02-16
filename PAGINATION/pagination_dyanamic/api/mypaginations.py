from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 5

#########################################
    page_query_param = 'p' #<-----------------you can set the url container word as can chociese like page as p------------------------>

    page_size_query_param = 'records'  #<------------you use this query param of use the records word and set any record values like records=10------------------------------------>

    max_page_size = 7   #<--------------you can set the dyanamically page client site like records or p = any value-------------------------->

    last_page_strings = 'end' #<--------------similar like page_size_query_param------------------------------------->