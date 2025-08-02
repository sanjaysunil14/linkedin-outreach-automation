# 🔗 LinkedIn Profile Outreach Automation

Automates sending personalized connection requests on LinkedIn by reading profile URLs from an Excel sheet and using Selenium for browser automation.

---

## 📌 Project Objective

To streamline professional outreach and networking by automating the process of sending personalized connection requests to LinkedIn profiles.

This project was created as part of the **Scoreazy Python Developer Internship Assignment**.

---

## 🚀 Features

- ✅ Reads LinkedIn profile URLs from an Excel file  
- ✅ Logs in to LinkedIn using user credentials  
- ✅ Sends connection requests with a custom message  
- ✅ Tracks success/failure for each profile  
- ✅ Saves the result in a new Excel sheet  

---

## 📂 Input

- `linkedin_profiles1.xlsx` with a column `LinkedIn_URL`  
- LinkedIn username and password (entered securely at runtime)  
- Custom message under 200 characters  

---

## 🧠 Tech Stack

- **Python 3**  
- **Selenium** for browser automation  
- **Pandas** for Excel handling  
- **Chrome WebDriver**

---

## 📈 Workflow

1. User runs the script  
2. Script logs in to LinkedIn  
3. Reads profile URLs from Excel  
4. Visits each profile, clicks "Connect"  
5. Adds a custom message and sends the request  
6. Logs success or failure in a new column (`status`)  
7. Saves results to `connection_result.xlsx`

---

## 🧪 Sample Output

| LinkedIn_URL                         | Status                      |
|-------------------------------------|-----------------------------|
| https://linkedin.com/in/example1    | Request send                |
| https://linkedin.com/in/example2    | Failed or Already Connected |

---

## ✉️ Custom Message Sent

