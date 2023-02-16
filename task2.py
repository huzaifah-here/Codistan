import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="codistan"
)

cursor = conn.cursor()
#QUERY
"""
SELECT c.NAME
FROM COMPANY c
INNER JOIN EMPLOYEE e ON c.ID = e.COMPANY_ID
INNER JOIN SALARY s ON e.ID = s.EMPLOYEE_ID
GROUP BY c.NAME
HAVING AVG(s.SALARY) >= 40000;
"""