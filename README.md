# SQLify | End-to-End Text-to-SQL LLM App

SQLify is an end-to-end text-to-SQL application developed using Large Language Models (LLMs) for natural language understanding and SQL query generation. This app streamlines the process of querying SQL databases by transforming natural language queries into SQL queries for efficient database retrieval.

## Key Features

- Utilizes Large Language Models (LLMs) for natural language understanding.
- Transforms natural language queries into SQL queries.
- Deploys on Google Gemini Pro for efficient querying of SQL databases.
- Streamlines the process of querying SQL databases.


## Deployment

SQLify can be deployed on Google Gemini Pro for efficient querying of SQL databases. Please refer to the deployment documentation for detailed instructions.
SQLify is deployed on Streamlit for interactive use. You can access the deployed app [here](https://sqlify.onrender.com/).

Here's how you can format the examples to include the expected output:

---

## Examples

### Example 1: Counting Records

**Question:** How many entries of records are present?

**SQL Command:**
```sql
SELECT COUNT(*) FROM STUDENT;
```

**Expected Output:**
```
| COUNT(*) |
|----------|
| 10       |
```

### Example 2: Filtering by Class

**Question:** Tell me all the students studying in Data Science class?

**SQL Command:**
```sql
SELECT * FROM STUDENT WHERE CLASS="Data Science";
```

**Expected Output:**
```
| ID | NAME    | CLASS         | MARKS |
|----|---------|---------------|-------|
| 1  | Ashish  | Data Science  | 85    |
| 3  | Salik   | Data Science  | 78    |
| 5  | Anurag  | Data Science  | 92    |
| ...| ...     | ...           | ...   |
```

---

In this format, each example includes the SQL query and the expected output in a tabular format, making it clear what the query should return.

## Installation

To install SQLify, simply clone the repository and install the required dependencies:

```bash
git clone https://github.com/ashish23112rai/SQLify.git
cd SQLify
pip install -r requirements.txt