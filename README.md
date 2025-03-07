# Nutrient Counter App 🍽️

A Django-based web application that helps users track their daily food consumption, set macronutrient goals, and visualize progress using Chart.js.

---

## 🚀 Features
- **User Authentication**: Register, login, and logout functionality.
- **Food Tracking**: Select food items from a shared database and track daily consumption.
- **Custom Nutrition Goals**: Set calorie, carbohydrate, protein, and fat goals.
- **Data Visualization**: View progress with bar, pie, and line charts.
- **Calorie Progress Bar**: See your daily calorie intake vs. goal.
- **Food Management**: Add new food items to the global database.
- **Mobile-Friendly UI**: Responsive design with Bootstrap.

---

## 📂 Project Structure
```
nutrient_counter/
│── n_counter/          # Django project settings
│── app/                # Main Django app
│   ├── migrations/     # Database migrations
│   ├── templates/      # HTML templates
│   │   ├── app/
│   │   │   ├── index.html
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   ├── add_food.html
│   │   │   ├── update_goals.html
│   │   │   ├── delete.html
│   ├── static/         # Static files (CSS, JS)
│   ├── models.py       # Database models
│   ├── views.py        # View functions
│   ├── forms.py        # Forms for user input
│   ├── urls.py         # URL routing
│── db.sqlite3          # SQLite database
│── manage.py           # Django management script
│── README.md           # Project documentation
```

---

## 🔧 Installation & Setup
### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/yourusername/nutrient-counter.git
cd nutrient-counter
```

### 2️⃣ **Create & Activate Virtual Environment**
```sh
python -m venv venv
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 4️⃣ **Run Migrations**
```sh
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ **Create Superuser**
```sh
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### 6️⃣ **Start the Development Server**
```sh
python manage.py runserver
```
Visit: `http://127.0.0.1:8000/`

---

## 📌 Usage
1. **Register/Login**: Create an account and log in.
2. **Set Goals**: Navigate to "Update Goals" and set daily intake targets.
3. **Add Food**: Select food items and track consumption.
4. **View Charts**: Analyze progress through visual graphs.
5. **Manage Food Items**: Admins can add food to the shared database.

---

## 📊 Data Visualization
The app uses **Chart.js** to display:
- **Bar Chart**: Shows actual intake vs. daily goals.
- **Pie Chart**: Displays macronutrient breakdown.
- **Line Chart**: Tracks calorie trends over time.
- **Progress Bar**: Indicates progress toward daily calorie goals.

---

## 🛠 Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML, Bootstrap, JavaScript
- **Database**: SQLite (default, but can be switched to PostgreSQL)
- **Charts**: Chart.js
