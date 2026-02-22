from google import genai
import os

client = genai.Client(api_key='AIzaSyDGemJYnV9PmHL8Az0zmRWv3YQCwbsyQAA')

for m in client.models.list():
    print(m.name)