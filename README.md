# susGPT
A toy program showing how you can use ChatGPT to see if a URL is suspicious.

You probably shouldn't run this in production.

## Usage
```
export OPENAI_API_KEY=$your_api_key
python3 susgpt $url_to_check
```
## Example
In:
```python
python3 susgpt login-bofa-account-center.dc480.io
```
Out:
```
Checking to see if login-bofa-account-center.dc480.io is suspicious...
login-bofa-account-center.dc480.io is suspicious: True, reason: Yes, this URL is suspicious. 

The URL appears to be linking to a Bank of America account login page, but the domain name dc480.io seems unrelated to Bank of America. Additionally, the use of "login" and "account center" in the URL can be a tactic used by phishers to trick individuals into entering their login credentials. It is always important to verify the legitimacy of a URL before entering any personal information.
```

## Requirements
Python 3.7+ (because of data classes)
openai package

```
python3 pip install -r requirements.txt
```