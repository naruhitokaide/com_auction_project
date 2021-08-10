# Computer Auction Website

A CRUD website for auctioning computers. View at https://iab207-assessment-3.herokuapp.com/

![techprowl2](https://user-images.githubusercontent.com/47819009/128790287-2839db50-b595-4f68-a7c2-9ccd8752d4bf.png)


## Technologies Used
- HTML
- CSS
- Bootstrap
- Python
- Flask
  - Flask Templates
  - Flask WTForms
  - Flask SQLAlchemy
  - Flask Login

## Features
- Landing page with recently posted items
- Items on landing page contain the following
  - The number of bids on an item
  - The status of a listing - closed or open for bid
  - The highest bid
- Users can check details of closed bids
- Users are able to select item listing and view the details of it.
- If the auction is not yet closed, the user can bit on the item by providing an amount greater than the current highest bid. 
- Users can add an item to their watchlist (if the listing is closed then this is not possible)
- Users can view items in their watchlist with details of item
- Users can register
- Users can login
- Users can list items once they are registered
- Users can logout
- Users can search by keyword
- Users can post reviews for listings
- Responsive layout 
- Page not found error is displayed for internal server errors and navigates user back to home page
- Form validation
- Data is dynamically created and stored in SQLite database
