from django.shortcuts import render
from jobb.utils import db 
from django.http import JsonResponse
# Create your views here.
def convert_objectid_to_str(doc):
    if '_id' in doc:
        doc['_id'] = str(doc['_id'])  # Convert ObjectId to string
    return doc

def get_jobs(request):
    jobs_collection = db['job']  # Replace 'jobs' with your collection name
    jobs = list(jobs_collection.find())  # Fetch data, excluding MongoDB's _id
    jobs_list = [convert_objectid_to_str(job) for job in jobs]
    return render(request, 'job.html', {'jobs': jobs})