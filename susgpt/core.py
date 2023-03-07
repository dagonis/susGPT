from dataclasses import dataclass

import openai

@dataclass
class SuspiciousURL:
    url: str
    suspicious: bool
    raw_response: openai.openai_object.OpenAIObject

    def __post_init__(self):
        self.reason = self.raw_response.choices[0].message.content.strip()

    def __str__(self):
        return f"{self.url} is suspicious: {self.suspicious}, reason: {self.reason}"

@dataclass
class ChatGPT:
    key: str

    def check_url(self, url: str) -> SuspiciousURL:
        """Check if a URL is suspicious using GPT-3.

        Args:
            url (str): The URL to check.

        Returns:
            SuspiciousURL: The result of the check
        """
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                                                  messages=[{"role": "user", "content": f"Is this url suspicious, please start your response with a yes or no then provide your reasons. {url}"}])
        output_text = completion.choices[0].message.content.strip()
        return SuspiciousURL(url, output_text.lower().startswith('yes'), completion)
