from django.shortcuts import render
from pymongo import MongoClient
from datetime import datetime
from jobb.utils import db 
from django.http import JsonResponse
from django.shortcuts import render
from pymongo import MongoClient

def convert_objectid_to_str(doc):
    if '_id' in doc:
        doc['_id'] = str(doc['_id'])  # Convert ObjectId to string
    return doc


# Function to convert ObjectId to string
def convert_objectid_to_str(doc):
    if '_id' in doc:
        doc['_id'] = str(doc['_id'])
    return doc

# Home page with search and filter functionality


def home_page(request):
    # Get filter parameters from the GET request
    keyword = request.GET.get('keyword', '')
    location = request.GET.get('location', '')
    job_type = request.GET.get('job_type', '')

    query = {}
    
    # Add filtering conditions based on the provided parameters
    if keyword:
        query['title'] = {'$regex': keyword, '$options': 'i'}  # Case-insensitive match for job title
    if location:
        query['location'] = {'$regex': location, '$options': 'i'}  # Case-insensitive match for location
    if job_type:
        query['job_type'] = {'$regex': job_type, '$options': 'i'}  # Case-insensitive match for job type

    # Access the jobs collection from your MongoDB database
    jobs_collection = db['job']

    jobs = []
    if len(query) == 0:
    	jobs = list(jobs_collection.find())    
    else:
    	jobs = jobs_collection.find(query)
    
    jobs = [convert_objectid_to_str(job) for job in jobs]

    # Prepare context data to pass to the template
    is_logged_in = 'user_id' in request.session  
    username = None
    if 'username' in request.session   :
        username = request.session['username']
    context = {
        'jobs': jobs,  # List of filtered jobs
        'keyword': keyword, 
        'location': location, 
        'job_type': job_type,  
        'is_logged_in': is_logged_in,
        'username': username,
    }


    # Render the template with the context
    return render(request, 'home.html', context)

