import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch({headless: true,
    args: [
      'no-sandbox',
      'disable-setuid-sandbox',
    ]});
  const page = await browser.newPage();
  
  const cookies = [{
    'name': 'flag',
    'value': 'SNYK{41e9641bd54a62f25b30f04ac7309a49ed989cf8644eb43861f0aeb6f3666bfe}',
    'domain': '127.0.0.1:5000'
  }];
  
  await page.setCookie(...cookies);

  const url = process.argv[2];

  await page.goto(url);

  // Wait for page to load
  const allResultsSelector = '.container';
  await page.waitForSelector(allResultsSelector);

  await browser.close();
})();