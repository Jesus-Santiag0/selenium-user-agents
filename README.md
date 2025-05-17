# selenium-user-agents

This code, created using Python, automatically selects a user agent for each request made by Selenium. It is primarily designed for web scraping.

## Details

> user-agents.py

Contains the algorithm to extract the most recent and common user agents found on the web for desktop devices. They are extracted from [useragents.me](https://useragents.me/).

> user-agents.txt

Contains the list of user agents extracted with **user-agents.py**. It's recommended to update if a significant amount of time has passed since this file was uploaded to the repository (**_just an updated user agent will suffice_**).

> selenium-user-agents.py

Contains the algorithm that reads and randomizes values ​​from the **user-agents.txt** file, in order to use them in the Selenium header for web queries.

_This example uses Firefox as the browser and Amazon.com links to consult_
