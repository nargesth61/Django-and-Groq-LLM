# **Project: Content Upload and Summarization Management API**

A simple API project that uses a test to receive a file, store its summary in a database, and display a list of files with their summary.
---

## **Features**
- Upload text file in `text/plain` format
- Connect to Groq API for content summarization
- Store file information and summaries in  database
---

## **Prerequisites**
1. Python 3.8+
2. Groq API access and API key
3. Tools required:
- Docker
- Postman for API testing
---

## **Installation and launch of the project**

### 1. Cloning the repository
```bash
git clone https://github.com/nargesth61/Django-and-Groq-LLM.git
cd <project-directory>

docker-compose up --build

for migrations database:
docker-compose run web bash
python manage.py makemigrations
python manage.py migrate

# **Endpoints**

## **1. Upload File **
- **URL**: `http://localhost:8000/api/upload/`
- **Method**: `POST`
- **Description**: This endpoint receives a text file uploaded by the user, summarizes the content using the Groq API, and stores the result along with the file information.

## **2.Get Summary**
- **URL**: `http://localhost:8000/api/history/`
- **Method**: `GET`
- **Description**: This endpoint return list of file data with summary for user.

