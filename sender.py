import subprocess

def send_email():
    smtp_server = "smtp.yourmailserver.com"
    smtp_port = 587  # Gunakan 465 untuk SSL langsung
    username = "admin@domain.tls"
    password = "yourpassword"
    
    email_content = """From: Febriyanto Nugroho <admin@domain.tls>
To: Febriyanto Nugroho <febri@pantero.id>
Subject: Meeting Reminder
Date: Sun, 02 Mar 2025 12:00:00 +0000
Message-ID: <1234567890@febri.click>
MIME-Version: 1.0
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: 7bit

Hello,

Izin numpang test email.

Best regards,
Febriyanto Nugroho
"""
    
    command = f"""
    openssl s_client -connect {smtp_server}:{smtp_port} -starttls smtp <<EOF
EHLO {smtp_server}
AUTH LOGIN
{username.encode().hex()}
{password.encode().hex()}
MAIL FROM:<{username}>
RCPT TO:<febri@pantero.id>
DATA
{email_content}
.
QUIT
EOF
    """
    
    process = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(process.stdout)
    print(process.stderr)

send_email()
