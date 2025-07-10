# Excel Reporter 📊

This is a simple Python project that reads employee data from an Excel file (`data.xlsx`), analyzes salary and department information, and writes a summary report to a new worksheet named `Summary`.

## Features

- ✅ Reads Excel data using `openpyxl`
- ✅ Calculates:
  - Total salary
  - Average salary
  - Number of employees per department
- ✅ Writes a clear summary to a new worksheet

## Example Input (Sheet: `Лист1`)

| Name    | Department | Salary |
|---------|------------|--------|
| Alice   | IT         | 5000   |
| Bob     | HR         | 4000   |
| Charlie | IT         | 5500   |
| Diana   | Sales      | 4500   |
| Eva     | HR         | 4200   |

## Output (`Summary` Sheet)

| Metric            | Value |
|-------------------|--------|
| Total Salary      | 23200  |
| Average Salary    | 4640.0 |
| HR Employees      | 2      |
| IT Employees      | 2      |
| Sales Employees   | 1      |

## Technologies Used

- Python 3.13+
- openpyxl

## How to Run

1. Make sure you have `openpyxl` installed:

   ```bash
   pip install openpyxl

2. Place your data.xlsx file in the project directory.

3. Run the script:
    python excel_reporter.py

---