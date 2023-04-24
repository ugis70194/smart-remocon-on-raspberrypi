import unittest
import requests

class TestHTTPResponse(unittest.TestCase):
  
  def test_reach_light_on(self):
    req = requests.get("http://localhost:3000/light_on")
    self.assertEqual(req.status_code, 200)
    
  def test_response_light_on(self):
    req = requests.get("http://localhost:3000/light_on")
    response_code = req.json()["response_code"]
    self.assertEqual(response_code, "OK")
    
  def test_reach_light_off(self):
    req = requests.get("http://localhost:3000/light_off")
    self.assertEqual(req.status_code, 200)
    
  def test_response_light_off(self):
    req = requests.get("http://localhost:3000/light_off")
    response_code = req.json()["response_code"]
    self.assertEqual(response_code, "OK")
    
if __name__ == "__main__":
  unittest.main()