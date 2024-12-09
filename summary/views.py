from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.exceptions import ParseError
from .models import UploadedFile
import requests
import logging


logger = logging.getLogger(__name__)

class UploadFileAPIView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        try:
            file = request.FILES.get('file')
            if not file:
                logger.error("No file uploaded")
                return JsonResponse({"error": "No file uploaded"}, status=400)

            content = file.read().decode('utf-8')
            groq_api_url = "https://api.groq.com/openai/v1/chat/completions"
            api_key = request.environ.get('GROQ_API_KEY')

            if not api_key:
                logger.error("API key is missing")
                return JsonResponse({"error": "API key is missing"}, status=500)

            # درخواست به Groq API با استفاده از 'messages' به جای 'text'
            response = requests.post(
                groq_api_url,
                json={
                    "model": "llama3-8b-8192",  # این مدل را با مدل مورد نظر خود جایگزین کنید
                    "messages": [{
                        "role": "user",
                        "content": content
                    }]
                },
                headers={"Authorization": f"Bearer {api_key}"}
            )

            if response.status_code != 200:
                logger.error(f"Groq API Error: {response.text}")
                return JsonResponse({"error": "Failed to summarize the content"}, status=500)

            summary = response.json().get("choices")[0].get("message", {}).get("content")
            if not summary:
                logger.error("Groq API response did not contain summary")
                return JsonResponse({"error": "Failed to retrieve summary"}, status=500)

            # ذخیره در پایگاه داده
            uploaded_file = UploadedFile.objects.create(name=file.name, summary=summary)

            return JsonResponse({
                "summary": summary,
                "file_id": uploaded_file.id,
            }, status=201)

        except ParseError:
            logger.exception("Error parsing the uploaded file")
            return JsonResponse({"error": "Invalid file format"}, status=400)

        except Exception as e:
            logger.exception("An unexpected error occurred")
            return JsonResponse({"error": str(e)}, status=500)