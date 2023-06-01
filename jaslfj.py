import requests

res_parse_list=[]
response=requests.get("https://bank.gov.ua/ua/markets/exchangerates")
response_text=response.text
response_parse=response_text.split('<td data-label="Офіційний курс">')
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("3"):
        for parse_elem_2 in parse_elem_1.split("</td>"):
            if parse_elem_2.startswith("3") and parse_elem_2[1].isdigit():
                res_parse_list.append(parse_elem_2)

dollar_curse = res_parse_list[0]

print(f'Купс долава - {dollar_curse}')