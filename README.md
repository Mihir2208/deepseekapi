# deepseekapi

Deepseek Local API with Django
This project provides a backend API built with Django that integrates with Ollama to run the Deepseek local model (deepseek-coder:33b-instruct). Users can send prompts to the API, and the Deepseek model will generate responses, which are logged to the console.

Features
Local Model Integration: Uses Ollama to run the Deepseek model locally.

Prompt-Response Workflow: Users can send prompts via API and receive responses from the Deepseek model.

No Frontend: Focuses solely on the backend implementation.

Prerequisites
macOS (tested on macOS, but should work on Linux as well).

Python 3.8+.

Ollama (for running local models).

Homebrew (recommended for installing dependencies).

Installation
1. Clone the Repository
bash
Copy
git clone <repository-url>
cd <project-directory>
2. Install Ollama
If you don’t have Ollama installed, follow these steps:

bash
Copy
curl -fsSL https://ollama.com/install.sh | sh
3. Pull the Deepseek Model
Pull the Deepseek instruct model:

bash
Copy
ollama pull deepseek-coder:33b-instruct
4. Set Up the Virtual Environment
Create and activate a virtual environment:

bash
Copy
python3 -m venv venv
source venv/bin/activate
5. Install Python Dependencies
Install the required packages:

bash
Copy
pip install django djangorestframework ollama
Configuration
1. Update Django Settings
Ensure your settings.py includes:

python
Copy
INSTALLED_APPS = [
    ...
    'rest_framework',
    'api',
]
Running the Server
1. Apply Migrations
Run the following to set up the database:

bash
Copy
python manage.py migrate
2. Start the Server
Run the Django development server:

bash
Copy
python manage.py runserver
API Endpoints
1. Generate Response
URL: http://127.0.0.1:8000/api/generate/

Method: POST

Request Body:

json
Copy
{
  "prompt": "Your prompt here"
}
Example Request:
json
Copy
{
  "prompt": "Explain quantum computing in simple terms"
}
2. Response:
json
Copy
{
  "response": "Quantum computing is a type of computing that uses quantum bits (qubits) instead of classical bits..."
}
Execution
1. Start Ollama
In one terminal, start the Ollama server:

bash
Copy
ollama serve
2. Start Django Server
In another terminal, start the Django development server:

bash
Copy
python manage.py runserver
3. Test the API
Use Postman or curl to send a POST request to http://127.0.0.1:8000/api/generate/ with the JSON body:

json
Copy
{
  "prompt": "Explain quantum computing in simple terms"
}
Example Response:
json
Copy
{
  "response": "Quantum computing is a type of computing that uses quantum bits (qubits) instead of classical bits..."
}
Troubleshooting
1. Check Logs
If you encounter issues, check the logs for errors.

Summary
This project provides a backend API for interacting with the Deepseek local model. It allows users to send prompts and receive responses, which are logged to the console.

**Let me know if you need further assistance! 🚀
Let me know if you need further assistance! 🚀

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please open an issue or submit a pull request.
