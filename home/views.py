from django.shortcuts import render
from pymongo import MongoClient
from datetime import datetime
from jobb.utils import db 
from django.http import JsonResponse


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
from django.shortcuts import render
from pymongo import MongoClient

# Assuming MongoDB connection is set up and you have a MongoDB client 'db'
# Example: db = MongoClient()['your_database_name']

def home_page(request):
    # Get filter parameters from the GET request
    keyword = request.GET.get('keyword', '')
    location = request.GET.get('location', '')
    job_type = request.GET.get('job_type', '')

    # Initialize the query dictionary for MongoDB filtering
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
    
    # Convert MongoDB's ObjectId to string for easier handling in the template
    jobs = [convert_objectid_to_str(job) for job in jobs]

    # Prepare context data to pass to the template
    context = {
        'jobs': jobs,  # List of filtered jobs
        'keyword': keyword,  # Current keyword filter
        'location': location,  # Current location filter
        'job_type': job_type,  # Current job type filter
    }

    # Render the template with the context
    return render(request, 'home.html', context)

