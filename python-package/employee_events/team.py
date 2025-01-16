# Import the QueryBase class
from .query_base import QueryBase

# Import dependencies needed for sql execution
# from the `sql_execution` module
import sqlite3
import pandas as pd

# Create a subclass of QueryBase
# called  `Team`
# Create a subclass of QueryBase
# called `Team`
class Team(QueryBase):

    # Set the class attribute `name`
    # to the string "team"
    name = "team"

    # Define a `names` method
    # that receives no arguments
    # This method should return
    # a list of tuples from an sql execution
    @classmethod
    def names(cls):
        # Query 5
        # Write an SQL query that selects
        # the team_name and team_id columns
        # from the team table for all teams
        # in the database
        query = """
        SELECT team_name, team_id
        FROM team
        """
        connection = sqlite3.connect('python-package/employee_events/employee_events.db')
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result

    # Define a `username` method
    # that receives an ID argument
    # This method should return
    # a list of tuples from an sql execution
    @classmethod
    def username(cls, id):
        # Query 6
        # Write an SQL query
        # that selects the team_name column
        # Use f-string formatting and a WHERE filter
        # to only return the team name related to
        # the ID argument
        query = f"""
        SELECT team_name
        FROM team
        WHERE team_id = {id}
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
        SELECT positive_events, negative_events FROM (
                SELECT employee_id,
                       SUM(positive_events) positive_events,
                       SUM(negative_events) negative_events
                FROM {cls.name}
                JOIN employee_events
                USING(team_id)
                WHERE {cls.name}.team_id = {id}
                GROUP BY employee_id
               )
        """
        connection = sqlite3.connect('python-package/employee_events/employee_events.db')
        df = pd.read_sql_query(query, connection)
        connection.close()
        
        return df
