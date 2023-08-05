# Stellar burger

#### The project was created for studying of Python auto test.
#### This project covers UI test for site https://stellarburgers.nomoreparties.site/
#### There was used the pytest lib and selenium WebDriver lib for creating and running auto-tests

### List of pages are covered by test (not fully):
* **the main page** - page with constructor and navigation buttons
* **profile** - page with personal info and logout button
* **login** - page to login
* **restore password** - page to restore password
* **registration** - page for registration

#### The following tests were created to cover the UI functionality

### List of tests (tests folder):
* **test_registration_page** - this class is for the registration cases
  * **test_registration_correct_data** - this method checks a success registration with correct email and password
 * **test_registration_too_short_password** -this method checks an error message if password too short 
* **test_login_page** - this class is for the login cases
  * **test_login_correct_data_via_login_btn** - this method checks success login via login button on the main page
  * **test_login_correct_data_via_profile** - this method checks success login though the profile page
  * **test_login_correct_data_via_restore_password** - this method checks success login on the restore password page
  * **test_login_correct_data_via_registration** - this method checks success login on the registration page
* **test_logout** - this class is for the logout cases
  * **test_logout_after_success_login** - this method checks success logout on the profile page
* **test_navigation** - this class is for the navigation between pages cases
  * **test_navigation_from_profile_to_constructor** - this method checks a navigation from the profile page to the main page, constructor block
  * **test_navigation_from_constructor_to_profile** - this method checks a navigation from the main page to the profile page
* **test_constructor** - this class is for the navigation inside the constructor block cases
  * **test_navigation_inside_constructor_without_login_sauce** - this method checks a navigation to the sauce block inside the constructor
  * **test_navigation_inside_constructor_without_login_filling** - this method checks a navigation to the filling block inside the constructor
  * **test_navigation_inside_constructor_without_login_buns** - this method checks a navigation to the buns block inside the constructor


*the test coverage is not 100%, only some main functionality*