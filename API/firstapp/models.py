from django.db import models

class ProjectModel(models.Model):
    str_name=models.CharField(max_length=50,null=False)
    str_code=models.CharField(max_length=5,null=False)


    def __str__(self):
        return self.str_name

class WorkTypeModel(models.Model):
    str_name = models.CharField(max_length=50, null=False)
    int_order=models.IntegerField(null=False)

    def __str__(self):
        return self.str_name

class WorkStatusModel(models.Model):
    choices=(
        ('new','new'),
        ('developed','developed'),
        ('tested','tested'),
        ('deployed','deployed')
    )
    str_name = models.CharField(choices=choices,max_length=50, null=False)
    str_code = models.CharField(max_length=50, null=False)
    int_order = models.IntegerField(null=False)

    def __str__(self):
        return self.str_name

class WorksModel(models.Model):
    str_title=models.CharField(max_length=300,null=False)
    txt_descrption=models.TextField(null=False)
    fk_project_id=models.ForeignKey(ProjectModel,on_delete=models.CASCADE,null=False)
    jsn_attachment=models.JSONField(null=True,blank=True)
    dat_created=models.DateField(auto_now_add=True, auto_now=False, blank=True)
    fk_type_id=models.ForeignKey(WorkTypeModel,on_delete=models.CASCADE)
    fk_work_status_id=models.ForeignKey(WorkStatusModel,on_delete=models.CASCADE)
    int_active=models.IntegerField(default=0)

    def __str__(self):
        return self.str_title
