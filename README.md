# Task-Manager
# Task Management System (Django + MySQL)

## 1. Overview of the Project

This project is a **Task Management Web Application** built using **Django (Python) and MySQL** following the **MVC/MVT architectural pattern**.

The application allows users to manage tasks efficiently by providing features such as:

* Create new tasks
* View all tasks
* Update existing tasks
* Delete tasks
* Search tasks
* Filter tasks by status
* Dashboard statistics
* Expandable task descriptions
* Due date alerts

The application provides a clean and responsive interface using **Bootstrap** and demonstrates the implementation of **CRUD operations, database design, MVC architecture, and user-friendly UI components**.

This project was built as part of the **Oritso Entry Level IT Assignment** to demonstrate knowledge of backend development, frontend integration, and database management.

---

# 2. Project Screenshots

### Dashboard

<img width="2465" height="723" alt="image" src="https://github.com/user-attachments/assets/20069d8b-b24d-4859-bdec-7b27a2a1a07d" />

---

### Task List

<img width="2382" height="691" alt="image" src="https://github.com/user-attachments/assets/1272f0d9-7e66-401b-8be7-fcf4e9d58d38" />


### Add Task Form


<img width="1120" height="1741" alt="image" src="https://github.com/user-attachments/assets/06b9021f-d0cf-4612-aacc-fa21a2d0760c" />


### Expandable Task Description

<img width="2530" height="1000" alt="image" src="https://github.com/user-attachments/assets/1ec6f3bc-adbd-46d0-a9bb-94e27130ab68" />


# 3. Database Design

The system uses a **Relational Database (MySQL)** to store task data.

The main entity in the system is the **Task** table which stores information related to task management.

## 3.1 ER Diagram

```
+--------------------+
|        Task        |
+--------------------+
| id (Primary Key)   |
| title              |
| description        |
| due_date           |
| status             |
| remarks            |
| created_on         |
| updated_on         |
| created_by         |
| updated_by         |
+--------------------+
```

The **Task entity** represents individual tasks created by the user.

---

## 3.2 Data Dictionary

| Column      | Data Type | Description                                |
| ----------- | --------- | ------------------------------------------ |
| id          | Integer   | Primary key identifying each task          |
| title       | CharField | Title or name of the task                  |
| description | TextField | Detailed description of the task           |
| due_date    | DateField | Deadline for the task                      |
| status      | CharField | Current status (Pending / Completed)       |
| remarks     | TextField | Additional notes or comments               |
| created_on  | DateTime  | Timestamp when task was created            |
| updated_on  | DateTime  | Timestamp when task was last updated       |
| created_by  | CharField | Name of the user who created the task      |
| updated_by  | CharField | Name of the user who last updated the task |

---

## 3.3 Indexes Used

Indexes improve database query performance.

The following fields are commonly used in search and filtering operations and can be indexed:

| Field    | Purpose                                        |
| -------- | ---------------------------------------------- |
| id       | Primary key index for fast lookup              |
| status   | Used for filtering tasks (Pending / Completed) |
| due_date | Used for identifying overdue tasks             |

Primary key indexing is automatically handled by Django ORM.

---

## 3.4 Code First vs Database First

This project follows the **Code First Approach**.

### Reason

The database schema is defined using **Django Models**, and Django automatically generates the database tables through migrations.

Advantages of this approach:

* Faster development
* Easier schema modifications
* Database structure is maintained within the codebase
* Version control friendly

Example Model:

```
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=50)
```

---

# 4. Application Architecture

The project follows the **MVC (Model View Controller)** pattern implemented in Django as **MVT (Model View Template)**.

| MVC        | Django Equivalent |
| ---------- | ----------------- |
| Model      | Django Models     |
| Controller | Django Views      |
| View       | Django Templates  |

### Application Flow

```
User Request
    ↓
URL Routing
    ↓
View (Business Logic)
    ↓
Model (Database Interaction)
    ↓
Template (HTML Rendering)
    ↓
Response Sent to User
```

This architecture separates concerns and ensures maintainability and scalability.

---

## 4.1 Application Type

This application uses:

```
Standard MVC Server Side Page Rendering (MPA)
```

The server generates HTML pages using Django templates.

This approach was chosen because:

* Simpler implementation
* Faster development
* Suitable for small to medium applications
* Better for assignment scope

---

# 5. Frontend Structure

The frontend is implemented using:

* HTML
* Bootstrap
* Django Template Engine

Bootstrap is used to provide responsive UI components and modern styling.

### Main UI Features

* Dashboard with statistics
* Task list table
* Expandable task details
* Task filtering tabs
* Calendar date picker
* Due date warning colors
* CRUD action buttons

---

### Frontend Pages

| Page      | Description              |
| --------- | ------------------------ |
| Dashboard | Displays task statistics |
| Task List | Shows all tasks          |
| Add Task  | Form to create new tasks |
| Edit Task | Form to modify tasks     |

---

# 6. Key Features Implemented

The system supports the following operations:

### Create

Users can create tasks with title, description, due date, and remarks.

### Read

All tasks can be viewed in the task list page.

### Update

Existing tasks can be modified.

### Delete

Tasks can be removed from the system.

### Search

Users can search tasks using keywords.

### Filtering

Tasks can be filtered by:

* All
* Pending
* Completed
* Overdue

### Expandable Task Details

Clicking on a task expands it to show:

* Description
* Remarks

### Due Date Alerts

Tasks close to the due date are highlighted:

| Color  | Meaning  |
| ------ | -------- |
| Red    | Overdue  |
| Orange | Due soon |

---

# 7. Build and Installation

## 7.1 Environment Details

Required Software:

* Python 3.x
* Django
* MySQL
* Git

---

## 7.2 Dependencies

Install dependencies using:

```
pip install -r requirements.txt
```

Main libraries used:

* Django
* mysqlclient
* Bootstrap (CDN)

---

## 7.3 Installation Steps

Clone the repository:

```
git clone https://github.com/yourusername/task-manager.git
```

Navigate to project directory:

```
cd task-manager
```

Install dependencies:

```
pip install -r requirements.txt
```

Apply migrations:

```
python manage.py migrate
```

Run the development server:

```
python manage.py runserver
```

Open the application:

```
http://127.0.0.1:8000
```

---

# 8. Project Structure

```
task-manager
│
├── taskmanager
│
├── tasks
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── templates
│   └── tasks
│       ├── dashboard.html
│       ├── task_list.html
│       ├── add_task.html
│       └── edit_task.html
│
├── static
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# 9. Conclusion

This project demonstrates the implementation of a **Task Management System using Django and MySQL**.

The system successfully implements:

* MVC architecture
* Database design principles
* CRUD operations
* User-friendly interface
* Task filtering and alerts
* Expandable task descriptions

The application showcases fundamental skills in **backend development, frontend integration, database management, and project documentation**.

---

# 10. System Architecture Diagram

The system follows a layered architecture where the user interacts with the frontend interface, which communicates with the Django backend. The backend processes the request, interacts with the database, and returns the response to the user.

### Architecture Flow

```
User (Browser)
       |
       v
Frontend (HTML + Bootstrap + Django Templates)
       |
       v
Django Views (Business Logic)
       |
       v
Django Models (ORM)
       |
       v
MySQL Database
```

### Explanation

1. **User Interface Layer**

   * The user interacts with the system through web pages built with HTML and Bootstrap.
   * Django templates dynamically render data on the frontend.

2. **Application Logic Layer**

   * Django views handle user requests and implement business logic.
   * CRUD operations are processed here.

3. **Data Access Layer**

   * Django Models interact with the MySQL database using Django ORM.
   * The ORM converts Python code into SQL queries.

4. **Database Layer**

   * The MySQL database stores task-related information including title, description, due date, and status.

This layered architecture improves maintainability, scalability, and separation of concerns.

---

# 11. Future Improvements

Although the current system provides complete task management functionality, several improvements can further enhance the application.

### 1. User Authentication System

Allow users to register and log in so that each user can manage their own tasks securely.

### 2. Email Notifications

Send email reminders to users when task deadlines are approaching.

### 3. Task Categories

Allow tasks to be grouped into categories such as Work, Study, Personal, etc.

### 4. File Attachments

Allow users to attach documents or files to tasks.

### 5. API Integration

Create REST APIs using Django REST Framework to allow mobile or third-party integrations.

### 6. Charts and Analytics

Add graphical dashboards displaying statistics such as task completion rate and productivity trends.

### 7. Real-Time Notifications

Use WebSockets or background workers to notify users when tasks become overdue.

### 8. Mobile Application

Develop a mobile version of the application using the backend APIs.

These improvements can transform the current system into a **full-featured productivity management platform**.


# 12. Author

*Siddhant Pratap Singh
*B.Tech Computer Science
*ABES Institute of Technology
