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

image_element = soup.select_one('#landingImage')
image = image_element.attrs.get('src')

description_element = soup.select_one('#feature-bullets')
description = description_element.text

review_element = soup.select('div.review')
scraped_rivews = []

for review in review_element:
    r_author_element = review.select_one('span.a-profile-name')
    r_author = r_author_element.text if r_author_element else None

    r_rating_element = review.select_one('i.review-rating')
    r_rating = r_rating_element.text.replace('out of 5 stars', '') if r_rating_element else None

    r_title_element = review.select_one('a.review_title')
    r_title_span_element = r_title_element.select_one("span:not([class])") if r_title_element else None
    r_title = r_title_span_element.text if r_title_span_element else None

    r_content_element = review.select_one('span.review-text')
    r_content = r_content_element.text if r_content_element else None

    r_date_element = review.select_one('span.review-date')
    r_date = r_date_element.text if r_date_element else None

    r_verified_element = review.select_one('span.a-size-mini')
    r_verified = r_verified_element.text if r_verified_element else None

    r = {
        "author" : r_author,
        "rating" : r_rating,
        "title" : r_title,
        "content" : r_content,
        "date" : r_date,
        "verified" : r_verified
        }
    
    scraped_rivews.append(r)
