# 🎯 Healthy Habits Tracker (Habit Tracker API)

An elegant and smart backend for anyone who wants to incorporate healthy habits into their life.
The project doesn’t just store data—it also tracks your progress and sends task reminders via a **Telegram bot**.

---

## 🚀 How It Works (Behind the Scenes)

The project uses a combination of several powerful tools:

1. **Django REST Framework** processes requests, verifies authorization tokens, and filters data.
2. **Celery Beat** is the system’s internal alarm clock. Every minute, it wakes up and checks the database.
3. **Celery Worker** retrieves a task to be sent and instantly forwards the message to Telegram via the API.
4. **Redis** acts as an invisible courier, delivering tasks from the scheduler (Beat) to the executor (Worker).

---

## 💻 Running the Project Locally

You can run the project in two ways: the classic way—using Poetry—or the quick way—using Docker.

### Option 1. Running via Docker (recommended)

Make sure you have Docker Desktop installed and running.

1. **Clone the repository:**
   ```bash
   git clone git@github.com:imnaur/coursework_5.git
   cd coursework_5
2. **Create a .env configuration file in the project’s root directory and fill it with your information:**
   Follow the example in the .env_template file
3. **Start the containers:**
   docker compose up --build
   The system will automatically download the images and build Django, Postgres, Redis, and Celery. The project will be
   accessible at http://localhost/.

### Option 2. Running via Poetry (For Development)

1. **Install dependencies::**
   poetry install
2. **Apply migrations and create a superuser::**
   poetry run python manage.py migrate
   poetry run python manage.py createsuperuser
3. **Start the local server::**
   poetry run python manage.py runserver
   (For deferred tasks to work in this mode, you’ll need to run Redis, Celery Worker, and Celery Beat separately in
   parallel terminals.)

## 🛠 Setting up CI/CD and automated deployment

The project has a fully-fledged automation pipeline (CI/CD) set up using GitHub Actions.
Every time you git push to the main branch, the code is validated and automatically deployed to the server.

## How the pipeline works (.github/workflows/deploy.yml):

**Lint (Flake8):** Checks code style for compliance with PEP8 standards.

**Run Tests:** Starts a temporary PostgreSQL database in a container, applies migrations, and runs Django tests.

**Deploy to Server:** If successful, connects to the remote server via SSH, updates the code from Git, and restarts the
Docker containers.

## Steps to set up deployment to a new server:

**Preparing the server (Ubuntu):**

Install Docker and Docker Compose on the target server.

Add your user to the docker group: sudo usermod -aG docker $USER.

Clone the repository to your home directory on the server once manually: git clone git@github.com:
imnaur/coursework5.git ~/coursework5.

## Configuring GitHub Secrets:

Go to your GitHub repository: Settings -> Secrets and variables -> Actions, and add the following secrets:

SERVER_HOST — The public IP address of your virtual machine (e.g., Yandex Cloud/Amazon Cloud).

SERVER_USER — The username for connecting via SSH (e.g., ubuntu).

SSH_PRIVATE_KEY — The contents of your private SSH key

Now, any code push to the main branch will automatically update the project on the remote server.

## 🔒 Security and CORS Configuration

To ensure that a frontend application (e.g., built with React or Vue) can safely send requests to our API, the
django-cors-headers package is configured in the project.
Allowed frontend origins are configured in the settings.py file via the CORS_ALLOWED_ORIGINS variable.

