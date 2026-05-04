# Unit17 DSTAT Backend API

## Project Description
The Unit17 DSTAT Backend API is a Flask-based web application designed to facilitate data management and analysis for various statistical purposes. This API provides endpoints to interact with the database storing statistical data, running analyses, and serving statistics to clients.

## Setup Instructions
1. **Clone the Repository**  
   Clone the repository to your local machine using:  
   ```bash  
   git clone https://github.com/AnonNazi431/unit17-dstat-backend.git  
   ```  

2. **Navigate to the Directory**  
   ```bash  
   cd unit17-dstat-backend  
   ```  

3. **Set Up a Virtual Environment**  
   Create a virtual environment to isolate dependencies:  
   ```bash  
   python -m venv venv  
   ```  

4. **Activate the Virtual Environment**  
   - For Windows:  
   ```bash  
   venv\Scripts\activate  
   ```  
   - For macOS/Linux:  
   ```bash  
   source venv/bin/activate  
   ```  

5. **Install Dependencies**  
   Install the necessary packages listed in `requirements.txt`:  
   ```bash  
   pip install -r requirements.txt  
   ```  

6. **Set Up Environment Variables**  
   Create a `.env` file in the root directory of the project and add necessary configuration variables. Example:  
   ```plaintext  
   FLASK_ENV=development  
   DATABASE_URL=your_database_url  
   ```  

7. **Run the Application**  
   Start the application using Flask:  
   ```bash  
   flask run  
   ```  

## Usage Guidelines
- Once the server is running, you can access the API at `http://127.0.0.1:5000/`
- Use tools like Postman or curl to make requests to endpoints, such as:
  - `GET /api/data` to retrieve statistical data.
  - `POST /api/data` to submit new statistical data.

## Additional Notes
- Ensure that your database is correctly set up and running before attempting to access the API.
- Refer to the API documentation for detailed information on endpoints and data models.