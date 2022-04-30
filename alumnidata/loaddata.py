import pandas as pd
from alumnidata.models import fieldstudy, job, education, success

def load_job():
    alumnijob = job.objects.all()
    jobData = [
        {
            'Alumni': x.alumniuser,
            'Organization': x.organization,
            'Type': x.organizeType,
            'Department': x.department,
            'JobTitle': x.jobTitle,
            'JobDesc': x.jobDesc
        } for x in alumnijob
    ]
    df = pd.DataFrame(jobData)
    return df

def load_fieldstudy():
    alumnifofs = fieldstudy.objects.all()
    studyData = [
        {
            'Alumni': x.alumniuser,
            'studyField': x.studyField,
            'studyMajor': x.studyMajor,
            'studyMinor': x.studyMinor,
            'yearStart': x.yearStart,
            'yearGraduate': x.yearGraduate,
            'gpa': x.gpa
        } for x in alumnifofs
    ]
    df = pd.DataFrame(studyData)
    return df

def load_education():
    alumnieducation = education.objects.all()
    educationData = [
        {
            'Alumni': x.alumniuser,
            'degree': x.degree,
            'university': x.university,
            'faculty': x.faculty,
            'major': x.major,
            'country': x.country
        } for x in alumnieducation
    ]
    df = pd.DataFrame(educationData)
    return df

def load_success():
    alumnisuccess = success.objects.all()
    successData = [
        {
            'Alumni': x.alumniuser,
            'achieveTitle': x.achieveTitle,
            'desc': x.desc,
            'achieveDate': x.achieveDate
        } for x in alumnisuccess
    ]
    df = pd.DataFrame(successData)
    return df