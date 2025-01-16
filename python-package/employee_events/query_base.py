# Import any dependencies needed to execute sql queries
import sqlite3
import pandas as pd

# Define a class called QueryBase
# that has no parent class
class QueryBase:

    # Create a class attribute called `name`
    # set the attribute to an empty string
    name = ""

    # Define a `names` method that receives
    # no passed arguments
    @classmethod
    def names(cls):
        # Return an empty list
        return []

    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    
    @classmethod
    def event_counts(cls, id):
        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date 
        
        if id is None:
            return pd.DataFrame()  # Return an empty DataFrame if id is None

        table_name = "employee_events"  # Use the correct table name
        query = f"""
        SELECT {table_name}.event_date, 
               SUM({table_name}.positive_events) AS positive_events,
               SUM({table_name}.negative_events) AS negative_events
        FROM {table_name}
        JOIN {cls.name} ON {table_name}.{cls.name}_id = {cls.name}.{cls.name}_id
        WHERE {table_name}.{cls.name}_id = {id}
        GROUP BY {table_name}.event_date
        ORDER BY {table_name}.event_date
        """

        connection = sqlite3.connect('python-package/employee_events/employee_events.db')
        df = pd.read_sql_query(query, connection)
        connection.close()
        return df
        

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    @classmethod
    def notes(cls, id):
        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        query = f"""
        SELECT note_date, note
        FROM notes
        WHERE employee_id = {id}
        AND team_id = {id}
        ORDER BY note_date
        """
        connection = sqlite3.connect('python-package/employee_events/employee_events.db')
        df = pd.read_sql_query(query, connection)
        connection.close()
        return df
