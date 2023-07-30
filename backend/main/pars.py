import json
from bs4 import BeautifulSoup
import requests
import pymorphy2

headers = {'User-Agent':
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
           }


def get_word(word: str):
    morph = pymorphy2.MorphAnalyzer(lang='ru')
    sklon_word = morph.parse(word)[0]
    nomn_word = sklon_word.inflect({'nomn'})
    sklon = [
        nomn_word.word,
        nomn_word.inflect({'gent'}).word,
        nomn_word.inflect({'datv'}).word,
        nomn_word.inflect({'accs'}).word,
        nomn_word.inflect({'ablt'}).word,
        nomn_word.inflect({'loct'}).word,
    ]

    word_value = pars_word_value(word)
    definition = word_value['definition']
    examples = word_value['examples']
    associations = word_value['associations']
    synonyms = word_value['synonyms']
    image_link = pars_image(word)

    return {
        'word': word,
        'definition': definition,
        'associations': associations,
        'synonyms': synonyms,
        'examples': examples,
        'image_link': image_link
    }


def pars_image(word):
    res = requests.get(
        'https://xn--80ajubim2a.xn--p1acf/%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/' + word,
        headers=headers
    )
    soup = BeautifulSoup(res.text, 'lxml')
    res = soup.find_all('script')
    data = json.loads(res[14].next)

    image = data['@graph'][3]['image'][0]
    return {"image": image}


def pars_word_value(word):
    res = requests.get(
        'https://kartaslov.ru/%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%B1%D1%8B%D0%B2%D0%B0%D0%B5%D1%82/' + word,
        headers=headers
    )
    soup = BeautifulSoup(res.text, 'lxml')
    site_data = soup.find_all('div', class_='v3-cross-block')

    associations = site_data[1].find_all('div', class_='v3-cross-block-list-item')
    synonyms = site_data[2].find_all('div', class_='v3-cross-block-list-item')

    word_value = site_data[5].find('li').find('p', class_="v3-map-dict-item").text

    examples = site_data[3].find('ul').find_all('li')
    result_examples = []
    for i in range(len(examples) - 1):
        temp = examples[i].text.replace('  ', '').split('\n')
        result_examples.append(list(filter(None, temp))[0])

    associations_result = [associations[i].find("a").text for i in range(len(associations))]
    synonyms_result = [synonyms[i].find("a").text for i in range(len(synonyms)  )]

    return {
        "definition": word_value,
        "examples": result_examples,
        "associations": associations_result,
        "synonyms": synonyms_result,
    }