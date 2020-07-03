from django.test import TestCase
from django.test import SimpleTestCase
from django.test import Client

# test views.py functions
from .views import get_ics, ics_to_gcal
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# test models.py sending and getting data to and from db

import re, os, time


# class LoginForHomePageServiceTest(TestCase):

#     def test_existingStudentLogin(self):
#         response = self.client.post(
#             '/timetasker/userlogin', {'unikey': 'hlee3288', 'password': '4594j9C7'})
#         self.assertEquals(response.status_code, 302)
#         self.assertRedirects(response, '/timetasker/home')


#     def test_onlyUnikeyLogin(self):
#         response = self.client.post(
#             '/timetasker/userlogin', {'unikey': 'meow', 'password': ''})
#         self.assertEquals(response.status_code, 401)


#     def test_onlyPasswordLogin(self):
#         response = self.client.post(
#             '/timetasker/userlogin', {'unikey': '', 'password': 'woof'})
#         self.assertEquals(response.status_code, 401)


#     def test_notExistingStudentLogin(self):
#         response = self.client.post(
#             '/timetasker/userlogin', {'unikey': 'meow', 'password': 'woof'})
#         self.assertEquals(response.status_code, 401)


#     def test_noInputToLogin(self):
#         response = self.client.post(
#             '/timetasker/userlogin', {'unikey': '', 'password': ''})
#         self.assertEquals(response.status_code, 401)


# class LogoutTest(TestCase):

#     def test_existingStudentLogout(self):
#         response = self.client.post(
#             '/timetasker/userlogin', {'unikey': 'hlee3288', 'password': '4594j9C7'})
#         self.assertEquals(response.status_code, 302)
#         self.assertRedirects(response, '/timetasker/home')
#         response = self.client.post('/timetasker/logout')
#         self.assertEquals(response.status_code, 302)

#     def test_existingStudentLogout_And_Login(self):
#         response = self.client.post(
#             '/timetasker/userlogin', {'unikey': 'hlee3288', 'password': '4594j9C7'})
#         self.assertEquals(response.status_code, 302)
#         self.assertRedirects(response, '/timetasker/home')
#         response = self.client.post('/timetasker/logout')
#         self.assertEquals(response.status_code, 302)
#         response = self.client.post(
#             '/timetasker/userlogin', {'unikey': 'hlee3288', 'password': '4594j9C7'})
#         self.assertEquals(response.status_code, 302)
#         self.assertRedirects(response, '/timetasker/home')


# class AccessHomePageServiceTest(TestCase):

#     def test_AccessHomePageWithoutLogin(self):
#         response = self.client.post('/timetasker/home')
#         self.assertEquals(response.status_code, 302)
#         self.assertRedirects(response, '/timetasker/userlogin')


# class ICS_FileGetterTest(TestCase):

    # def test_getICSFileWithExistingStudentAccount(self):
    #     self.assertEquals(bool(re.search(
    #         "^https://www.timetable.usyd.edu.au/personaltimetable/timetable/calendar/(.*)/timetable.ics$", get_ics('hlee3288', '4594j9C7'))), True)

    # def test_getICSFileWithInvalidUnikey(self):
    #     self.assertEquals(bool(re.search(
    #         "^https://www.timetable.usyd.edu.au/personaltimetable/timetable/calendar/(.*)/timetable.ics$", get_ics('meow', ''))), False)
    
    # def test_getICSFileWithInvalidPassword(self):
    #     self.assertEquals(bool(re.search(
    #         "^https://www.timetable.usyd.edu.au/personaltimetable/timetable/calendar/(.*)/timetable.ics$", get_ics('', 'woof'))), False)
    
    # def test_getICSFileWithInvalidStudentAccount(self):
    #     self.assertEquals(bool(re.search(
    #         "^https://www.timetable.usyd.edu.au/personaltimetable/timetable/calendar/(.*)/timetable.ics$", get_ics('meow', 'woof'))), False)
    
    # def test_getICSFileWithNoAccountDetails1(self):
    #     self.assertEquals(bool(re.search(
    #         "^https://www.timetable.usyd.edu.au/personaltimetable/timetable/calendar/(.*)/timetable.ics$", get_ics('', ''))), False)
    
    # def test_getICSFileWithNoAccountDetails2(self):
    #     self.assertEquals(get_ics(None, None), False)

#class ICS_FileUploaderToGcalTest(TestCase):
#
#    def checkForCalendar(username, password):
#        direct_path = os.path.dirname(os.path.abspath(__file__))
#    
#        if direct_path is not None:
#            print("driver path found")
#        
#            direct_path = direct_path + '\\chromedriver.exe'
#        # INSERT DRIVER HERE dashuifnmoeasdmoa
#            driver = webdriver.Chrome(direct_path)
#            driver.get('https://accounts.google.com/ServiceLogin/signinchooser?service=cl&passive=1209600&osid=1&continue=https%3A%2F%2Fcalendar.google.com%2Fcalendar%2Fr&followup=https%3A%2F%2Fcalendar.google.com%2Fcalendar%2Fr&scc=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
#            username_field = driver.find_element_by_name("identifier")
#            username_field.send_keys(username)
#            username_field.send_keys(Keys.RETURN)
#            driver.implicitly_wait(2)
#            password_field = driver.find_element_by_name("password")
#            password_field.send_keys(password)
#            password_field.send_keys(Keys.RETURN)
#            time.sleep(3)
#            driver.implicitly_wait(3)
#            timetable = driver.page_source
#            result = bool(re.search("Student Timetable", timetable))
#            return result
    
    # def test_ICS2GCALInsertionTest(self):
    #     self.assertEquals(ics_to_gcal("soft2201.timetasker@gmail.com", "0118nineninenineeighteight199nine119sevenTWOfive_3", "https://www.timetable.usyd.edu.au/personaltimetable/timetable/calendar/460026008/cA7uYkLM1cytOgc6mvo1mwEIGvcAe3roJQLgCPM9eBo/timetable.ics"), True)
    #     self.assertEquals(checkForCalendar("soft2201.timetasker@gmail.com", "0118nineninenineeighteight199nine119sevenTWOfive_3"), True)
    
    # def test_ICS2GCALInvalidICSTest(self):
    #    self.assertEquals(ics_to_gcal("soft2201.timetasker@gmail.com", "0118nineninenineeighteight199nine119sevenTWOfive_3", "https://www.timetable.usyd.edu.au/personaltimetable/timetable/calendar/460026008/cA7uYkLM1cytOgc6mvo1mwEIGvcAeroJQLgCPM9eBo/timetable.ics"), False)
    #     self.assertEquals(checkForCalendar("soft2201.timetasker@gmail.com", "0118nineninenineeighteight199nine119sevenTWOfive_3"), False)

    # def test_ICS2GCALInvalidGmailTest(self):
    #     self.assertEquals(ics_to_gcal("thisisnotarealaccount", "0118nineninenineeighteight199nine119sevenTWOfive_3", "https://www.timetable.usyd.edu.au/personaltimetable/timetable/calendar/460026008/cA7uYkLM1cytOgc6mvo1mwEIGvcAe3roJQLgCPM9eBo/timetable.ics"), True)
    #     self.assertEquals(checkForCalendar("soft2201.timetasker@gmail.com", "0118nineninenineeighteight199nine119sevenTWOfive_3"), False)    
    
    # def test_ICS2GCALInvalidPasswordTest(self):
    #     self.assertEquals(ics_to_gcal("soft2201.timetasker@gmail.com", "password", "https://www.timetable.usyd.edu.au/personaltimetable/timetable/calendar/460026008/cA7uYkLM1cytOgc6mvo1mwEIGvcAe3roJQLgCPM9eBo/timetable.ics"), True)
    #     self.assertEquals(checkForCalendar("soft2201.timetasker@gmail.com", "0118nineninenineeighteight199nine119sevenTWOfive_3"), False)    
    