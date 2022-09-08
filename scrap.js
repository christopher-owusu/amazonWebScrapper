
// Packages 
const axios = require('axios');   // Used to grab the url
const cheerio = require('cheerio');   // Used to grab info from site
require("dotenv").config();    // Gets info from our .env file
const accountSid = process.env.TWILIO_ACCOUNT_SID;
const authToken = process.env.TWILIO_AUTH_TOKEN;
const client = require('twilio')(accountSid, authToken);

const url = 'https://www.amazon.com/dp/B09MW17JQY/ref=twister_B09Z16XW2J?_encoding=UTF8&psc=1';

// Things that we want to extract
const product = { name:"", price: "", link:"" };

// Set interval
const handle = setInterval(scrape, 20000);


async function scrape() {
    // Fetch data from url
    const { data } = await axios.get(url);

    // Load html page
    const $ = cheerio.load(data);
    const item = $("div#dp-container");   // Gets the container that holds the product info

    // Extract needed data 
    product.name = $(item).find('h1 span#productTitle').text();   // Gets the text product title
    product.link = url;

    const price = $(item).find('span .a-price-whole').first().text().replace(/[,.]/g, "");
    // Changes price to integer from string
    const priceNum = parseInt(price);
    product.price = priceNum;
    console.log(product);

    // Send SMS Notification
    if (priceNum < 800) {
        client.messages.create({
            body: `The price of ${product.name} went below ${price}. Find out more at ${product.link}`,
            from: "+12763789303",
            to: '0241991189'
        }).then((message) => {
            console.log(message);
            clearInterval(handle);
        });
        
    }

}

scrape(); 