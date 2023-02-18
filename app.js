const express = require('express');
const axios = require('axios');
const cheerio = require('cheerio');

const app = express();

const PORT = process.env.port || 3000;

const website = 'https://news.sky.com';

try {
    axios(website).then((response) => {
        const data = response.data;
        const $ = cheerio.load(data);

        let content = [];

        $('.sdc=site-tile__headline', data).each(function () {
            const title = $(this).text();
            const url = $(this).find('a').attr('href');

            content.push({
                title,
                url,
            });

            app.get('/', (req, response) => {
                response.json(content);
            });
        });
    });
} catch (error) {
    console.log(error, error.message);
}

app.listen(port, () => {
    console.log('server is running on PORT:${PORT}');
})
