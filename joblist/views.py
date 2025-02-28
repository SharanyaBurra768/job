from django.shortcuts import render
from jobb.utils import db 
from django.http import JsonResponse
# Create your views here.
def convert_objectid_to_str(doc):
    if '_id' in doc:
        doc['_id'] = str(doc['_id'])  
    return doc

def get_jobs(request):
    jobs_collection = db['job']  
    jobs = list(jobs_collection.find())  
    jobs_list = [convert_objectid_to_str(job) for job in jobs]
    return render(request, 'job.html', {'jobs': jobs})


def job_detail(request, job_id):
    jobs_collection = db['job']  
    applications_collection = db['applications']
    jobs = list(jobs_collection.find({'job_id': job_id}))  
    if request.method == 'POST':
        applicant_name = request.POST.get('applicant_name')
        applicant_email = request.POST.get('applicant_email')
        print(88888888888888888)

        application = {
            'job_id': job_id,
            'applicant_name': applicant_name,
            'applicant_email': applicant_email,
        }

        applications_collection.insert_one(application)

        print(11)
        return redirect('job_detail', job_id=job_id)


    else:
        form = JobApplicationForm()
    return render(request, 'job_detail.html', {'job': job, 'form': form})