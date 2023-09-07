import asyncio
import base64
import json
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import websockets
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from jinja2 import Template

from config import settings
from config.settings import BASE_DIR


# Create your views here
class SMTPMailer:

    def __init__(self, email: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.email = email
        self.smtp = smtplib.SMTP(host=settings.SMTP_SERVER_NAME, port=settings.SMTP_SERVER_PORT)

    def answer_access_type(self, session_b64: str, decoded: dict):
        # Run TLS protocol and logining client
        self.smtp.starttls()
        self.smtp.login(
            user=settings.APPLICATION_NAME,
            password=settings.APPLICATION_PASSWORD
        )

        # Set MIMEMultipart
        _TLS_MESSAGE = MIMEMultipart('alternative')
        _TLS_MESSAGE['From'] = settings.APPLICATION_NAME
        _TLS_MESSAGE['To'] = self.email
        _TLS_MESSAGE['Subject'] = 'Регистрация аккаунта'

        with open(os.path.abspath('') + "/confirm_email/template_email.html", 'r+', encoding='utf-8') as html_document:
            # Created HTML-Template for attach coding
            resolved_html = Template(html_document.read()).render(
                first_name=decoded['first_name'],
                last_name=decoded['last_name'],
                url=f"https://dev.aromatic.kz/confirmEmail/{session_b64}"
            )

        _TLS_PART = MIMEText(resolved_html, 'html')
        _TLS_MESSAGE.attach(_TLS_PART)

        # Answer access code to mail client.
        self.smtp.sendmail(
            settings.APPLICATION_NAME,
            self.email,
            _TLS_MESSAGE.as_string()
        )


async def make_success_align(data: dict, b64data: str):
    async with websockets.connect(f"ws://127.0.0.1:8000/auth/register/{b64data}/") as ws:
        await ws.send(json.dumps({"type": "success_connection"}))


async def accessing_email(request: HttpRequest, b64data: str) -> HttpResponse:
    data = json.loads(base64.b64decode(bytes(b64data.encode('utf-8'))))
    asyncio.create_task(make_success_align(data, b64data))
    return render(request, "success.html", data)
