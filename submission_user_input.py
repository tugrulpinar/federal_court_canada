from data_base import Contacts, SubmissionTypes
import pandas as pd
import time


class CourtInfo:
    def __init__(self):
        self.app_last_name = ""
        self.court_no = ""
        self.type = ""
        self.alt_email = ""
        self.s = SubmissionTypes()
        self.c = Contacts()

    def get_input(self):
        self.__get_last_name()
        self.__get_court_no()
        self.__get_submission_type()
        self.__get_alt_email()

    def __get_last_name(self):
        while True:
            self.app_last_name = input(
                "Please enter Applicant Last Name: ").strip()
            if self.app_last_name.isalpha() and len(self.app_last_name) > 0:
                break
            else:
                continue

    def __get_court_no(self):
        while True:
            self.court_no = input("Please enter the Court Number: ").strip()
            no = "IMM"
            if self.court_no.startswith(no.lower()) or self.court_no.startswith(no.upper()):
                break
            else:
                print("Please include the 'IMM'\n")
                continue
        print("")

    def __get_submission_type(self):
        while True:
            self.type = input(
                "What type of submission we are making?\na) Application Record\nb) Reply Memo\nc) Notice of Discontinuance\nd) Notice of Change of Solicitor\ne) Book of Authorities\nf) Motion Record\ng) Letter\n").strip()
            self.type = self.type.lower()
            if self.type in "abcdefg" and len(self.type) > 0:
                print("")
                print(self.app_last_name.upper())
                print("")
                print(f"Court Number: {self.court_no}")
                print("")
                print(
                    f"Type of submission: {self.s.choices.get(self.type.lower())}")
                print("")
                break
            else:
                print("Please select one of the options\n")
                print("")
                continue

    def __get_alt_email(self):
        # PROMPT THE USER FOR ALTERNATIVE EMAIL
        emails = pd.Series(self.c.secondary_emails)
        print(emails)
        print("")
        while True:
            self.alt_email = input(
                "Secondary email (Please put initials): ").strip()
            self.alt_email = self.alt_email.upper()
            if len(self.alt_email) == 0:
                print("")
                print("Please provide an input\n" + "\n")
                continue
            elif self.alt_email not in self.c.secondary_emails:
                print("")
                print(
                    "Sorry, there's no email address associated with these initials. Please try something else.\n")
                continue
            else:
                print("")
                print(
                    f"Submission confirmation will also be sent to {self.c.secondary_emails[self.alt_email]}\n")
                time.sleep(2)
                break
