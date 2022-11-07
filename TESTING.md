# TESTING 

Return to the [README.md](README.md)

# Table of content:
- [Validator testing](#validator-testing)
- [Browser compatibility](#browser-compatibility)
- [Manual testing](#manual-testing)
- [Accessibility](#accessibility)
- [Bugs](#bugs)
  - [Solved bugs](#solved-bugs)
  - [Unsolved bugs](#unsolved-bugs)
- [STRIPE payment testing](#stripe-payment-testing)
- [Email verification testing when signing up](#email-verification-testing-when-signing-up)
- [Django Administration testing](#django-administration-testing)


## Validator testing

Python code problems were showing within the workspace.

![python problems](media/testing/python_errors.png)

- All Python workspace problems have been corrected.

![python problems resolved](media/testing/python_errors_fixed.png)

- After clearing all the from from the terminal, I have tested Python code with - [PEP8 validator](http://pep8online.com/) but as the Website was compromised I have validated code through gitpod as per Code Institute instructions.

![python problems resolved](media/testing/pep8.png)

- No problems were detected.

![python problems resolved](media/testing/python_clear.png)

All HTML Urs were validated with ![W3 validator](https://validator.w3.org/):

[Landing page](https://validator.w3.org/nu/?doc=https://art-of-chocolate.herokuapp.com/)

[Category page](https://validator.w3.org/nu/?doc=https://art-of-chocolate.herokuapp.com/?category=dark_chocolate)

[Login](https://validator.w3.org/nu/?doc=https://art-of-chocolate.herokuapp.com/accounts/login/)

[Signup](https://validator.w3.org/nu/?doc=https://art-of-chocolate.herokuapp.com/accounts/signup/)

[Basket](https://validator.w3.org/nu/?doc=https://art-of-chocolate.herokuapp.com/basket/)

[Chocolate page](https://validator.w3.org/nu/?doc=https://art-of-chocolate.herokuapp.com/chocolate_page/35)

[Password reset](https://validator.w3.org/nu/?doc=https://art-of-chocolate.herokuapp.com/accounts/password/reset/)

[Checkout](https://validator.w3.org/nu/?doc=https://art-of-chocolate.herokuapp.com/checkout/)

[Contact us](https://validator.w3.org/nu/?doc=https://art-of-chocolate.herokuapp.com/contact/)

Some of the validation screenshots can be found below.

Main page validation
![html problems](media/testing/html_validation.png)

Checkout session error was showing below error but it was validated by Page source and also in the live booking process.
![checkout problem](media/testing/checkout_error.png)

Checkout session validated in live booking process.

![checkout problem resolved](media/testing/checkout_validated.png)

- Errors from all pages have been corrected.

![html problems resolved](media/testing/html_validated.png)


- CSS Validation was made with Jigsaw ![W3 validator](https://jigsaw.w3.org/css-validator/) and was showing no errors.

![checkout problem resolved](media/testing/css_validation.png)

## Browser compatibility

Different browsers were used to validate the look and compatibility of the page.

Landing page [Google Chrome](https://www.google.com/chrome/?brand=YTUH&gclid=EAIaIQobChMIlsOG9sya-wIVcoBQBh3FIgOFEAAYASAAEgIHcfD_BwE&gclsrc=aw.ds)

![google chrome screenshot](media/testing/google_chrome.png)

Chocolate page [MS Edge](https://www.microsoft.com/en-us/edge)

![ms esgde screenshot](media/testing/ms_edge.jpeg)

Contact Us page [Mozzilla Firefox](https://www.mozilla.org/en-US/firefox/new/)

![mozilla firefox screenshot](media/testing/mozilla.png)

## Manual testing

I have manually tested functionality of the Website:
 - Sign in with E-mail verification.
 - Adding products to basket as Anonymous and Registered User.
 - Stripe payment with mailjet confirmation E-mail.
 - Newsletter with Mailchimp and adding E-mails to Audience section.
 - Shipping form - not to let user to proceed without filling the form and adding numbers to phone number input field.
 - Contact Us form which is submitted to the terminal.
 - Buttons on all pages to make sure they are working (adding product, removing product, submitting forms).
 - Access and restrictions for specific users -  Anonymous, Registered and Superuser.
 - Using print to check Javascript code.

## Accessibility
I have confirmed that the Website is accessible by inspecting it in Lighthouse on the [Google Chrome](https://www.google.com/chrome/?brand=FKPE&gclid=EAIaIQobChMIqOPWwuu69AIVFeDtCh1CEgKGEAAYASAAEgKvwvD_BwE&gclsrc=aw.ds) Dev tools.
    
Result for desktop 
 - Performance for the desktop version 

![lighthouse desktop](media/testing/desktop_low_lighthouse.png)

 - Increased parameters.

![checkout problem resolved](media/testing/desktop_performance_increased.png)

 - Future implementation to improve best practices : Resizing images.
 - I tried removing Javascript from base.html and CSP added as meta tag but result for Best Practices dicreased.
![best practices](media/testing/best_practices.png)

Result for mobile devices
- Performance for mobile devices 

![lighthouse mobile](media/testing/mobile_lighthouse.png)

## Bugs

### Solved bugs
All problems from [Gitpod](https://www.gitpod.io/) have been resolved. Most of them were Python related, indentation bugs and lines of code too long.

- Attribute error - resolved by removing shop app name from the apps list.

![solved bugs attribute error](media/testing/attribute_error.png)

- Not Found error - resolved by adding correct path to urls.py file.

![solved bugs not found error](media/testing/not_found_error.png)

- ProgrammingError at - Models were updated but migration was not done. Resolved by making migrations and migrating new model added.

![solved bugs programming error](media/testing/programming_error.png)

- IndentationError - Migration was not processing due to incorrect indentationt, indentation corrected to resolve the issue.

![solved bugs indentation error](media/testing/indentation_error.png)

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

### Email verification testing when signing up

- Verification was tested both locally and through deployed website.

![verification local](media/testing/verification_local_test.png)

- Processing payment
![verification deployed](media/testing/verification_deployed_test.png)

### Django Administration testing
- I have tested Django Administration and all is working as it should. All data is storing as intended.

![django test](media/testing/django_test.png)
