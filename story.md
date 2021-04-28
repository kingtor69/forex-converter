# Forex currency converter
## The Story
## by Tor Kingdon

1. home route/page `('/', 'home.html')`
   1. user is presented with a form asking for currency codes to convert from and to, and an amount
      1. all fields are marked required in HTML template
      2. codes are "text" inputs and amount is "number
2. `'/submit'` route
   1. properly format the form data
      1. convert codes to upper-case strings
      2. round the amount to 2 digits
   2. check validity
      1. check if from/to codes are valid Forex CurrencyCodes
      2. check that the amount is a positive number
   3. prepare error messages
      1. make each message into a string
      2. complie those messages into a list of errors:
            `session['messages'] = [<from_error>, <to_error>, <amt_error>]`
    4. if there are errors, redirect to `'/'`
       1. the when `session['messages']` exists, this will display the error messages and the form for resubmission
    5. if no errors, redirect to `'/convert'`
 1. `'/convert'` route
    1. run conversion
    2. round converted amount to 2 digits(?)
    3. add `session['converted'] = <converted_amount>`
    4. redirect to `'/'`
