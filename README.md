# Django Auctions Website

This project is a Django-based web application for creating and managing online auctions. Users can list items for auction, place bids, and monitor auctions they're interested in.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Django Auctions Website was created during the process of learning web development using the Django framework. It provides users with the ability to create item listings for auctions, place bids on items, and monitor their ongoing auctions.

## Features

### Key Features

- **Category Filter**: Organize listings by categories.
- **Active Listings Page**: View all active listings.
- **Bidding & Listing Pages**: Detailed information on listings and bidding options.
- **Watchlist**: Add listings to your watchlist for easy access.
- **Place Bids**: Participate in auctions by placing bids.
- **User Profiles**: Manage your account and listings.
- **Close Auctions**: Close auctions when they're completed.
- **Notifications**: Receive notifications for bid updates.
- **Activate Auctions**: Activate auctions for items you want to sell.
- **Create Listings**: Add new listings to the platform.
- **Exploring Models**: Learn about Django's data models and relationships.

## Demo

For a quick visual overview of the key features, watch our 5-minute demo video [here](https://youtu.be/xgyz1m0VApU).
You can test the website live at [https://youssefel0.pythonanywhere.com/](https://youssefel0.pythonanywhere.com/). Please note that this is a testing environment, and the website may not be available after a certain date.

## Installation

To run this project locally, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/youssefel01/Auctions.git

2. Navigate to the project directory:

   ```bash
   cd Auctions

3. Create a virtual environment to isolate your project's dependencies:

   ```bash
   python -m venv venv

4. Activate the virtual environment (on Windows):

   ```bash
   venv\Scripts\activate

   (On macOS and Linux):

   source venv/bin/activate

5. Apply database migrations:

   ```bash
   python manage.py migrate

6. Create a superuser account to access the admin panel:

   ```bash
   python manage.py createsuperuser

7. Start the development server:

   ```bash
   python manage.py runserver

9. Open your web browser and go to http://127.0.0.1:8000 to access the application.

You have now successfully set up the Django Auctions Website locally. Enjoy exploring and customizing your auction platform!

## Usage

- To create a new listing, log in and click on "Create Listing" in the navigation bar. Fill in the required details, and your item will be up for auction.
- To place a bid on an item, navigate to the item's detail page and use the bidding form.
- You can also add items to your watchlist by clicking the "Add to Watchlist" button on an item's detail page.
- Monitor your active listings and bidding activity in your user profile.

## Technologies

- Python
- Django
- SQLite
- HTML/CSS
- Bootstrap

## Contributing

Contributions are welcome! If you have any suggestions or find issues, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

   
