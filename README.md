# Logistics Management System 

The LMS will facilitate order processing, shipment tracking, inventory management, and reporting for logistics companies. It will support both web and mobile platforms.


## Features 
- User [**Authentication**](#user-authentication) and role management 
- [**Order**](#order-management) processing and tracking 
- [**Inventory**](#inventory-management) management 
- [**Route**](#route-optimzation) optimizaiton 
- Reporting and **analytics**

## LMS UML & Screen Ketches 

Our [UML](UML%20&%20Sketches/lms_uml.PNG) class diagrams will help us create our *Django Models* and we've also included an **initial** [screen ketch](UML%20&%20Sketches/lms_sketch.png) that maps out our *Django Templates* 

## LMS Flowchart & User Story 

Our [Flowchart](flowchart_&_usecase/TekBasic_-_Flowchart.jpg) and [User Story](flowchart_&_usecase/tek_basic_LMS_spreadsheet.png) helps us map out the workflow of our logistic management system 
[User story](https://docs.google.com/spreadsheets/d/1TRWM4X3m8ce1DH5L9vNB4vYQrEc0RXMGlLlSn-PWqgg/edit?usp=sharing)

## Update Logs 
**03/11**
- [x] Updated Home Page (Dashboard)
- [x] Select Different Perferred Card?
  - Visa | American Express | Mastercard

**03/11**
- [x] Multiple Order Items 
  -  List Group to display forms
  -  Sends get request for Product + Quantity (We make manually save the OrderItem)
  -  (Commit is False)--> Django Sessions to store and talk between views 
  -  Upon payment, we'll add to our DB 
- [x] On Order creation successul send email 
  - Order Must have an email field (we could assume its the user but since this is a management system, we might be making this order for someone) 
- [x] Integrate Stripe Payment 
  - We only wan to do **Charge** which uses their server-side instead of a client-based (making product on their page and redirecting our users to it)
    - Stripe Charge API [Reference](https://stackoverflow.com/questions/55092240/how-to-integrate-stripe-payment-with-existing-django-form-and-only-save-form-on)
    - We're looking at [PaymentIntent](https://docs.stripe.com/payments/quickstart?lang=python) + Stackoverflow [response](https://stackoverflow.com/questions/74100476/integrate-stripe-payment-flow-into-django)
    - Copied over the views + checkout.html BUT checkout.js 
      - Change the fetch() url to use our views, success url to our views + Remove **hard coded items**
  - Testing [cards](https://docs.stripe.com/testing)
  - In summary, we pulled changed checkout.html + checkout.js to fit our script. Created a path to handle payment (generate token for PayementIntent)
    - We're using **server-side** instead of client
- [x] Order Summary
  - Include what they're buying + Testing Cards

**03/10**
- [x] View Tracking information (Specific Shipment) 
- [x] Included maps for routes + eta
- [x] We may need to work on changing the **Status** level the Drivers could do that
- [x] Instead of generate a route automatically (upong save which is bad because address might not always be good) Drivers could do that
  - We generate a route automatially but we also let drivers update the map 
- [x] Added DateTimeField to our Route models to keep track of updates

**03/08**
- [x] Fix redirect Product Update Delete
- [x] Pre-save logic checks state transition: if restock goes from `False` to `True` we email  
- [x] Ensure Users are notified if the inventory goes low via email 
  - Since notifications aren't our full focus let's just add a "Remove All Notifcations" Button 
- [x] Practice ORS + Folium on Jupyter Notebook first (similarize syntax, api key etc)
  - ORS --> Build routes in Long Lat with Profile as Driving Car
  - Folium --> Map out our route in Lat Long 
    - Starting Point will be at Tekbasic
  - Geopy --> Grab Long/Lat Information from Address 
- [x] When confident, build our your Django 
  - Once an **Order** is created it will automatically build our Route no?
- [x] Working on **Drivers** User story:
  - Build shipment tracking page 
    - Render Folium map as [Embedded HTML](https://youtu.be/KHi58Gf5EJE?si=tBDJ7bTgAFmQtayp&t=341) 
  - Search functionality (Tracking number, pickup/delivery address) (Chain Queries)
  - ~~View Tracking information (Specific Shipment)~~ (Work on tomorrow)
  - ^ Included maps for routes + eta
    - **GET** REquest no need to Post/Delete/Put
- We may need to work on changing the **Status** level the Drivers could do that 
- Instead of generate a route automatically (upong save which is bad because address might not always be good) Drivers could do that

**03/07**
- Work with FOrm Errors (Inventory + Product) (Done)
- Work with Inventory Search (Done)
- LowStock => Email or Message/Toast 
  - Standalone Inventory ONLY (Done)
  - Alert Setting check box?
    - Checkbox --> `request.POST.getlist('checkbox_name')` --> If notification doesnt exist in **InventoryNotification** model, then we add
    - Signal --> Restock is set --> send email to ALL users who requested to be notified 
      - Notified Flag if True then we won't send another email (prevents spamming )
      - ~~Pre-save logic checks state transition: if restock goes from `False` to `True` we email~~  
- ~~Decrease inventory when an order was made?~~ 

**03/06**
- [OpenRouteServices](https://openrouteservice.org/) | [Stripe](https://stripe.com/) NO TIME => Django email 
  -  [Getting Directions](https://www.youtube.com/watch?v=xBxWuq8SR6k)
  -  MAYBE [Rout Optimization](https://youtu.be/OOCvhc0k1R4?si=UVgdZ-y9n1AZDisy)
- Forgot Password 
  - we'll use a real [reset password](https://dev.to/earthcomfy/django-reset-password-3k0l) 
  - requires an actual working email 
  - Setting up Django Emails 
    - Google acc --> Turn **on** 2 factor auth --> **app passwords**
    - add app pass + email to `.env`  
  - We inherited from `PasswordResetView` creatin an email template body, subject template txt file and success url once we send out the email
  - Inside that email, we have a link to our custom `PasswordResetConfirmView` which renders out our form that takes *new_password* and *confirm new_password* but **also** redirects us to a success page: `PasswordResetCompleteView` 
    - All of these views are `from django.contrib.auth import views as auth_views`
- View Specific Inventory based off SKU
- Update & Remove Inventory
- **When you update a product, make sure the slug field also updates**
- ~~Work with FOrm Errors (Inventory + Product)~~
- ~~Work with Inventory Search~~
- ~~LowStock => Email or Message/Toast~~

**03/05**
- Handling Product/Inventory Signal 
- Update Total Price Signal 
- Django Commands to insert Fake Data?
  - `faker` `pip install Faker` + `pip install colorama`
  - Based on Products/Inventory we could use `py manage.py create_ws_data -n 10 -m Inventory` *to create 10 Testing Inventory Data* 
- Warehouse Staff User Story:
  -  Inventory Management Page 
  -  [Searching](https://learndjango.com/tutorials/django-search-tutorial) Inventory based off SKU 
     - **Parent Search HTML** where we create a *block* use *variables* then in our **Child template** we use the *block* and supply the *variables*
     - `{% with var=val var2=val2 %}`  
     - Form sends a `GET` request without a *csrf token* which redirects us BACK to our current page **WITH URL PARAMS**
     - use `Q` with `filter` to search our model based on `request.GET.get('url_param')`   
  - ~~View Specific Inventory based off SKU~~
  -  Create new inventory and product
     - This would suggest that Product:Inventory = One:Many relationship 
     - But we'll build an inventory by default   
     - Forms appear as Modal switching via Button on that modal 
       - Error handling, Toast message, Bootstrap form  
  -  ~~Update & Remove Inventory~~
-  Prepare to merge (github):
   -  Add and Commit any changes 
   -  `git fetch origin master` to fetch the latest changes 
   -  `git merge origin/master`
   -  Resolve conflict + add commit new changes 
   -  Push changes + pull request 
   -  `python manage.py makemigrations --merge`


**03/04** 
  - Profile Page 
    - Update Form with **help texts** and **fields** (Including *New Password*)
      - Handle Form Errors as well 
    - Display of current contact info 
    - Need to work on File Submission & Delete account 
      - `request.FILES` for our Form Class and `enctype="multipart/form-data"` for our Form Tag  
      - Bootstrap Modal to confirm Delete
  - Success/Error Message 
    - Figure out how to use `toast` + handle `form errors` 
    - Django `messages`
      - Custom tags in `settings.py`. Our `base.html` (which we extend on every temp) houses our toast and has a js script to show it 
      - [Guide](https://stackoverflow.com/questions/67044129/django-messages-bootstrap-toast-how-to-make-it-work)
      - [JS Toast Event](https://joshkaramuth.com/blog/django-messages-toast-htmx/)
  - Favicon
  - Product + Inventory Management 
    - Signals => total price 
    - Signals => Create Inventory once Product is created  
    - `pip install django-extensions` to access shell_plus

**02/27**
  - Authentication System 
  - Media & Static [Files](https://dev.to/emiloju/how-to-handle-media-uploads-in-django-1kpc) 
  - [Bootstrap5](https://www.w3schools.com/django/django_add_bootstrap5.php) Integration 
    - `pip install django-bootstrap-v5` 
  - [Side](https://dev.to/codeply/bootstrap-5-sidebar-examples-38pb) Nav & Base HTML 
  - MySQL Database 
    - `pip install mysqlclient` 
  - Envrionmental Variables
    - `pip install python-dotenv` 
    - Be sure to add a `.env` with: *DEBUG_LOCAL*, *MYSQL_LOCAL_CONNECTION*, *SECRET_LOCAL_KEY*
      - **MYSQL_LOCAL_CONNECTION** should follow: `"NAME USER PASSWORD HOST PORT"`
  - Tasks to Consider:
    - Profile Page & Uploading / Display Profile Image 
    - Login/Register Display Succes/Error Message
    - Replace Home Icons 
    - Start working on the Different Management Pages 


## User Authentication 
- [x] [Custom](https://dev.to/earthcomfy/getting-started-custom-user-model-5hc) LMS User
  - Role Field (default to "Worker") Updated by **ADMINS**
  - Depending on each role, they'll be granted certain access     
- [x] Register & Login Page (Error/Success Message)
- [x] Sign Out (Error/Success Message)
- [x] Updating Profile Information 


## Order Management 

## Inventory Management 

## Route Optimzation 
