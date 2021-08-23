
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from rest_framework import status
from django.db.models import Q
from datetime import datetime
date=datetime.now()
# from .filters import WorksFilter

class ProjectView(APIView):
    def get(self, request):
        res_data = list(ProjectModel.objects.all().values("id","str_name"))
        return Response(res_data, status=status.HTTP_200_OK)

class WorkStatusView(APIView):
    def get(self, request):
        res_data = list(WorkStatusModel.objects.all().values("id","str_name"))
        return Response(res_data, status=status.HTTP_200_OK)

class WorkTypeView(APIView):
    def get(self, request):
        res_data = list(WorkTypeModel.objects.all().values("id","str_name"))
        return Response(res_data, status=status.HTTP_200_OK)





class WorksGetPost(APIView):
    def get(self, request):
        res_data = list(WorksModel.objects.filter(int_active__gte=0).values("id","str_title","txt_descrption","fk_project_id_id","jsn_attachment",
                                                   "dat_created","fk_type_id_id",
                                                   "fk_work_status_id_id","int_active"))
        return Response(res_data, status=status.HTTP_200_OK)

    # def post(self, request):
    #     dict_data = request.data
    #     fk_project_id_id = dict_data["fk_project_id_id"] #oxgen digit
    #     project=ProjectModel.objects.filter(str_name=fk_project_id_id).get()
    #     int_project_id=project.id
    #     ins_project = ProjectModel.objects.get(id=int_project_id)
    #     fk_type_id_id = dict_data["fk_type_id_id"] #"bug"
    #     worktype=WorkTypeModel.objects.filter(str_name=fk_type_id_id).get()
    #     int_type_id=worktype.id
    #     ins_worktype = WorkTypeModel.objects.get(id=int_type_id)
    #     fk_work_status_id_id = dict_data["fk_work_status_id_id"]
    #     workstatus=WorkStatusModel.objects.filter(str_name=fk_work_status_id_id).get()
    #     int_workstatus_id=workstatus.id
    #
    #     ins_work_status = WorkStatusModel.objects.get(id=int_workstatus_id)
    #
    #     WorksModel.objects.create(str_title=dict_data["str_title"], txt_descrption=dict_data["txt_descrption"],
    #                                      fk_project_id=ins_project,
    #                                      jsn_attachment=dict_data["jsn_attachment"], fk_type_id=ins_worktype,
    #                                      fk_work_status_id=ins_work_status,
    #                                      int_active=0)
    #     return Response("saved",status=status.HTTP_200_OK)
    def post(self, request):
        dict_data = request.data
        fk_project_id_id = dict_data["fk_project_id_id"] #oxgen digit
        project=ProjectModel.objects.get(id=fk_project_id_id)
        fk_type_id_id = dict_data["fk_type_id_id"] #"bug"
        worktype=WorkTypeModel.objects.get(id=fk_type_id_id)
        fk_work_status_id_id = dict_data["fk_work_status_id_id"]
        workstatus=WorkStatusModel.objects.get(id=fk_work_status_id_id)


        WorksModel.objects.create(str_title=dict_data["str_title"], txt_descrption=dict_data["txt_descrption"],
                                         fk_project_id=project,
                                         jsn_attachment=dict_data["jsn_attachment"], fk_type_id=worktype,
                                         fk_work_status_id=workstatus,
                                         int_active=0)
        return Response("saved",status=status.HTTP_200_OK)


class WorkUpdate(APIView):
    def put(self, request, id):
        dict_data = request.data
        fk_project_id_id = dict_data["fk_project_id_id"]
        ins_project = ProjectModel.objects.get(id=fk_project_id_id)
        fk_type_id_id = dict_data["fk_type_id_id"]
        ins_worktype = WorkTypeModel.objects.get(id=fk_type_id_id)
        fk_work_status_id_id = dict_data["fk_work_status_id_id"]
        ins_work_status = WorkStatusModel.objects.get(id=fk_work_status_id_id)
        ins_works = WorksModel.objects.get(id=id)
        ins_works.str_title=dict_data["str_title"]
        ins_works.text_descrption=dict_data["txt_descrption"]
        ins_works.fk_project_id=ins_project
        ins_works.jsn_attachment = dict_data["jsn_attachment"]
        ins_works.fk_type_id = ins_worktype
        ins_works.fk_work_status_id=ins_work_status
        ins_works.int_active = 1
        ins_works.save()
        return Response("updated", status=status.HTTP_200_OK)


class WorkDelete(APIView):
    def put(self, request, id):
        ins_works = WorksModel.objects.get(id=id)
        ins_works.int_active = -1
        ins_works.save()
        return Response("updated", status=status.HTTP_200_OK)



class DateFilter(APIView):
    def get(self,request):
        print(request.data)
        res_data = list(WorksModel.objects.all().filter(Q(dat_start= "2021-08-20") & Q(dat_end="2021-08-30")).values("str_title","txt_descrption","fk_project_id__str_name",
                                                   "jsn_attachment","dbl_estimatation","dat_start",
                                                   "dat_end","dat_created","fk_type_id__str_name","dat_approved",
                                                   "fk_work_status_id__str_name","dbl_taken","int_active"))
        return Response(res_data, status=status.HTTP_200_OK)

class GetCurrentDate(APIView):
    def get(self,request):
        return Response(date, status=status.HTTP_200_OK)


