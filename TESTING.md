# TESTING 

Return to the [README.md](README.md)

## Validator testing and browser compatibility
- I have tested Python code with - [PEP8 validator](http://pep8online.com/), ...


- All errors have been corrected


- HTML Validation was made with ![W3 validator](https://validator.w3.org/)


- CSS Validation was made with Jigsaw ![W3 validator](https://jigsaw.w3.org/)



## Accessibility
- I have confirmed that the Website is accessible by inspecting it in Lighthouse on the [Google Chrome](https://www.google.com/chrome/?brand=FKPE&gclid=EAIaIQobChMIqOPWwuu69AIVFeDtCh1CEgKGEAAYASAAEgKvwvD_BwE&gclsrc=aw.ds) Dev tools.
    
Result for desktop 
 - Performance for the desktop version 


Result for mobile devices
- Performance for mobile devices 



## Bugs

### Solved
- All problems from [Gitpod](https://www.gitpod.io/) from the image have been resolved. Most of them were indentation bugs and lines of code too long.

![solved bugs]

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


### STRIPE payment testing

- I have tested Stripe payment with card provided in Stripe documents.

![stripe payment testing card](media/testing/stripe_card_testing.png)

![stripe payment testing payment](media/testing/stripe_payment_testing.png)

### Unsolved bugs
- Unsolved problem which relates to ms-toolsai.jupyter extension not bein synched and not added in .gitpod.yml. I have checked Slack community and this is known issue which we can ignore.
- This is also part of the repository cloned for the project that should not be touched.


### Django Administration testing
- I have tested Django Administration,

