import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "navaneetkandaloju@gmail.com"  # Replace with your Gmail
EMAIL_PASSWORD = "sbbf bjgj gzti zcbz"  # Use your Gmail App Password

# File paths
file_path = "contacts.xlsx"  # Excel file containing email list
resume_path = "resume.pdf"  # Change to your actual resume file name

# Load the Excel file
df = pd.read_excel(file_path)

# Ensure "Status" column exists
if "Status" not in df.columns:
    df["Status"] = ""

# Function to send email
def send_email(name, email, title, company):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = email
    msg["Subject"] = "Application for Data Analyst / Data Science Roles"

    # Email body
    body = f"""
    Dear {name},

    I hope you are doing well. I am reaching out to express my interest in entry-level opportunities across the IT domain at {company}. With my background in Python, SQL, data analysis, machine learning and networking, I am confident that my skills align well with your team’s needs.

    Thank you for considering my application. I have attached my resume and would be grateful for any opportunity or referral that aligns with my profile.

    Looking forward to your response.

    Best regards,  
    Navaneeta Chary Kandaloju  
    7386584090  
    www.linkedin.com/in/navaneetkandaloju  
    """
    
    msg.attach(MIMEText(body, "plain"))

    # Attach resume
    if os.path.exists(resume_path):
        with open(resume_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(resume_path)}",
        )
        msg.attach(part)
    else:
        print("⚠ Resume file not found!")

    # Send email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, email, msg.as_string())
        server.quit()
        
        print(f"✅ Email sent successfully to {name} ({email})")
        return True
    except Exception as e:
        print(f"❌ Failed to send email to {name} ({email}): {e}")
        return False

# Send emails only to those without a "Sent" status
for index, row in df.iterrows():
    if row["Status"] != "Sent":  # Only send if not already sent
        success = send_email(row["Name"], row["Email"], row["Title"], row["Company"])
        if success:
            df.at[index, "Status"] = "Sent"  # Mark as sent
        df.to_excel(file_path, index=False)  # Save progress after each email
