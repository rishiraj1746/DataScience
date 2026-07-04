print("-----Student Grade Analyzer-----")

english_grade = float(input("Enter English grade: "))
math_grade = float(input("Enter Math grade: "))
science_grade = float(input("Enter Science grade: "))
hindi_grade = float(input("Enter Hindi grade: "))
social_studies_grade = float(input("Enter Social Studies grade: "))

total_grade = english_grade + math_grade + science_grade + hindi_grade + social_studies_grade
average_grade = total_grade / 5

grade_criteria = lambda average_grade: "Excellent" if average_grade >= 90 else "Good" if average_grade >= 75 else "Average" if average_grade >= 50 else "Poor"
print(f"Total Grade: {total_grade}")
print(f"Average Grade: {average_grade}")
print(f"Higher Grade: {max(english_grade, math_grade, science_grade, hindi_grade, social_studies_grade)}")
print(f"Lower Grade: {min(english_grade, math_grade, science_grade, hindi_grade, social_studies_grade)}")
print(f"Grade Classification: {grade_criteria(average_grade)}")
