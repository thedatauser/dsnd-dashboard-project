# Import the QueryBase class
from .query_base import QueryBase

# Import dependencies needed for sql execution
# from the `sql_execution` module
import sqlite3
import pandas as pd

# Define a subclass of QueryBase
# called Employee
class Employee(QueryBase):

    # Set the class attribute `name`
    # to the string "employee"
    name = "employee"

    # Define a method called `names`
    # that receives no arguments
    # This method should return a list of tuples
    # from an sql execution
    @classmethod
    def names(cls):
        # Query 3
        # Write an SQL query
        # that selects two columns 
        # 1. The employee's full name
        # 2. The employee's id
        # This query should return the data
        # for all employees in the database
        query = """
        SELECT first_name || ' ' || last_name AS full_name, employee_id
        FROM employee
        """
        connection = sqlite3.connect('python-package/employee_events/employee_events.db')
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result

    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution
    @classmethod
    def username(cls, id):
        # Query 4
        # Write an SQL query
        # that selects an employee's full name
        # Use f-string formatting and a WHERE filter
        # to only return the full name of the employee
        # with an id equal to the id argument
        query = f"""
        SELECT first_name || ' ' || last_name AS full_name
        FROM employee
        WHERE employee_id = {id}
        """
        connection = sqlite3.connect('python-package/employee_events/employee_events.db')
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result

    # Below is a method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returned containing the execution of
    # the sql query
    @classmethod
    def model_data(cls, id):
        query = f"""
        SELECT SUM(positive_events) positive_events,
               SUM(negative_events) negative_events
        FROM {cls.name}
        JOIN employee_events
        USING(employee_id)
        WHERE {cls.name}.employee_id = {id}
        """
        connection = sqlite3.connect('python-package/employee_events/employee_events.db')
        df = pd.read_sql_query(query, connection)
        connection.close()

        return df
