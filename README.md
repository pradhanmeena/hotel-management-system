## Title of the project:
### Hotel Management System using python

## Description

The **Hotel Management System** is a software application designed to help hotel managers efficiently manage day-to-day hotel operations. This system allows the manager to **add and maintain room details**, **register new customer information**, and **assign specific rooms** on particular floors.

The application provides features for check-in and check-out, bill generation, and customer data management. Customer details can be easily fetched and transferred from one window or module to another, ensuring smooth workflow and reduced manual effort.

Overall, this system improves operational efficiency, reduces errors, and simplifies hotel management through a centralized and user-friendly interface.
## Installation
1. **Install Python and MySQL** : Ensure that you have installed mysql and python in your system
2. **Changing database details**: when you have download the files of this software you will find a file `database_details.py`.
                 In this file you need to change these details according to your database that you have created on your system:
<br><br>`file: database_details.py`
   ```
   class DatabaseDetails:
      def __init__(self):
          self.host='localhost'               #change it according your host name 
          self.user='root'                    #change it according your host username
          self.password='admin123'            #change these  passwords according yours 
          self.database='raw'                 #change the name of database 
   ```

3. **table**: In the next step you needto to open and run the file 'table.py' that help to create all required tables.

4. **Change Images paths**: In the file `login_page.py`, update the paths of the image files to ensure the application displays the interface correctly and maintains a better visual appearance.You need to modify the image paths at the following `line numbers: 27, 111, 255, and 260`.
## Usage
Follow the steps below to use this software:
1. Open the project folder and run the file login_page.py.
2. The login window will appear on the screen.
3. Since you do not have an existing account, click on the Create New Account button.
4. Fill in the required details and create your account successfully.
5. After creating the account, return to the login page and log in using your credentials.
6. Once logged in, the main user interface (UI) of the project will be displayed.
## Managing Hotel Data:
1. Click on the Details button.
2. Enter all room details along with their respective floor numbers.
3. Save the data and go back to the main menu.
4. Click on the Customer button.
5. Enter the customer’s personal details such as name, mobile number, and other required information.
6. Save the customer details.
7. Click on the Room button.
8. Enter the customer’s mobile number.
9. Click on Fetch Data to automatically retrieve customer details.
10. Fill in the remaining room allocation details and confirm the assignment.

## Contact
- **Email:** pradhanmeena7778@gmail.com  
- **Phone:** +91 6376244866


