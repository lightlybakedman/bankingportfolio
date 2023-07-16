import requests

APININJAS_KEY = "Ixa7F06gKTZDS8Euz9ZL6g==5po9rtQkIdC0cuXA"


def get_central_bank_rate(country: str):
    if country.lower() == "germany":
        return 3.5  # API could not find the interest rate for Germany or EU

    api_url = "https://api.api-ninjas.com/v1/interestrate"
    params = {"country": country}
    response = requests.get(
        api_url, headers={"X-Api-Key": APININJAS_KEY}, params=params
    )
    if response.status_code == requests.codes.ok:
        # print(response.json())
        # print(response.json()["central_bank_rates"][0]["rate_pct"])
        return response.json()["central_bank_rates"][0]["rate_pct"]
    else:
        print("Error:", response.status_code, response.text)
