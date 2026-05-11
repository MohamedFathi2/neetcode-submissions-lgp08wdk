CREATE TABLE students(
    id INTEGER UNIQUE NOT NULL,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
);


-- Do not modify below this line --
SELECT column_name, is_nullable, column_default, 
  CASE WHEN EXISTS (
    SELECT 1 FROM information_schema.constraint_column_usage cu
    JOIN information_schema.table_constraints tc ON tc.constraint_name = cu.constraint_name
    WHERE cu.column_name = columns.column_name AND cu.table_name = 'students' AND tc.constraint_type = 'UNIQUE'
  ) THEN 'YES' ELSE 'NO' END AS is_unique
FROM information_schema.columns
WHERE table_name = 'students';