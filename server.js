const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(express.static('public'));

app.post('/generate-listing', (req, res) => {
    const { title, description, price } = req.body;
    const listing = `Title: ${title}\nDescription: ${description}\nPrice: $${price}`;
    res.json({ listing });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});