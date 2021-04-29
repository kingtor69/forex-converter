### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  * Python is cooler than JavaScript ;)
  * Seriously, though, Python runs only on the server:
    * that means it can not run offline on a user's computer without additional software installed
    * on web apps, Python's interaction with the web server and the "front end" requires extra attention from software developers
  * JavaScript can be run on the server side (Node JS), but what we've learned so far runs in the browser

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

  * A unit test is used to determine if any given relatively simple method or function within a program functions as expected. There are small "units" of the overall program. A unit test is testing either the front-end or the back-end programming, but not both.

- What is an integration test?

  * An intergration test determines how the small units of the program interact with each other. Integration tests can be used to test the interaction between front- and back-end programming.
  
- What is the role of web application framework, like Flask?

  * Frameworks such as Flask (or Jinja or others) can be used to make the interaction between Python and the front end of a web app. These frameworks manage data going between front- and back-end languages to make life easier for the developer and seemless to the user. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  * A query string is user-readable and easily shared between users since the user can see both the prompt ('type=') and the response ('pretzel') and thus it's easier to understand the second part of the URL.
  * This is especially true if there are more variables than just one (e.g. 'foods?type=pretzel+salt=True+sweet=False'), which is a good reason to use a query string for more complex structures.
  * route URLs are better used on simpler distinctions, like there is only one variable and the prompt is either unimportant or self-explanatory

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

  * request.form['<variable>'] retrieves data from a POSTed form
  * request.json['<variable>'] retrieves data from a POSTed JSON string

- What is a cookie and what kinds of things are they commonly used for?

  * A cookie is a file stored on the user's computer that contains information the server accessess in order to customize the app's output for that user. 
  * For example, when a user logs in the cookie would be set to a logged-in state, or if the user has selected some viewing preferences. This way they don't have to keep answering the same questions no matter how many pages they go to within a specific web app.

- What is the session object in Flask?

  * The session object is similar to a cookie except that the information stored within is not useful to the user.
  * There is a cookie used in Flask's session, but it serves as a reference to the actual data which is stored on the server.

- What does Flask's `jsonify()` do?

  * `jsonify()` turns a set or dictionary into a JSON string.
