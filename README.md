# AV Glasses

Link to [Deployed Site](your link here)

Blue light glasses is new modern world is best feature for adults and kids, who spend lot of time infornt of any screans.
- Blue light glasses protects from eyes getting dry.
- Blue light glasses protects from eye irritation.
- Blue light glasses helps your sleep.
- Blue light glasses protects from fatigueness.

[AV Glasses](live site here) is an online blue light protection glasses shop, which offers not only the glasses, but also case for their new or existing pair of galasses and wipes to clean a lence.

## Table of Contents

1. UX
    - Project Goals
    - User Stories
    - Design

2. Features
    - Existing Features
        - Landing Page
        - Product Page
        - Cart Page
        - Checkout Page
        - Profiles Page
        - Admin Product Managment
        - Django allauth features
    - Features Left to Implement
    - Design

3. Information Architecture
    - Database Choice

4. Technologies Used
    - Languages
    - Libraries and Packages
    - Databases

5. Testing

6. Deployment
    - Heroku Deployment with AWS
    - Local Deployment

7. Credits

8. Disclaimer

# UX
## Project Goals
### Target Audience
- People who are looking to buy blue light protection glasses
- People who have problems spending longer time infront of a screan
- People who want to give present for the close people , so they are protected

### Visitor / User Goals
- Purchase products in a smooth and secure way
- Get informed with the products before buying by product reviews / product information
- Get all accessories at same place

### Business Goals (Site Owner's Goals)
- Provide customers with a secure and safe ecommerce shop
- Establish the shop's brand
- Expand their business effectively
- Make profit from selling products


## User Stories

- Viewing and Navigation

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User/ Shopper | access the website from any devices | Use the website anytime and anywhere |
| Shopper | Easily see what products are offered | Find the product I want to buy |  
| Shopper | All the products are in categories and are accesible from nav bar| Don't need to spend a lot of time finding what is in need |
| Shopper | Have a shopping cart icon on nav bar | Always check the current order and checkout when I want |

<br/>

- Registration, User Accounts and User Community

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily register for an account | Have a personal account where I can edit my information |  
| Site User | View my order history | Ease see which products you have bought and when |
| Site User | Receive an email confirmation after registering | Verify that my account registration was successful |
| Site Owner | Let the site users log in when they leave reviews/subscribed for news letters | Track who left reviews/ subscribed for news letters |

<br/>

- Online shopping

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Shopper | Search a product with keywords | Find the most appropriate products |
| Shopper | View individual product pages that have prices, descriptions, etc | Get detailed information about the product before purchasing |
| Shopper | Filter by a specific category | Easily find products in a specific category |
| Shopper/Site Owner | Leave/View product reviews with scores | Understand which products are popular with other customers |
| Site Owner | Easily add a new product | Make sure the online site has the latest catalogue |
| Site Owner | Easily update or delete product | Make sure the online site has the latest catalogue |

<br/>

- Cart, Purchasing and Checkout

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Shopper | Easily select the quantity of a product after adding a product to a cart | Ensure I don't accidentally select the wrong product and the quantity | 
| Shopper | The delivery information is prefilled if logged in | Smoothly proceed with my purchase | 
| Shopper | Automatically suggest to log in if I did not log in | Smoothly proceed with my purchase | 

<br/>


## Design

### Brand Identity
- Vision: Spend how long you need time infront of the screan without wories about healt. Eather you work, study or just surfing in internet.
- Mission: Provide safe time infront any screan as in 21st century even in a car is multiple screans, so we care about your health. And at AV Glasses you can purchas with one click online without the hassle of going to a physical shops.
- Values: 1.Happiness - Improve your happiness with brand new stylish pair of glasses, 2.Elegance - All our frames are best sellers, 3.Health - Nothing is more important than your health.

### Color Scheme
Color scheme is important as this is one of the first things site visitors notice when visiting the site. I chose mainly green for the site's primary color, because green color is warm and welcoming and the website look professional and high-end. 

### Typography
For AV Glasses shop I choose `'Julius Sans One' that falls under sans-serif.

- Icons: FontAwesome is used for the main icon library accross the site.


# Features

## Existing Features
This website is composed of 6 applications: `home`, `cart`, `checkout`, `products`, `profiles`, `newsletters`.

## Landing Page
Landing Page is designed as a single page website to provide site visitors with enough information so they can understand what the business is about of this site. This page has minimal amount of information to let the site visitors take next actions. The page compose of `Navbar`, `Why you need glasses?`, `google maps API` section. Shop now buttons have little animation on hover to atract custumers.

### Navbar
Navbar is fixed at the top of pages across the site, so that the site visitors easily navigate the whole site.  Navbar contains  `Brand Logo`, `Search Box`, `Site Menu`, `My Account dropdown` and `Cart icon`.
- Search box: This search box function allows the visitors to search the products on online shop with keywords. The keywords are searched over `name` and `descriotion` field of Product Model. This function uses "OR" condition not "AND" when searching the keywords.
- Site Menu & My Account dropdown: My Account dropdown is included to toggle menu for smaller screen.
- Cart icon: Shows the sum of total amount thru out the site if you have something in your shoping cart.


### 5 benefits?
`why you need a blue light glasses` section explains why you need glasses if yoy spend time at the screans like any other modern people at 21st century..

`Google maps API?` section shows where is our physical office.

### Footer
The footer section consists of two lines: 1: its automated copyright date, 2: explaining that this web site at the moment is for learning purpues only no actual selling or buying.


## Product Page
### Online Shop Page
By clicking 'Shop Now' on the site button, you can go to the online shop page.
- Product Filter: There is a filter section at the right side of the online shop page, and you can filter products by 'price', 'rating', 'name.'


- Result Number: It's shown on the right side top corner. Customers can see how many results were found in total at a glance.

- Products: The products are displayed so custumer can see `Product picture`, `Product Name`, `Price`, `Category`, `Product rating`. If the user is logged in as a superuser, Edit / Delete option is also shown on each product.

### Product Detail Page
- Product Image
- Product Name
- Product Price
- Product Category
- Product Rating
- Product Description
- Option to choose quantity
- See revievs/add revievs
- Add product to cart or continue shoping without adding choosen product
- If loged in as superuser option to edit or delete product


## Cart Page
- Cart page shows the products added to the cart. Customers are able to change the quantity or remove the products in this cart page. To see total and delivery price. They have option by clicking buttons to to chechout page or to continue shopping.

## Checkout Page
### Checkout Page
- On the checkout page, customers are asked to fill in delivery details. Also they can see pictures of their selected products and to see grand total. At the moment, this shop does not collect user's billing information within the User Profile model or Order model.(However, the billing data is recorded in Stripe from the billing information added by the customer.) 

### Checkout Success Page
- A thank you message will be displayed after the checkout process as well as the table that holds the order details.
- `Also see other products` button is placed after table the page, and if the customer has been logged into their account, `Back to Profile` will be shown. And at the bottom will be option to sign up for newsletters providing your email.

## Profiles Page
`My Profile` page is available for authenticated users and will be shown in the `My Account` Dropdown menu at the navbar which appears when you log into your account.
### My Profile Page
- In Profile Page, authenticated users can 1. edit `Delivery Information`, 2. see `Order History` and 3. subscribe for newsletters.

## Admin Product Managment
Only authenticated superusers can access the admin page (1.products/add/, 2. products/edit/, 3. products/delete/). If non-logged in users try to access the url directly, it will redirect to the sign in page. If a non-superuser tries to access the url, an error message pops up which says that only a superuser can access this page.

## Django-allauth features
- Sign Up: The users will be asked to fill out `E-mail`, `User Name` and `Password` to create an account. When the sign up form is submitted, a verification email will be sent to the user's email address to complete the sign up process.
- Log In: Users will be asked to input `User Name` or `Email`, and `Password` to login. If the user successfully logged in, a success message will pop up and redirect to the landing page.
- Log out: Log out page is accessible from the site menu. After the user successfully signed out button on the sign out page, a success message will appear and redirect to the landing page.

## Features Left to Implement
There are some of features left to implement in the future which I could not add to the project this time due to time constraints. These features are great to be added for a more complete online shop service which would lead to higher customer satisfaction.
### 1. Limit the user who can leave product review
At the moment, all the authenticated users can leave reviews to any products if they are logged in. It should be limited to those who actually purchased the product for the validity of the reviews.
### 2. Social Account Login
This function allows users to sign up / log into their account of the site, using an existing third party account such as Google and Facebook. This is beneficial to users and the site owners. For users, it's hassle free for remembering a password for the site and it gives the users a smooth registration process. For the site owners, there are many benefits gained by social login - such as increasing user sign ups, reducing bounce rate and gaining a user's social account details which is beneficial for marketing purpose.
### 3. Order Tracking System
To keep the customers informed with the status of their purchase, it would be nice if the site provides the order status such as shipment information in order history and email notifications.

### Form Validation
- Django Form Validation

# Information Architecture
## Database choice
- Development phase
**SQLight** database was used for the development which is installed with Django. 

- Deployment phase
**PostgreSQL** was used on deployment stage, which is provided as add-on by Heroku application.

- User model is provided as a default by Django's authentication system

- Fixtures for categories and products made by me in jason files.

### Product App
`Product` app gives users best expierience in searching for the right product in categories or keywords. And alos filtering products for better user expierence.

### Order App
`Order` model collects the delivery information, stripe_pid and order information. All the fields except `user_profile` field have `null=false`. The reason why `user_profile` does not have `null=false` is that guest customers (not authenticated users) can also purchase products and complete the checkout process without creating an account. `Order` model is connected to `OrderLineItem` model which collects information of purchased products.

### Profile App
`Profile` is used for my profile page where the authenticated users can see their delivery details and their order history.

### Newsletter App
`Newsletter` app gives users option to sign up for newsleter and for bussines to make custumers to want to come back.

## Languages
- HTML, CSS, JavaScript, Python

## Libraries and Packages
- [Django](https://www.djangoproject.com/)
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [Bootstrap (v4.4.1)](https://www.bootstrapcdn.com/)
- [JQuery](https://jquery.com/)
- [Veu.js](https://vuejs.org/)
- [Font Awesome](https://fontawesome.com/)
- [Animate.css](https://animate.style/)
- [Stripe](https://stripe.com/ie)
- [Google Fonts](https://fonts.google.com/)

## Databases
- [SQlite3](https://www.sqlite.org/index.html)- database used for development.
- [PostgreSQL](https://www.postgresql.org/) - database used for production.






# Testing
1. Manual Testing
    - Responsiveness
    - Landing Page
    - Navbar
    - Footer
    - Online shoping
    - Cart
    - Checkout and Checkout Success Page
    - SignIn / SignOut
    - Profile and Order History
    - Admin Product Management
    - All Links
    - All Buttons
    - Stripe Payments 
    
2. Automated Testing
    - LightHouse on Google DevTool
3. Checked web site thru html validator https://validator.w3.org/ , checked CSS code https://jigsaw.w3.org/css-validator/ , checked my JS code http://beautifytools.com/javascript-validator.php
4. Tried my website in diferent web browsers all worked very good. Checked all screan sizes on my smart tv, on my laptom, on my tablet and on my phone all works.
5. On console in dev tools shows no errors.






# Deployment







# Credits
## Content & Code
- I constantly read [Django](https://docs.djangoproject.com/en/3.1/), [Stripe](https://stripe.com/docs) and [Python](https://docs.python.org/3/) documenation and tutorial throughout the development.
- For the hover efects credit to stack overflow.
- For the review model and newsletter app credit to https://www.youtube.com/channel/UCfVoYvY8BfTDeF63JQmQJvg
- This project was developed refering to the Boutique Ado Django mini-project from Code Institute course materials. The codes are customized and modified to fit the purpose of this milestone project.

### Images & Media
- All the icons in this website were provided by [Font Awesome](https://fontawesome.com/).
- The credits for the images used in this site are from (https://ebay.com/)

### Acknowledgements
- Code Institute Slack Community that gave me a light when I was stuck in my coding.
- Got insparation for readme file from other code institute students.

### Disclaimer
This website is created for educational purpose only.


