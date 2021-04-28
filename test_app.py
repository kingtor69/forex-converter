from unittest import TestCase
from app import app
from flask import session


class ForexAllIsWellTests(TestCase):

    # TODO -- write tests for every view function / feature!
    # the rest of the code, obviously enough, written by Tor Kingdon
    
    def test_home(self):
        """tests that home page loads on first visit"""
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1 class="text-center">Forex Currency Converter</h1>', html)
    
    def test_conversion(self):
        """tests conversion logic is working for $1 to equal $1 and for decimals to be output properly"""
        with app.test_client() as client:
            res = client.post('/submit', data = {'from': 'USD', 'to': 'USD', 'amt': '1'}, follow_redirects=True)
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn("""<td colspan="2" class="rounded border border-dark msgs success text-light">
                    US$ 1.00 converted is 
                    
                      <h2>
                        US$ 1.00
                      </h2>
                    
                  </td>""", html)
            
    def test_redirect_from_submit(self):
        """tests for redirection happening after form submission"""
        with app.test_client() as client:
            res = client.post('/submit', data = {'from': 'USD', 'to': 'USD', 'amt': '1'})
            self.assertEqual(res.status_code, 302)  

    def test_reset(self):
        """tests that session data is cleared and home page is reloaded"""
        with app.test_client() as client:
            res = client.get('/reset', follow_redirects=True)
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<input type="text" id="amt" name="amt" placeholder="1" required="required" aria-required="true" value="">', html)


class ForexErrorTests(TestCase):

    def test_bad_currency_codes():
        """test for all three fields being wrong"""
        with app.test_client() as client:
            res = client.post('/submit', data = {'from': 'apples', 'to': 'oranges', 'amt': '1'}, follow_redirects=True)
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn("""<thead class="card-title border-bottom text-dark bg-warning">
            
              
                <tr>
                  
                  <td colspan="2" class="rounded border border-dark msgs errors text-dark">
                    From currency code (APPLES) is not valid.
                    
                  </td>
                </tr>
              
                <tr>
                  
                  <td colspan="2" class="rounded border border-dark msgs errors text-dark">
                    To currency code (ORANGES) is not valid.
                    
                  </td>
                </tr>
              
                <tr>
                  
                  <td colspan="2" class="rounded border border-dark msgs errors text-dark">
                    Amount (many) must be a number.
                    
                  </td>
                </tr>
              
            
            </thead>""", html)

# class ForexSessionTests(TestCase):
#     @classmethod
#     def setUp(self):
#         self.client = app.test_client()
#         with self.client.session_transaction() as sess:
#             sess[''] = ''
    
#     def test_(self):
#         res = self.client.get('')
#         html = res.get_data(as_text=True)
#         self.assertEqual(res.status_code, 200)
#         self.assertIn('', html)