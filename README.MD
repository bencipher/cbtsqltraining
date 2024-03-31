## Getting Started

This is the readme file for running the script to make mass insert into the db! Here's how to set up your development environment and run the code.

**Prerequisites:**

* A computer with a working internet connection.
* Run the script in the script.sql in your sql server scripts (copy/paste)

**Software Installations:**

1. **Python:**
   Download and install Python from the official website: [https://www.python.org/](https://www.python.org/). Choose the appropriate installer for your operating system (Windows, macOS, or Linux). Follow the on-screen instructions to complete the installation.

**Setting Up the Project Environment:**

1. **Open your project folder:**

   - **Using File Explorer (Windows) or Finder (Mac):**

     i. Locate the folder containing the project files on your computer.
     ii. Right-click on the folder.
     iii. Select the option that opens the folder in your terminal/command prompt (e.g., "Open in Terminal" on macOS or "Open in Command Prompt" or "Open in PowerShell" on Windows). This will launch your terminal and automatically set the current working directory to the project folder.

2. **Create and Activate Virtual Environment:**

   **a. Windows:**

     i. In the terminal window (launched from Step 1), you're already in the project directory. Use the following command to create a virtual environment named `my_env` (replace with your preferred name):

       ```bash
       python -m venv my_env
       ```

     ii. Activate the virtual environment:

       ```bash
       my_env\Scripts\activate
       ```

   **b. macOS/Linux:**

     i. In the terminal window (launched from Step 1), you're already in the project directory. Use the following command to create a virtual environment named `my_env` (replace with your preferred name):

       ```bash
       python -m venv my_env
       ```

     ii. Activate the virtual environment:

       ```bash
       source my_env/bin/activate
       ```

   **Note:** The prompt will change to indicate you're now working within the virtual environment (e.g., `(my_env)user@machine:~$`).

3. **Install Required Dependencies:**

   - The project dependencies are listed in a file named `requirements.txt`. Install them using:

     ```bash
     pip install -r requirements.txt
     ```

**Setup Database server to connect with Python:**

1. **ODBC Adapter (if connecting to SQL Server):**
   - Download and install the ODBC adapter for Python from Microsoft: [https://go.microsoft.com/fwlink/?linkid=2249006](https://go.microsoft.com/fwlink/?linkid=2249006)

2. **Create SQL Server Credentials (if applicable):**

   - Follow the appropriate steps for your SQL Server setup to create a username and password for authentication (https://www.sqlservercentral.com/articles/setting-up-management-studio-for-remote-sql-server).

3. **Create `.env`:**

   - Create a file named `.env` in the project directory (**important: exclude this file from version control!**).
   - Add the following lines, replacing placeholders with your database information:

     ```
     #SQL_SERVER=MSSQLSERVER
     SQL_SERVER=YOUR_SERVER_NAME
     SQL_DATABASE=YOUR_DATABASE_NAME
     SQL_USERNAME=YOUR_USERNAME
     SQL_PASSWORD=YOUR_PASSWORD
     ```

**Running the Code:**

1. **Ensure your virtual environment is activated (refer to step 2a or 2b for activation commands).**

2. **Execute the main Python file:**

   ```bash
   python main.py
   ```

**Additional Notes:**

- If you encounter any issues during the setup process, feel free to consult online resources or ask for help during class.
- Remember to replace placeholders with your actual information when setting up database credentials (if applicable).
- To deactivate the virtual environment, simply type `deactivate` in your terminal.