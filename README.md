# Send-News-Emails-using-Python
This Python code automates the process of fetching the latest news articles related to a specified topic using the News API and sending them via email to multiple emails. We have used the requests library to make API calls and the smtplib library to handle the email sending process.

### Requirements
- Python 3.x
- Libraries: `requests`, `smtplib`, `datetime`
- A valid News API key
- Gmail account credentials

### Setup
1. **Install Required Libraries**:
   Ensure you have the required libraries installed. You can install them using pip:

   ```bash
   pip install requests
   ```
2. **Create a Credentials File**:
   Create a file named `credentials.py` in the same directory as the script with the following content:

   ```python
   email = "your_email@gmail.com"
   password = "your_password"
   api = "your_news_api_key"
   ```
   Replace `your_email@gmail.com`, `your_password`, and `your_news_api_key` with your actual Gmail credentials and News API key.
   
4. **Usage**:
   - Modify the `topic` variable in the script to change the news topic.
   - Update the `recipients` list with the email addresses you want to send the news to.
   - Run the script:

   ```bash
   python your_script_name.py
   ```
   
### Important Notes
- Ensure that "Less secure app access" is enabled in your Gmail account settings, or use an App Password if you have 2-Step Verification enabled.
- The script currently fetches articles from the last day; you can adjust the date range as needed.

### Troubleshooting
- If you encounter issues with sending emails, check your Gmail settings and ensure that the credentials are correct.
- For problems with the News API, verify that your API key is valid and that you are not exceeding the request limits.
  
### License
This project is licensed under the MIT License. Feel free to modify and distribute it as needed.
