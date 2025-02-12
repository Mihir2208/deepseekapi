from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import ollama

class GenerateView(APIView):
    def post(self, request):
        prompt = request.data.get('prompt', '')
        if not prompt:
            return Response({'error': 'Prompt is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            response = ollama.generate(
                model='deepseek-r1:latest',
                prompt=prompt,
                stream=False
            )
            answer = response['response']
            print(f"Prompt: {prompt}\nResponse: {answer}\n{'='*50}")
            return Response({'response': answer})
        
        except Exception as e:
            print(f"Error: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)