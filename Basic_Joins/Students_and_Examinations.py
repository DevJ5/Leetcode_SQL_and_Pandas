import pandas as pd


def students_and_examinations(
    students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame
) -> pd.DataFrame:
    df = students.merge(subjects, how="cross")
    examinations.rename(columns={"subject_name": "subject_name2"}, inplace=True)
    df_result = df.merge(
        examinations,
        how="left",
        left_on=["student_id", "subject_name"],
        right_on=["student_id", "subject_name2"],
    )

    return (
        df_result.groupby(["student_id", "student_name", "subject_name"], dropna=False)[
            "subject_name2"
        ]
        .count()
        .reset_index(name="attended_exams")
    )


# SQL Variant
"""
SELECT students.student_id,
       students.student_name,
       subjects.subject_name,
       Count(examinations.student_id) AS attended_exams
FROM   students
       CROSS JOIN subjects
       LEFT JOIN examinations
              ON students.student_id = examinations.student_id
                 AND subjects.subject_name = examinations.subject_name
GROUP  BY students.student_id,
          subjects.subject_name
ORDER  BY students.student_id,
          subjects.subject_name  
"""
