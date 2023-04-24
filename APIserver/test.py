import unittest
import requests

class TestHTTPResponse(unittest.TestCase):
  
  def test_light_on(self):
    req = requests.get("http://localhost:3000/light_on")
    self.assertEqual(req.status_code, 200)
    
  def test_light_off(self):
    req = requests.get("http://localhost:3000/light_off")
    self.assertEqual(req.status_code, 200)