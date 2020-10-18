#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[90]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.  
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
#school_data.head(5)
#student_data.head(5)
school_data_complete.head(5)


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Calculate the percentage of students who passed math **and** reading (% Overall Passing)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[91]:


total_school = school_data["school_name"].count()
total_school


# In[92]:


total_student = student_data["student_name"].count()
total_student


# In[93]:


total_budget = school_data["budget"].sum()
total_budget


# In[94]:


average_math_score= student_data["math_score"].mean()
average_math_score


# In[95]:


average_reading_score= student_data["reading_score"].mean()
average_reading_score


# In[118]:


student_pass_math = student_data.loc[student_data["math_score"]>=70, ["Student ID", "student_name", "gender", "grade", "school_name", "reading_score", "math_score"]]
student_pass_math.head(5)


# In[136]:


student_pass_reading = student_data.loc[student_data["reading_score"]>=70, 
                    ["Student ID", "student_name", "gender", "grade", "school_name", "reading_score", "math_score"]]
student_pass_reading.head(5)


# In[ ]:





# In[142]:


student_pass_math_reading = student_data.loc[(student_data["reading_score"]>=70) & (student_data["math_score"]>=70), 
                    ["Student ID", "student_name", "gender", "grade", "school_name", "reading_score", "math_score"]]
student_pass_math_reading.head(5)


# In[143]:


#find number of student that pass math (>=70)
total_student_pass_math = student_pass_math["school_name"].count()
total_student_pass_math


# In[144]:


#find number of student that pass reading (>=70)
total_student_pass_reading = student_pass_reading["school_name"].count()
total_student_pass_reading


# In[146]:


#find number of student that pass math and reading (>=70)
total_student_pass_math_and_reading = student_pass_math_and_reading["school_name"].count()
total_student_pass_math_and_reading


# In[102]:


#Percentage of student that pass math (>=70)
percent_passing_math = total_student_pass_math / total_student *100
percent_passing_math


# In[103]:


#find number of student that pass reading (>=70)
percent_passing_reading = total_student_pass_reading / total_student *100
percent_passing_reading


# In[148]:


#Percentage of student that pass math and reading (>=70)
percent_passing_math_reading = total_student_pass_math_and_reading / total_student *100
percent_passing_math_reading


# In[149]:


#Create a dataframe to hold the above results

summary_df = pd.DataFrame({"Total number of school": [total_school],
                            "Total number of student": [total_student],
                            "Total budget": [total_budget],
                            "Average math score": [average_math_score],
                            "Average reading score": [average_reading_score],
                            "passing math score (%)": [percent_passing_math] ,
                            "passing math score (%)": [percent_passing_reading] ,
                            "passed math and reading (%)": [percent_passing_math_reading] })
summary_df


# In[150]:


#Optional: give the displayed data cleaner formatting
summary_better_format_df = pd.DataFrame(
                            {"Tasks":["Total number of school","Total number of student",
                                       "Total budget","Average math score","Average reading score",
                                       "passing math score (%)","passing math score (%)", 
                                       "passed math and reading (%)"],
                             "Value":[[total_school],[total_student],[total_budget],[average_math_score],
                                      [average_reading_score],[percent_passing_math],
                                     [percent_passing_reading],[percent_passing_math_reading]]
                            })
summary_better_format_df


# ## School Summary

# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * % Overall Passing (The percentage of students that passed math **and** reading.)
#   
# * Create a dataframe to hold the above results

# In[151]:


school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete.head()


# In[155]:


grouped_school_data_complete=school_data_complete.groupby(["school_name"])
grouped_school_data_complete.head(5)


# In[157]:


#Total students by school and school name
total_students_by_school = school_data_complete.groupby('school_name')['student_name'].count()
total_students_by_school


# In[158]:


#Total school budget by school
total_budget_by_school = school_data_complete.groupby('school_name')['budget'].mean()
total_budget_by_school


# In[160]:


#budget per student
per_student_budget = total_budget_by_school/total_students_by_school
per_student_budget


# In[161]:


#Sum of math scores per school / # of students
total_math_score_per_school=school_data_complete.groupby('school_name')['math_score'].sum()
total_math_score_per_school


# In[162]:


#average of math scores per school
average_math_score_per_school = total_math_score_per_school /total_students_by_school
average_math_score_per_school


# In[164]:


#Sum of reading scores per school / # of students
total_reading_score_per_school=school_data_complete.groupby('school_name')['reading_score'].sum()
total_reading_score_per_school


# In[165]:


#average of math scores per school
average_reading_score_per_school = total_reading_score_per_school /total_students_by_school
average_reading_score_per_school


# In[171]:


#number of student pass math per school, math scores>=70
student_pass_math_per_school = student_pass_math.groupby('school_name')['math_score'].count()
student_pass_math_per_school


# In[174]:


#percent pass math per school
percent_pass_math = student_pass_math_per_school/total_students_by_school *100
percent_pass_math


# In[251]:


#number of student pass reading per school, reading score>=70
student_pass_reading_per_school = student_pass_reading.groupby('school_name')['reading_score'].count()
student_pass_reading_per_school


# In[252]:


#percent pass reading
percent_pass_reading = student_pass_reading_per_school/total_students_by_school *100
percent_pass_reading


# In[253]:


#number of student pass both math and reading per school, reading score>=70
student_pass_math_and_reading_per_school = student_pass_math_reading.groupby('school_name')['math_score'].count()
student_pass_math_and_reading_per_school


# In[239]:


#percent pass overall
percent_pass_math_and_reading = student_pass_math_and_reading_per_school/total_students_by_school *100
percent_pass_math_and_reading


# In[226]:


#grouped school mane by type
school_type=school_data_complete.groupby('school_name')["type"].first()
school_type


# In[227]:


#Create a data frame to hold the above values
school_summary = pd.DataFrame({'School Type': school_type,
                                 'Total Students': total_students_by_school,
                                 "Total School Budget":total_budget_by_school,
                                'Per Student Budget': per_student_budget,
                                'Average Math Score': average_math_score_per_school,
                                 'Average Reading Score': average_reading_score_per_school,
                                 '% Passing Math': percent_pass_math,
                                 '% Passing reading': percent_pass_reading,
                                 '% Overall passing': percent_pass_math_and_reading
                                })
school_summary


# ## Top Performing Schools (By % Overall Passing)

# * Sort and display the top five performing schools by % overall passing.

# In[228]:


#To sort from highest to lowest, ascending=False must be passed in
top_performance_school = school_summary.sort_values("% Overall passing", ascending=False)
top_performance_school.head(5)


# In[ ]:





# ## Bottom Performing Schools (By % Overall Passing)

# * Sort and display the five worst-performing schools by % overall passing.

# In[229]:


#To sort from highest to lowest, ascending=False must be passed in
top_performance_school = school_summary.sort_values("% Overall passing", ascending=True)
top_performance_school.head(5)


# In[ ]:





# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[230]:


school_data_complete.head(5)


# In[231]:


#Math score by grade
math_score_by_grade = school_data_complete.pivot_table(index="school_name",columns="grade", values="math_score")
math_score_by_grade


# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[233]:


#reading score by grade
reading_score_by_grade = school_data_complete.pivot_table(index="school_name",columns="grade", values="reading_score")
reading_score_by_grade


# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[234]:


print(school_summary["Per Student Budget"].max())
print(school_summary["Per Student Budget"].min())


# In[235]:


# Create bins in which to place values based upon TED Talk views
bins = [ 0, 585, 630, 645, 675]

# Create labels for these bins
group_labels = ["<$584", "$585 - 629", "$630 - 644", "$645 - 675"]


# In[236]:


#Slice the data and place it into bins
pd.cut(school_summary["Per Student Budget"], bins, labels=group_labels).head()


# In[237]:


# Place the data series into a new column inside of the DataFrame
school_summary["Spending Ranges (Per Student)"] = pd.cut(school_summary["Per Student Budget"], bins, labels=group_labels)
school_summary.head()


# In[221]:


#score by school spending
score_by_school_spending=school_summary.groupby("Spending Ranges (Per Student)")
print(score_by_school_spending["Average Math Score"].count())
score_by_school_spending[["Average Math Score", "Average Reading Score", "% Passing Math", "% Passing reading", "% Overall passing"]].mean()


# In[ ]:





# In[ ]:





# In[18]:





# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[241]:


print(school_summary["Total Students"].max())
print(school_summary["Total Students"].min())


# In[242]:


# Create bins in which to place values based upon school size
bins = [ 0, 1000, 2000, 5000]

# Create labels for these bins
group_labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[243]:


#Slice the data and place it into bins
pd.cut(school_summary["Total Students"], bins, labels=group_labels).head()


# In[244]:


# Place the data series into a new column inside of the DataFrame
school_summary["School Size"] = pd.cut(school_summary["Total Students"], bins, labels=group_labels)
school_summary.head()


# In[246]:


#score by school size
score_by_school_size = school_summary.groupby("School Size")
print(score_by_school_size["Average Math Score"].count())
score_by_school_size[["Average Math Score", "Average Reading Score", "% Passing Math", "% Passing reading", "% Overall passing"]].mean()


# In[ ]:





# In[ ]:





# ## Scores by School Type

# * Perform the same operations as above, based on school type

# In[249]:


school_summary.head()


# In[248]:


#print(school_summary["type"].max())
#print(school_summary["type"].min())


# In[ ]:


# Create bins in which to place values based upon school size
#bins = [ 0, 1000, 2000, 5000]

# Create labels for these bins
#group_labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[ ]:





# In[24]:





# In[ ]:




