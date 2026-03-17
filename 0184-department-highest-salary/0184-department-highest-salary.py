import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # 1. Join the tables to get Department names
    df = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_emp', '_dept'))
    
    # 2. Find the max salary for each department
    # transform('max') keeps the index the same so we can compare row-by-row
    df['max_salary'] = df.groupby('departmentId')['salary'].transform('max')
    
    # 3. Filter rows where the employee's salary equals the department's max salary
    result = df[df['salary'] == df['max_salary']]
    
    # 4. Select and rename columns as per the requirement
    result = result[['name_dept', 'name_emp', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']
    
    return result