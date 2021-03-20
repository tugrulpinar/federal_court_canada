from pdf_recognizer import PdfRecognizer
from uinput import UserInput


class DecisionMaker():
    def __init__(self):
        self.pdf_rec = PdfRecognizer()
        self.user_input = UserInput()
        self.app_first_names = None
        self.app_last_names = None
        self.app_number_of_applicants = None
        self.app_type_of_decision = None
        self.app_alt_email = None

    def start_engine(self):
        self.pdf_rec.scan_pdf()
        self.__get_permission()

    def __get_permission(self):
        while True:
            answer = input(
                "\nBased on this information, do you wish you proceed with e-filing?\nA) Yes\nB) No\n").strip()

            # MAKE SURE THE USER PROVIDES AN INPUT
            if len(answer) < 1:
                continue

            # IF YES, PROCEED WITH THE EFILING
            if answer in "Aa":
                print('\n')
                self.user_input.get_alt_email()
                self.app_first_names = self.pdf_rec.applicant_names
                self.app_last_names = self.pdf_rec.applicant_lastnames
                self.app_number_of_applicants = self.pdf_rec.number_of_applicants
                self.app_type_of_decision = self.pdf_rec.application_type
                self.app_alt_email = self.user_input.c.secondary_emails[self.user_input.alt_email]

                break
            # IF NO, GET THE APPLICANT INFO FROM THE USER MANUALLY
            elif answer in "Bb":
                self.user_input.get_user_input()
                self.app_first_names = self.user_input.first_names
                self.app_last_names = self.user_input.last_names
                self.app_number_of_applicants = self.user_input.number_of_applicants
                self.app_type_of_decision = self.user_input.type_of_decision
                self.app_alt_email = self.user_input.c.secondary_emails[self.user_input.alt_email]

                break

            else:
                print("\nPlease select one of the options\n")
                continue
