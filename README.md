
# Insurance Management System

This is a Insurance Management System based on 3 interface to be used by the bank admin , agents and well as the various policy holders of the bank.

The project includes the User Interface built using Streamlit and the database that uses MySql.


## Deployment

To host this project

1.Clone it

```bash
  https://github.com/Kesu-1407/Insurance-Management-System.git
```
2.Go to project directory

```bash
  cd Insurance-Management-System
```
3.Create a mysql database named 'insurance' and give your password to your user and hosting address in the usermy.py file

```bash
con=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='insurance'
)
```

## Dependencies

1.Streamlit

```bash
pip install streamlit
```
2.Python 3.8
3.mysql-connector-python
```bash
pip install mysql-connector-python
```
4.Start the server
```bash
streamlit run gotit.py
```
## Entity Diagram

![App Screenshot](https://github.com/Kesu-1407/Insurance-Management-System/blob/main/entity%20diagram.jpg?raw=true)


## Schema Diagram

![App Screenshot](https://github.com/Kesu-1407/Insurance-Management-System/blob/main/schema.jpg?raw=true)
## Authors

- [@Kesu-1407](https://www.github.com/Kesu-1407)

