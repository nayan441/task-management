# Django Project Setup and Running Guide

## Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- Virtualenv (optional but recommended)

## Cloning the Repository
```sh
git clone https://github.com/your-username/your-django-project.git
cd your-django-project
```

## Setting Up the Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

## Configuring the Environment Variables
Copy the `.env.example` file to `.env` and update the necessary values:
```sh
cp .env.example .env
```

## Database Setup
Run the following commands to apply migrations and create a superuser:
```sh
python manage.py makemigrations
python manage.py migrate
```

## Running the Project
To start the Django development server:
```sh
python manage.py runserver 8000
```
## API Documentetion
Swagger UI document is integrated. You can access it through below command.
```sh
http://127.0.0.1:8000/swagger/
```

## License
This project is licensed under the MIT License.

## Contact
For any issues, contact [ynayan93@gmail.com](mailto:ynayan93@gmail.com).

