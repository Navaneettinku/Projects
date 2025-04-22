import smtplib
import pandas as pd

# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "navaneetkandaloju@gmail.com"  # Replace with your Gmail
EMAIL_PASSWORD = "sbbf bjgj gzti zcbz"  # Use the App Password here

# Load the Excel file
file_path = "contacts.xlsx"  # Replace with the actual file path
df = pd.read_excel(file_path)

# Lists to store valid and invalid emails
valid_emails = []
invalid_emails = []

# Function to check email sending capability
def check_email(row):
    email = row["Email"]
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)  # Checking authentication
        server.mail(EMAIL_SENDER)
        code, message = server.rcpt(email)  # Checking recipient email validity
        server.quit()

        if code == 250:
            print(f"✅ Email can be sent to {email}")
            valid_emails.append(row)
        else:
            print(f"⚠️ Possible issue with {email}: {message.decode()}")
            invalid_emails.append(row)

    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed! Check your email and App Password.")
        exit()  # Stop execution if authentication fails
    except smtplib.SMTPRecipientsRefused:
        print(f"❌ Email cannot be sent to {email}. Recipient refused.")
        invalid_emails.append(row)
    except Exception as e:
        print(f"❌ Error with {email}: {e}")
        invalid_emails.append(row)

# Check all emails in the Excel file
for index, row in df.iterrows():
    check_email(row)

# Convert valid & invalid emails to DataFrames
valid_df = pd.DataFrame(valid_emails)
invalid_df = pd.DataFrame(invalid_emails)

# Save results to separate files
valid_df.to_excel("can_send.xlsx", index=False)
invalid_df.to_excel("cannot_send.xlsx", index=False)

print("\n✅ Email check complete! Results saved to 'can_send.xlsx' and 'cannot_send.xlsx'.")
