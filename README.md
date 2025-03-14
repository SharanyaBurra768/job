# Jobb (Job Recommendation System)


## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [API Doc]()

## Introduction
The **Job Recommendation System** is a Django web application designed to simplify the job search process. 

Main functionalities:

User:
- Viewing job listings and detailed job descriptions.
- Submitting job applications.
- Managing user profiles.
- Uploading and updating resumes.
- Receiving personalized job recommendations.

Employer:
- View job application
- Post a new job.



## Features
- **Job Viewing:** Browse available job postings and view detailed descriptions.
- **Job Application:** Submit applications for jobs directly through the platform.
- **User Profile Management:** View and update user profiles.
- **Resume Submission:** Upload and update resumes.
- **Job Recommendations:** Receive tailored job recommendations based on your profile and application history.

## Installation

### Prerequisites and Dependency (Tech Stack)
- Python
- Django 
- MongoDB
- HTML
- CSS
- JavaScript

### Setup 
1. **Clone the Repository**

2. **Navigate to the Project Directory**

3. **Install Dependencies**

4. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```


## API Doc (Not complete)

### Job Endpoints

#### GET `/jobs/`
Retrieves a list of available jobs.

**Request:**
```bash
curl -X GET http://localhost:8000/jobs/
```

**Response:**
```json
[
  {
    "id": "1",
    "title": "Software Engineer",
    "description": "Job description here",
    "company": "Tech Corp",
    "location": "City, Country"
  }
]
```

#### GET `/jobs/{job_id}/`
Retrieves detailed information for a specific job.

**Request:**
```bash
curl -X GET http://localhost:8000/jobs/job1/
```

**Response:**
```json
{
  "id": "job1",
  "title": "Software Engineer",
  "description": "Detailed job description",
  "requirements": "Job requirements",
  "company": "Tech Corp",
  "location": "City, Country"
}
```


#### POST `/applications/`
Submits a job application.


**Response:**
```json
{
  "status": "success",
  "message": "Application submitted successfully."
}
```

### Resume Endpoints

#### POST `/resume/`
Submits or updates a user's resume.


**Response:**
```json
{
  "status": "success",
  "message": "Resume submitted successfully."
}
```

### Recommendation Endpoints

#### GET `/recommendations/`
Retrieves personalized job recommendations for the user.

**Request:**
```bash
curl -X GET "http://localhost:8000/recommendations/?user_id=user123"
```

**Response:**
```json
[
  {
    "id": "2",
    "title": "Data Scientist",
    "description": "Job description here",
    "company": "Analytics Inc.",
    "location": "City, Country"
  }
]
```

### User Endpoints

#### GET `/profile/`
Retrieves the profile information of a user.

**Request:**
```bash
curl -X GET http://localhost:8000/profile/
```

**Response:**
```json
{
  "user_id": "user123",
  "name": "John Doe",
  "email": "john.doe@test.com",
}
```

#### PUT `/profile/`
Updates the user's profile information.


**Response:**
```json
{
  "status": "success",
  "message": "Profile updated successfully."
}
```
