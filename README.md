 Detailed Approach for Scraping Registered Projects from HPRERA

In this project, I aimed to scrape details of registered real estate projects from the HPRERA Public Dashboard. The details sought included the promoter's name, PAN number, permanent address, and GSTIN number, all displayed in a popup upon clicking the RERA number link. Here's a comprehensive step-by-step breakdown of the approach I took to tackle the situation:


REQUIREMENTS

SELENIUM  "pip install selenium"

WEB-DRIVER MANAGER "pip install webdriver-manager"


 1. Understanding the Target Website and Data Structure

- Website Analysis: I started by examining the [HPRERA Public Dashboard](https://hprera.nic.in/PublicDashboard) to identify how the project information is structured. I found that the details are displayed in a modal popup when the RERA number links are clicked.

- HTML Structure Inspection: I used the browser's Developer Tools to inspect the HTML structure, focusing on the elements containing project details and the close button within the popup.

 2. Setting Up the Web Scraper

- Tool Selection: I chose Selenium for web scraping because it can handle JavaScript and interact with dynamic content like modals.

- Environment Setup: I installed the required dependencies (`selenium` and the appropriate WebDriver, `chromedriver` for Chrome).

 3. Script Development

Initial Steps:
- Opening the Website: The WebDriver was configured to open the target URL.
- Locating Elements: I identified the RERA number links using a CSS selector or XPath based on attributes in the `onclick` attribute.

Detailed Data Extraction:
- Clicking RERA Links: For each RERA link, I used Selenium's `ActionChains` to click and trigger the modal popup.
- Extracting Information: Once the popup was open, I extracted the relevant details using XPath, targeting table rows (`<td>`) containing specific texts like 'Name', 'PAN No.', etc.

Closing the Popup:
- Identifying the Close Button: The close button was identified using the CSS selector `[data-dismiss='modal']`, targeting a button with the `data-dismiss` attribute.

 
4. Handling Issues and Challenges

Handling Exceptions:
- Timeouts: I set a timeout for finding elements, using `WebDriverWait` to wait until the elements were present in the DOM.
- NoSuchElementException: Exception handling was implemented to log any issues where elements were not found, which helped in diagnosing problems with specific projects.

Specific Issues Encountered:
- Inconsistent Data Structure: One project had an issue where the expected elements were not found. This could be due to missing data or a different HTML structure for that particular project.

 5. Testing and Validation

Iterative Testing:
- I ran the script iteratively, making adjustments to the selectors and handling based on the feedback from each run.

Data Validation:
- I compared the scraped data against the visible data on the website to ensure accuracy.

 6. Finalization and Optimization

Code Optimization:
- I reduced unnecessary wait times and ensured all edge cases were handled.
- Implemented a clean shutdown procedure for the WebDriver.

Documentation and Comments:
- The script was well-documented, explaining each step and the purpose of various parts of the code.

 7. Summary of the Output

Successful Extraction:
- Details were successfully extracted for 6 out of the 6 projects.


Handling Dynamic Content:
- The approach demonstrated the ability to handle dynamically loaded content using Selenium's capabilities effectively.





 Issues Faced

1. TimeoutException:
   - Cause: Occurred when Selenium couldn't find the specified elements within the given time frame.
   - Resolution: Increased the wait time and verified the CSS selectors to ensure they matched the elements.

2. NoSuchElementException:
   - Cause: Raised when expected elements (such as project details in the popup) were not found.
   - Resolution: Implemented error handling and used `WebDriverWait` to wait for elements to become present in the DOM.

3. Inconsistent Data Structure:
   - Cause: Some projects had different HTML structures or missing data fields in their popups.
   - Resolution: Manually inspected the problematic projects and adjusted the script to account for possible variations.

4. Closing the Popup:
   - Issue: Initially, the close button could not be identified due to incorrect or ambiguous selectors.
   - Resolution: Used a specific selector (`button[data-dismiss='modal']`) based on the button's attributes.

5. Dynamic Content Loading:
   - Cause: Delays in loading content led to elements being accessed before they were fully loaded.
   - Resolution: Added `time.sleep` and `WebDriverWait` to ensure elements were fully loaded before interacting with them.

6. Differentiating Project Data:
   - Issue: Ensuring the correct data was extracted and matched the visible data for validation.
   - Resolution: Validated the data by cross-checking it against the visible data on the website.

7. Handling Edge Cases:
   - Issue: Some popups had missing elements, causing the script to fail or skip projects.
   - Resolution: Added checks for element presence and handled missing data gracefully.

These issues were systematically addressed to create a robust and reliable web scraping script.




Output:



![Screenshot (5)](https://github.com/user-attachments/assets/a68372ee-7aca-4d70-89bf-21536ceda3ae)



