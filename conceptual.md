### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  * Python is cooler than JavaScript ;)
  * Seriously, though, Python run on the server
    - that means it can not run offline on a user's computer without additional software installed
    - on web apps, Python uses a framework such as Flask to interact with the user's browser (which in turn interacts with the user)
    - JavaScript runs on the users browser and can run on that browser without an internet connection or any additional software

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  * honestly, I don't see the need for two, but here goes:
    1.  c = dic.get('c')
    2.  c = None
        for key in dic.keys:
            if key == 'c':
                c = dic['c']
 
  * both can be done with an alternate value. e.g:
    1.  c = dic.get('c', 3)
    2.  c = None
        for key in dic.keys:
            if key == 'c':
                c = dic['c']
            else:
                c = 3

- What is a unit test?

  * A unit test is to determine if any given method or function within a program functions as expected. It is analagous to removing the video card from a computer and testing it isolated from the computer

- What is an integration test?

  * An intergration test determines how a group of methods, functions or programs work together. To use the computer hardware analogy above, you would be running an integration test by keeping (or replacing) the video card in the computer and testing the video card by inputting predetermined data and response from the card to the motherboard.
  
- What is the role of web application framework, like Flask?

  * without a web app framework like Flask, Python can only be run with special software not found in a web browser. Flask interprets data from the web browser and allows Python to work with that data, then the framework translates the response from Python to something the user can see and interact with via their web browser.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  * If the information to be passed into the application is entered by the user into a form, it would generally be easier to pass that data in a query string
  * This is especially true if there are more variables than just one (e.g. 'foods?type=pretzel+salt=True+sweet=False')
  * route URLs are better used for pre-determined routes, such as a choose your own adventure game (e.g. '/chapter/1/d') or a series of questions on a survey ('/question/3')

- How do you collect data from a URL placeholder parameter using Flask?

  * using the "decorator" @app.route with the variable in pointy-brackets, like this:
      @app.route('/question/<int:question_num>')
      def show_question(question_num):

- How do you collect data from the query string using Flask?

  * within the method (after the decorator and method definition), the items in the query string are accessible using `request.args`['<variable>'], e.g:
      @app.route('/foods')
      def display_food_info():
          food_type = request.args['type']

- How do you collect data from the body of the request using Flask?

  * 

- What is a cookie and what kinds of things are they commonly used for?

- What is the session object in Flask?

- What does Flask's `jsonify()` do?

  * `jsonify()` turns a set or dictionary into a string, which is a format that can be transferred between server and browser and parsed at the other end and accessed as an object in JavaScript
