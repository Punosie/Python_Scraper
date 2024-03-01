import requests
from bs4 import BeautifulSoup


url = 'https://www.amazon.in/Apple-iPhone-15-Pro-256/dp/B0CHWZ86W2/ref=sr_1_24?dib=eyJ2IjoiMSJ9.eFa-TvbcC_zjCq_5PD2KO7esruSMHK5ZeG6Ar_e-Gy4Yxc61NR9Qh-S3XchUD4-CQX7RjkUi7bAC9xW5xCjNL_n5qrtd5ubhTrfcEFg9nqoPg6fOer0Zyi5GngWB9LPTqlV17crHXyBomqH7jbHW5Bb03xPR1Pcr6OqVGBF1owxgzNu9T9T9ZwjCDE3t3Z8X4Y6xD-VvJJXIzpP4fibuBmBg9ECaUIdJmy5j8iFUr3o-NyYdPF2dy-J9039eqAeNQedmnKccV5WU82cvBjRS1yCPasHLo8vemN9lCJk7TFs.sJQ-7a8d62wszhzNDD3d7y5cUiW2gkRcP_aQICoKHbI&dib_tag=se&qid=1709321570&refinements=p_6%3AA14CZOWI0VEHLG%7CA1P3OPO356Q9ZB%7CA2HIN95H5BP4BL%2Cp_89%3AApple&s=electronics&sr=1-24'

custom_headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                  'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8' }

response = requests.get(url, headers=custom_headers)
soup = BeautifulSoup(response.text, 'lxml')

title_element = soup.select_one('#productTitle')
title = title_element.text.strip()

rating_element = soup.select_one('#acrPopover')
rating_text = rating_element.attrs.get('title')
rating = rating_text.replace('out of 5 stars', '')

price_element = soup.select_one('span.a-price').select_one('span.a-price-whole')
price = price_element.text.strip()

print(price)
