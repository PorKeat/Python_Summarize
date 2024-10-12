import requests
from transformers import pipeline
from bs4 import BeautifulSoup
from db_connection import connect

class Model:
    def __init__(self):
        self.connection = connect()  
        self.summarizer = pipeline("summarization")
        self.max_length = 150
        self.max_input_length = 1024

    def save_summary(self, url, summary):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute('INSERT INTO summaries (url, summary) VALUES (%s, %s)', (url, summary))
                self.connection.commit()
                return True
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False

    def fetch_and_summarize(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch the URL: {e}")

        soup = BeautifulSoup(response.content, 'html.parser')
        content = ' '.join(p.get_text() for p in soup.find_all('p'))

        if len(content) > self.max_input_length:
            content = content[:self.max_input_length]

        summary = self.summarizer(content, max_length=self.max_length, min_length=30, do_sample=False)
        return ' '.join(sentence['summary_text'] for sentence in summary)

    def close_connection(self):
        self.connection.close()
