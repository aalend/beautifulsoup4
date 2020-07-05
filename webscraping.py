from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="X-UA-Compatible" content="ie=edge" />
        <title>My Webpage</title>
    </head>
    <body>
        <div id="section-1">
            <h3 data-hello="hi">Hello</h3>
            <img src="https://source.unsplash.com/200x200/?nature,water" />
            <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto
                culpa cumque velit aperiam officia molestias maiores qui
                officiis incidunt. Omnis vitae eveniet reprehenderit excepturi
                officiis quod, eum natus voluptatem nihil fugit necessitatibus
                dolorum quae accusamus aliquid enim fuga dicta beatae!
            </p>
        </div>
        <div id="section-2">
            <ul class="items">
                <li class="item"><a href="#">Item 1</a></li>
                <li class="item"><a href="#">Item 2</a></li>
                <li class="item"><a href="#">Item 3</a></li>
                <li class="item"><a href="#">Item 4</a></li>
                <li class="item"><a href="#">Item 5</a></li>
            </ul>
        </div>
    </body>
</html>
"""

# first param is what to scrape
# second param is parser library
soup = BeautifulSoup(html_doc, 'html.parser')

# select direct
print(soup.head.title)

# find()
el = soup.find('div')
el = soup.find(id='section-1')
el = soup.find(class_='items')
el = soup.find(attrs={"data-hello": "hi"})  # if not exist returns Null

# find_all() returns list of items
el = soup.find_all('div')
el = soup.find_all('div')[1]  # select index 1 in list

# select()
el = soup.select('#section-1')  # returns lists

# get_text()
el = soup.find(class_='item').get_text()

# loop through .item and print text
for item in soup.select('.item'):
    print(item.get_text())


# Navigation
el = soup.body.contents[1].contents[1]

# find_next_sibling()
el = soup.body.contents[1].contents[1].find_next_sibling()

# find_previous_sibling()
el = soup.find(id='section-2').find_previous_sibling()

# find_parent()
el = soup.find(class_='item').find_parent()

# find_next_sibling('p')
el = soup.find('h3').find_next_sibling('p')

print(el)
