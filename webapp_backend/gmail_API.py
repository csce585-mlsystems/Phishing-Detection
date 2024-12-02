from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import re

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    """Authenticate and build the Gmail API service."""
    creds = None
    try:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=8080)
        return build('gmail', 'v1', credentials=creds)
    except Exception as e:
        print(f"Error during Gmail authentication: {e}")
        return None

def fetch_links_from_emails(service, max_results=10):
    """Fetch links from the most recent emails."""
    try:
        results = service.users().messages().list(userId='me', maxResults=max_results).execute()
        messages = results.get('messages', [])
        links = []
        
        for msg in messages:
            msg_data = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
            
            # Extract the email body
            payload = msg_data.get('payload', {})
            parts = payload.get('parts', [])
            for part in parts:
                if part.get('mimeType') == 'text/plain':
                    data = part.get('body', {}).get('data', '')
                    if data:
                        # Decode the email body
                        import base64
                        decoded_data = base64.urlsafe_b64decode(data).decode('utf-8')
                        # Extract links from the decoded data
                        email_links = re.findall(r'(https?://\S+)', decoded_data)
                        links.extend(email_links)
        
        return links
    except Exception as e:
        print(f"Error fetching emails: {e}")
        return []
