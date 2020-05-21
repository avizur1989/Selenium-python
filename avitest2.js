const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  //fiil the form
  await page.goto('http://contractorsinsurancereview.com/ExampleForm/');
  await page.type('#name', 'Avi Zur'); 
  await page.type('#email', 'a@a.com');
  await page.type('#phone', '0503355992');
  await page.type('#company', 'Jones');
  
  //select from the dropdown list:
  await page.select('#employees', '51-500');
  // first screenshot before clicking the button
  await page.screenshot({path: 'example343488.png'});
  
 //clicking the button, writing to the console and take another screenshot
  await Promise.all([
      await page.click('body > div > div.row > div.large-5.medium-5.columns > div > form > p:nth-child(8) > button')  
    ]);
  page.once('load', () => console.log('Page loaded!'));
  

  await page.screenshot({path: 'eeegff343434fge.png'});


  await browser.close();
})();