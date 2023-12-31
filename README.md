# ALX / Holberton Planning Tracker

![Planning Tracker logo](https://github.com/Matsadura/ALX-Planning/assets/132571698/06165dc5-063c-4bcf-ae22-2aa7b95b9c18)



## Overview

The ALX / Holberton Planning Tracker is a Python script designed to track and manage ongoing projects, providing timely alerts through Discord. It fetches project details and sends notifications to keep users informed about upcoming deadlines.


Note : For Holberton students replace ``https://intranet.alxswe.com`` with ``https://intranet.hbtn.io``


![demo](https://github.com/Matsadura/ALX_Holberton-Planning-Tracker/assets/132571698/c4b49ffd-b8cd-42a4-8396-f374ae720ed3)


## Features

- **Real-time Tracking:** The script fetches the latest project information from the ALX / Holberton planning system.
- **Discord Notifications:** Stay updated with timely alerts on your Discord server, ensuring you never miss a project deadline.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Matsadura/ALX_Holberton-Planning-Tracker
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up login and Discord Webhook:

   - Add your login credentials to email and password variables.
   
   - Obtain a Discord Webhook URL and replace `YOUR_DISCORD_WEBHOOK_URL` in the script with the actual URL.
  
Note: You can get the webhook following this short demo

![hook](https://github.com/Matsadura/ALX-Planning/assets/132571698/9d5d4ddc-ece3-42c4-ae6e-5052e3764756)

4. Run the script:

   ```bash
   python3 main.py
   ```
Note: The most ideal usage situation is to setup a Cron-Job to fetch the data daily at a set time.

## Usage

1. Execute the script to fetch and analyze the current planning data.

2. Receive Discord notifications with project details, deadlines, and resource information.


## Author

Zidane ZAOUI

Feel free to contribute, report issues, or suggest enhancements. Happy tracking!

---

*This project is not affiliated with ALX or Holberton. It is an independent tool created for personal use.*


## More Projects

[Monty Language Interpreter](https://github.com/Matsadura/monty)

[Simple Shell](https://github.com/Matsadura/simple_shell)

[Printf Implementation](https://github.com/Matsadura/printf)

[ALX Time Saver](https://github.com/Matsadura/ALX_Time_Saver)
