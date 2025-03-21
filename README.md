# **Task Manager API**

A Django REST Framework (DRF) based API for managing tasks. This API allows users to create, read, update, and delete tasks. It includes user authentication, authorization, and filtering features.

---

## **Features**
- **User Authentication**: Token-based authentication using JWT (JSON Web Tokens).
- **Task Management**:
  - Create a new task.
  - List all tasks.
  - Retrieve details of a specific task.
  - Update a task.
  - Delete a task.
- **Authorization**:
  - Only authenticated users can create, update, or delete tasks.
  - Only the task owner can update or delete their tasks.
- **Filtering and Searching**:
  - Filter tasks by `completed` status.
  - Search tasks by `title` and `description`.

---

## **Technologies Used**
- **Backend**: Django, Django REST Framework (DRF)
- **Authentication**: JWT (JSON Web Tokens)
- **Database**: SQLite (default), can be configured to use PostgreSQL, MySQL, etc.
- **Filtering**: `django-filter`
- **Testing**: Django Test Framework

---

## **Setup Instructions**

### **Prerequisites**
- Python 3.8 or higher
- pip (Python package manager)

---

### **1. Clone the Repository**
```bash
git clone https://github.com/ajaykumarsaini231/Task-List-Create.git
cd Task-List-Create
```

---

### **2. Create a Virtual Environment**
```bash
python -m venv myenv
```

---

### **3. Activate the Virtual Environment**
- **Windows (Command Prompt)**:
  ```bash
  myenv\Scripts\activate
  ```
- **Windows (PowerShell)**:
  ```bash
  .\myenv\Scripts\Activate.ps1
  ```
- **macOS/Linux**:
  ```bash
  source myenv/bin/activate
  ```

---

### **4. Install Dependencies**
```bash
pip install -r requirements.txt
```

---

### **5. Apply Migrations**
```bash
python manage.py migrate
```

---

### **6. Create a Superuser (Admin)**
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin user.

---

### **7. Run the Development Server**
```bash
python manage.py runserver
```
The API will be available at `http://127.0.0.1:8000/`.

---

## **API Endpoints**

### **Authentication**
- **Obtain JWT Token**: `POST /api/token/`
  - Request Body:
    ```json
    {
      "username": "your-username",
      "password": "your-password"
    }
    ```
  - Response:
    ```json
    {
      "refresh": "xxxxx",
      "access": "xxxxx"
    }
    ```

- **Refresh JWT Token**: `POST /api/token/refresh/`
  - Request Body:
    ```json
    {
      "refresh": "xxxxx"
    }
    ```

---

### **Tasks**
- **Create a Task**: `POST /api/tasks/`
  - Request Body:
    ```json
    {
      "title": "New Task",
      "description": "Task description",
      "completed": false
    }
    ```

- **List All Tasks**: `GET /api/tasks/`
  - Query Parameters:
    - `completed`: Filter by completion status (true/false).
    - `search`: Search by `title` or `description`.

- **Retrieve a Task**: `GET /api/tasks/{id}/`

- **Update a Task**: `PUT /api/tasks/{id}/`
  - Request Body:
    ```json
    {
      "title": "Updated Task",
      "description": "Updated description",
      "completed": true
    }
    ```

- **Delete a Task**: `DELETE /api/tasks/{id}/`

---

## **Testing**
To run the test suite, use the following command:
```bash
python manage.py test
```

---

## **Environment Variables**
Create a `.env` file in the root directory and add the following variables:
```plaintext
SECRET_KEY=your-secret-key
DEBUG=True
```

---

## **Contributing**
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgements**
- Django REST Framework
- Simple JWT for authentication
- Django Filter for filtering and searching

---

## **Contact**
For questions or feedback, please contact:
- **Your Name**: [Mail:](mailto:nabalkishorsaini231@gmail.com)
- **GitHub**: [Ajay Kumar Saini](https://github.com/ajaykumarsaini231)

---

This README provides all the necessary information to set up, use, and contribute to the project. Let me know if you need further customization!
