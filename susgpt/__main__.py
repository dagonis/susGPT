import argparse
import os

from core import ChatGPT, SuspiciousURL

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str, help='The URL to check.')
    args = parser.parse_args()
    print(f"Checking to see if {args.url} is suspicious...")
    api_key = os.getenv('OPENAI_API_KEY')
    chat_gpt_client = ChatGPT(api_key)
    result = chat_gpt_client.check_url(args.url)
    print(result)

if __name__ == '__main__':
    main()