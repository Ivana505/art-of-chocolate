# TESTING 

Return to the [README.md](README.md)

## Validator testing

![python problems](media/testing/python_errors.png)

- All errors have been corrected

![python problems resolved](media/testing/python_errors_fixed.png)

- After clearing all the errors from the terminal, I have tested Python code with - [PEP8 validator](http://pep8online.com/) but as the Website was compromised I have validated code through gitpod as per instructions.

![python problems resolved](media/testing/ppep8.png)

- No problems were detected

![python problems resolved](media/testing/python_clear.png)

- All HTML Url were validated with ![W3 validator](https://validator.w3.org/)

Main page validation
![html problems](media/testing/html_validation.png)

Checkout session error
![checkout problem](media/testing/checkout_error.png)

- All errors have been corrected

![html problems resolved](media/testing/html_validated.png)

Checkout session validated in live booking process

![checkout problem resolved](media/testing/checkout_validated.png)


- CSS Validation was made with Jigsaw ![W3 validator](https://jigsaw.w3.org/) and was showing no errors.

![checkout problem resolved](media/testing/css_validation.png)

## Browser compatibility

Different browsers were used to validate the look and compatibility.

Landing page [Google Chrome](https://www.google.com/chrome/?brand=YTUH&gclid=EAIaIQobChMIlsOG9sya-wIVcoBQBh3FIgOFEAAYASAAEgIHcfD_BwE&gclsrc=aw.ds)

![google chrome screenshot](media/testing/google_chrome.png)

Chocolate page [MS Edge](https://www.microsoft.com/en-us/edge)

![ms esgde screenshot](media/testing/ms_edge.png)

Contact Us page [Mozzilla Firefox](https://www.mozilla.org/en-US/firefox/new/)

![mozilla firefox screenshot](media/testing/mozilla.png)

## Manual testing

- I have manually tested functionality of the Website:
 - Sign in
 - Logout
 - Adding to bag
 - Payment
 - Newsletter with Mailchimp 
 - Shipping Form
 - Contact Us form 
 - Buttons
 - Access and restrictions for specific users
 - Using print to check Javascript code

## Accessibility
I have confirmed that the Website is accessible by inspecting it in Lighthouse on the [Google Chrome](https://www.google.com/chrome/?brand=FKPE&gclid=EAIaIQobChMIqOPWwuu69AIVFeDtCh1CEgKGEAAYASAAEgKvwvD_BwE&gclsrc=aw.ds) Dev tools.
    
Result for desktop 
 - Performance for the desktop version 

![lighthouse desktop](media/testing/desktop_low_lighthouse.png)

 - Increased parameters.

![checkout problem resolved](media/testing/desktop_performance_increased.png)

 - Future implementation to improve best practices : Resizing images.
 - Tried removing Javascript from base.html and CSP added as meta tag but result for Best Practices dicreased.
![best practices](media/testing/best_practices.png)

Result for mobile devices
- Performance for mobile devices 
![lighthouse mobile](media/testing/best_practices.png)

## Bugs

### Solved bugs
All problems from [Gitpod](https://www.gitpod.io/) have been resolved. Most of them were Python related, indentation bugs and lines of code too long.

- Attribute error - resolved by removing shop app name from the apps list.

![solved bugs attribute error](media/testing/attribute_error.png)

- Not Found error - resolved by adding correct path to urls.py file.

![solved bugs not found error](media/testing/not_found_error.png)

- ProgrammingError at - Models were updated but migration was not done. Resolved by making migrations and migrating new models added.

![solved bugs programming error](media/testing/programming_error.png)

- IndentationError - Migration was not processing due to incorrect indentationt, indentation corrected to resolve the issue.

![solved bugs indentation error](media/testing/invalid_host_error.png)

- SyntaxError - Due to misspelling error migration was not possible, entry corrected to resolve the issue.

![solved bugs syntax error](media/testing/syntax_error.png)

- PermissionError - Error when tried to edit the product. Resolved with connecting and installing cloudinary correctly.

![solved bugs permission error](media/testing/permission_edit_error.png)

- NameError - Resolved by importing get_404 object to django.

![solved bugs name error](media/testing/name_error.png)

- TamplateDoesNotExist - error resolved by moving html to correct template folder.

![solved bugs template does not exist](media/testing/template_does_not_exist.png)

### Unsolved bugs
JSHint was showing two different warnings and one variable as unused.

 - I have added /* jshint esversion: 11, jquery: true */ to basket.js to ignore " ['quantity'] is better written in dot notation. " error.

 - restrictAlphabets variable is used within shipping form to restrict the user of inputting letters into the phone field.

![javascript errors](media/testing/java_script_warnings.png)

### STRIPE payment testing

- I have tested Stripe payment with card provided in Stripe documentation.

![stripe payment testing card](media/stripe/stripe_card_testing.png)

![stripe payment testing payment](media/stripe/stripe_payment.png)

![stripe payment url confirmation](media/stripe/order_confirmation_page.png)

![order email confirmation](media/stripe/email_confirmation.png)

![inbox email confirmation](media/stripe/inbox.png)

### E-mail verification testing when signing up

- Verification was tested both locally and through deployed website.

![verification local](media/testing/verification_local_test.png)

- Processing payment
![verification deployed](media/testing/verification_deployed_test.png)

### Django Administration testing
- I have tested Django Administration and all is working as it should. All data is storing as intended.

![django test](media/testing/django_test.png)
