import requests

url = "https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/data-engineer"

payload = {
    "name": "Ebraim Carvalho",
    "mail": "ebraimfcfilhoe@hotmail.com",
    "github_url": "https://github.com/ebraimcarvalho/tweet_data"
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Resposta:", response.text)
