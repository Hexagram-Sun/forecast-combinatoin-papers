import pandas as pd

def item2md(p):
    cite = p['cite'].replace('\n', '').replace('  ', ' ')
    author = cite[:cite.find('(')]
    year = cite[cite.find('(')+1:cite.find(')')]
    name = cite[cite.find('.')+1:].strip()
    name = name[:name.find('.')+1]
    doi = cite[cite.find('DOI:'):]
    cite = cite.replace(name, f'**{name}**')\
               .replace(doi, f'[*{doi}*]({p["url"]})')\
               .replace(author, '')
    return f'{cite}\n\n  **brief: {p["brief"]}**'

df = pd.read_excel('./papers.xlsx')
with open('./readme.md', 'w', encoding='utf-8') as f:
    f.write('# forecast-combinatoin-papers\n\n')
    for i in range(len(df)):
        f.write('+ ')
        f.write(item2md(df.iloc[i]))
        f.write('\n<br>\n\n')
    

