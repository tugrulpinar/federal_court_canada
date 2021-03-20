import os
from data_base import Contacts
from pdfminer.high_level import extract_text
import pandas as pd
import time


class UserInput():
    def __init__(self):
        self.first_names = []
        self.last_names = []
        self.number_of_applicants = None
        self.type_of_decision = None
        self.alt_email = None
        self.c = Contacts()

    def get_user_input(self):
        self.__get_number_of_applicants()
        self.__get_full_names()
        self.__error_control()
        self.get_alt_email()

    def __get_number_of_applicants(self):
        # ASK FOR THE NUMBER OF APPLICANTS. 1) MAKE SURE THE USER PUTS IN AN INTEGER.
        # 2) PROMPT THE USER TO PUT A VALUE BEFORE PRESSING ENTER. 3) MAKE SURE TO GET RID OF THE WHITE SPACE.
        while True:
            try:
                self.number_of_applicants = int(
                    input("Please enter number of Applicants: ").strip())
                break
            except:
                print("Invalid input")

    def __get_full_names(self):
        # PROMPT THE USER FOR THE APPLICANT(S) NAMES BASED ON THE NUMBER THEY PREVIOUSLY PUT IN
        for x in range(1, self.number_of_applicants + 1):
            applicant_names = input(f"Applicant{x} First Name: ").strip()
            if len(applicant_names) == 0:
                print("Please provide correct input")
                self.first_names.clear()
                self.last_names.clear()
                self.__get_full_names()
                return
            applicant_lastnames = input(f"Applicant{x} Lastname: ").strip()
            if len(applicant_lastnames) == 0:
                print("Please provide correct input")
                self.first_names.clear()
                self.last_names.clear()
                self.__get_full_names()
                return

            self.first_names.append(applicant_names.title())
            self.last_names.append(applicant_lastnames.upper())

        print("")
        for x in range(self.number_of_applicants):
            print(self.first_names[x] + " " + self.last_names[x])

        return

    def __error_control(self):
        # ALLOW THE USER TO GO BACK AND REENTER NAMES IF THERE'S A MISTAKE
        mistake_control = input(
            "\nPlease review the full name(s) and press 'c' to continue. Press 'r' to re-enter names.\r\n").strip()
        mistake_control = mistake_control.lower()
        if len(mistake_control) == 0:
            print("\nPlease provide an input\n")
            self.__error_control()
        if mistake_control == "c":
            self.__get_type_of_decision()
            return
        elif mistake_control == "r":
            self.first_names.clear()
            self.last_names.clear()
            self.__get_full_names()
            self.__error_control()
            return
        else:
            print("\nInvalid input\n")
            self.__error_control()

    def __get_type_of_decision(self):
        # EXTRACT THE TEXT FROM THE PDF FILE TO PREDICT THE TYPE OF APPLICATION
        try:
            text = extract_text("App. for Leave", page_numbers=[1])
            if "Appeal" in text:
                print("PDF scan result: RAD Appeal")
            elif "Protection Division" in text:
                print("PDF scan result: RPD Appeal")
            elif "PRRA" in text:
                print("PDF scan result: PRRA Appeal")
            elif "H&C" in text:
                print("PDF scan result: H&C Appeal")
        except:
            pass

        # ASK FOR THE TYPE OF APPLICATION
        while True:
            t_of_d = input(
                "\nWhat type of application we are appealing?\na) RPD\nb) RAD\nc) PRRA\nd) H&C\ne) SP\nf) TRV\n").strip()
            self.type_of_decision = t_of_d.lower()
            if len(t_of_d) == 0:
                print("Please provide an input\n")
                continue
            elif self.type_of_decision in "abcdef":
                break
            else:
                print("Please select one of the options\n")
                continue

    def get_alt_email(self):
        # PROMPT THE USER FOR ALTERNATIVE EMAIL
        emails = pd.Series(self.c.secondary_emails)
        print(emails)

        while True:
            self.alt_email = input(
                "\nSecondary email (Please put initials): ").strip()
            self.alt_email = self.alt_email.upper()
            if len(self.alt_email) == 0:
                print("\nPlease provide an input\n" + "\n")
                continue
            elif self.alt_email not in self.c.secondary_emails:
                print(
                    "\nSorry, there's no email address associated with these initials. Please try something else.\n")
                continue
            else:
                print(
                    f"\nSubmission confirmation will also be sent to {self.c.secondary_emails[self.alt_email]}\n")
                time.sleep(2)
                break
