# Import your libraries
import pandas as pd

df = pd.DataFrame(db_employee)
df1 = pd.DataFrame(db_dept)
df_merged = pd.merge(df, df1, left_on='department_id', right_on='id')
df_merged.drop('id_y', axis=1)
df_filtered = df_merged[df_merged['department'].isin(['marketing', 'engineering'])]
# calculate the difference between the highest salaries found in the marketing and engineering departments
marketing_max_salary = df_filtered.loc[df_filtered['department'] == 'marketing', 'salary'].max()
engineering_max_salary = df_filtered.loc[df_filtered['department'] == 'engineering', 'salary'].max()
salary_difference = abs(marketing_max_salary - engineering_max_salary)
