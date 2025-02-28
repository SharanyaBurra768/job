from django.shortcuts import render
from pymongo import MongoClient
from datetime import datetime
from jobb.utils import db 
from django.http import JsonResponse
from django.shortcuts import render, redirect
from pymongo import MongoClient

def convert_objectid_to_str(doc):
    if '_id' in doc:
        doc['_id'] = str(doc['_id']) 
    return doc

def convert_objectid_to_str(doc):
    if '_id' in doc:
        doc['_id'] = str(doc['_id'])
    return doc

def job_detail(request, job_id):
    jobs_collection = db['job']  
    applications_collection = db['applications']
    jobs = list(jobs_collection.find({'job_id': job_id}))  
    if request.method == 'POST':
        if not request.session.get('username'):
            return render(request, 'home.html')
        applicant_name = request.POST.get('applicant_name')
        applicant_email = request.POST.get('applicant_email')

        application = {
            'job_id': job_id,
            'applicant_name': applicant_name,
            'applicant_email': applicant_email,
            'username': request.session.get('username'),
        }

        applications_collection.insert_one(application)

        return redirect('job_detail', job_id=job_id)

    return render(request, 'job_detail.html', {'job': jobs[0]})


def home_page(request):
    keyword = request.GET.get('keyword', '')
    location = request.GET.get('location', '')
    job_type = request.GET.get('job_type', '')

    query = {}
    
    if keyword:
        query['title'] = {'$regex': keyword, '$options': 'i'} 
    if location:
        query['location'] = {'$regex': location, '$options': 'i'}  
    if job_type:
        query['job_type'] = {'$regex': job_type, '$options': 'i'} 

    jobs_collection = db['job']

    jobs = []
    if len(query) == 0:
    	jobs = list(jobs_collection.find())    
    else:
    	jobs = jobs_collection.find(query)
    
    jobs = [convert_objectid_to_str(job) for job in jobs]

    is_logged_in = 'user_id' in request.session  
    username = None
    if 'username' in request.session   :
        username = request.session['username']
    context = {
        'jobs': jobs,  
        'keyword': keyword, 
        'location': location, 
        'job_type': job_type,  
        'is_logged_in': is_logged_in,
        'username': username,
    }


    return render(request, 'home.html', context)

