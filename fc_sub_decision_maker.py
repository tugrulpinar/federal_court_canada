from sub_algo import SubmissionRecognizer
from submission_input import CourtInfo
from data_base import SubmissionTypes


class SubDMaker:
    def __init__(self):
        self.dm_imm = None
        self.dm_lname = None
        self.dm_alt_email = None
        self.type_letter = None
        self.algo = SubmissionRecognizer()
        self.input = CourtInfo()
        self.sub_type = SubmissionTypes()

    def initiate(self):
        self.input.get_submission_type()
        self.type_letter = self.input.type
        path = self.sub_type.choices[self.type_letter]
        try:
            self.algo.extract_keys(path)
            print(f"\nCourt No: {self.algo.imm}")
            print(f"\nApplicant Lastname: {self.algo.lastname}")
            self.user_confirmation()
        except:
            print("\nThere is no associated file in the directory")

    def user_confirmation(self):
        while True:
            answer = input(
                "\nBased on this information, do you wish you proceed with e-filing?\nA) Yes\nB) No\n").strip()

            # MAKE SURE THE USER PROVIDES AN INPUT
            if len(answer) < 1:
                continue

            # IF YES, PROCEED WITH THE EFILING
            if answer in "Aa":
                print('\n')
                self.dm_imm = self.algo.imm
                self.dm_lname = self.algo.lastname
                self.input.get_alt_email()
                self.dm_alt_email = self.input.c.secondary_emails[self.input.alt_email]

                break
            # IF NO, GET THE APPLICANT INFO FROM THE USER MANUALLY
            elif answer in "Bb":
                self.input.get_input()
                self.dm_imm = self.input.court_no
                self.dm_lname = self.input.app_last_name
                self.dm_alt_email = self.input.c.secondary_emails[self.input.alt_email]

                break

            else:
                print("\nPlease select one of the options\n")
                continue
