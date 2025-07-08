# 🎓 Student Grades Analyzer

A lightweight Python project to **collect**, **analyze**, and **store** student grade data.

This project is part of a personal learning series called "**Project in Nosaya**" — small yet practical projects to refresh and improve my Python and data analysis skills.

---

## 🚀 Features

- ✅ Generate an Excel template for student data entry
- 📥 Read student data from an Excel file
- 📊 Analyze grades:
  - Calculate average, maximum, and minimum grades
  - Classify students into successful and failed
- 📁 Export results to structured JSON files

---

## 🧩 Project Structure

```
student-grades-analyzer/
│
├── main.py                  # Entry point of the app
├── collect_data.py          # Handles template creation and Excel reading
├── analysis.py              # Performs statistical analysis
├── store_data.py            # Saves analysis results to JSON
├── MyData/                  # Output directory for JSON files
```

---

## 📦 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/student-grades-analyzer.git
   cd student-grades-analyzer
   ```

2. Install required libraries:
   ```bash
   pip install pandas openpyxl
   ```

---

## ▶️ How to Use

1. Run the main script:
   ```bash
   python main.py
   ```

2. Choose:
   - `(1)` to generate an Excel template
   - `(2)` to read data from an existing Excel file

3. The script will:
   - Analyze the data
   - Export 3 JSON files:
     - `analysis_to_<filename>.json`
     - `successful_students_to_<filename>.json`
     - `failed_students_to_<filename>.json`

---

## 📂 Example Output

**analysis_to_Template_2025-07-08_21-55-01.json**
```json
{
  "AVG": 74.5,
  "MAX": 90,
  "MIN": 55
}
```

**successful_students_to_...**
```json
{
  "Ahmed": 85,
  "Sara": 76
}
```

**failed_students_to_...**
```json
{
  "Omar": 55
}
```

---

## 👨‍💻 Author

**Mostafa Amin**  
Data Analyst | Data Engineer  
📫 Connect with me on [LinkedIn](https://www.linkedin.com/in/mostafa-amin-391427221/)  

---

## 📘 License

This project is licensed under the MIT License - feel free to use and modify.

---

✅ *Built as part of my personal journey to revisit Python for Data Analysis — "Project in Nosaya #1"*
