         - name: Create index.html
           run: |
             echo '<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>AI Vinted Auto Listing</title>\n    <link rel="stylesheet" href="styles.css">\n</head>\n<body>\n    <div class="container">\n        <h1>AI Vinted Auto Listing</h1>\n        <form id="listingForm">\n            <label for="title">Title:</label>\n            <input type="text" id="title" name="title" required>\n            \n            <label for="description">Description:</label>\n            <textarea id="description" name="description" required></textarea>\n            \n            <label for="price">Price:</label>\n            <input type="number" id="price" name="price" required>\n            \n            <button type="submit">Generate Listing</button>\n        </form>\n        <div id="result"></div>\n    </div>\n    <script src="script.js"></script>\n</body>\n</html>' > index.html

         - name: Create styles.css
           run: |
             echo 'body {\n    font-family: Arial, sans-serif;\n    background-color: #f4f4f4;\n    margin: 0;\n    padding: 0;\n}\n\n.container {\n    max-width: 600px;\n    margin: 50px auto;\n    padding: 20px;\n    background-color: #fff;\n    box-shadow: 0 0 10px rgba(0,0,0,0.1);\n}\n\nh1 {\n    text-align: center;\n    color: #333;\n}\n\nform {\n    display: flex;\n    flex-direction: column;\n}\n\nlabel {\n    margin-top: 10px;\n}\n\ninput, textarea {\n    padding: 10px;\n    margin-top: 5px;\n    border: 1px solid #ccc;\n    border-radius: 4px;\n}\n\nbutton {\n    margin-top: 20px;\n    padding: 10px;\n    background-color: #28a745;\n    color: #fff;\n    border: none;\n    border-radius: 4px;\n    cursor: pointer;\n}\n\nbutton:hover {\n    background-color: #218838;\n}\n\n#result {\n    margin-top: 20px;\n    padding: 10px;\n    background-color: #e9ecef;\n    border: 1px solid #ced4da;\n    border-radius: 4px;\n}' > styles.css

         - name: Create script.js
           run: |
             echo 'document.getElementById('listingForm').addEventListener('submit', async function(event) {\n    event.preventDefault();\n    \n    const title = document.getElementById('title').value;\n    const description = document.getElementById('description').value;\n    const price = document.getElementById('price').value;\n    \n    const response = await fetch('/generate-listing', {\n        method: 'POST',\n        headers: {\n            'Content-Type': 'application/json'\n        },\n        body: JSON.stringify({ title, description, price })\n    });\n    \n    const result = await response.json();\n    document.getElementById('result').innerText = result.listing || 'Error generating listing.';\n});' > script.js

         - name: Create server.js
           run: |
             echo 'const express = require('express');\nconst bodyParser = require('body-parser');\nconst app = express();\nconst port = 3000;\n\napp.use(bodyParser.json());\napp.use(express.static('public'));\n\napp.post('/generate-listing', (req, res) => {\n    const { title, description, price } = req.body;\n    const listing = `Title: ${title}\nDescription: ${description}\nPrice: $${price}`;\n    res.json({ listing });\n});\n\napp.listen(port, () => {\n    console.log(`Server running at http://localhost:${port}`);\n});' > server.js

         - name: Create package.json
           run: |
             echo '{\n  "name": "ai-vinted-auto-listing",\n  "version": "1.0.0",\n  "description": "AI Vinted auto listing",\n  "main": "server.js",\n  "scripts": {\n    "start": "node server.js"\n  },\n  "author": "Manokai42",\n  "license": "ISC",\n  "dependencies": {\n    "body-parser": "^1.19.0",\n    "express": "^4.17.1"\n  }\n}' > package.json

         - name: Create .gitignore
           run: |
             echo 'node_modules/' > .gitignore

         - name: Create free_ai_setup.py
           run: |
             echo 'import requests\nfrom bs4 import BeautifulSoup\n\ndef scrape_vinted(query):\n    url = f"https://www.vinted.fr/catalog?search_text={query.replace(' ', '%20')}"\n    headers = {"User-Agent": "Mozilla/5.0"}\n    response = requests.get(url, headers=headers)\n    \n    if response.status_code == 200:\n        soup = BeautifulSoup(response.text, "html.parser")\n        items = soup.find_all("div", class_="feed-grid__item")\n        \n        results = []\n        for item in items[:5]:  # Limit to 5 results\n            title = item.find("span", class_="title").text if item.find("span", class_="title") else "No title"\n            price = item.find("span", class_="price").text if item.find("span", "price") else "No price"\n            link = item.find("a")["href"] if item.find("a") else "No link"\n            results.append({"title": title, "price": price, "link": link})\n        \n        return results\n    else:\n        return "Failed to scrape Vinted"\n\nprint(scrape_vinted("Nike Air Force 1"))' > free_ai_setup.py
