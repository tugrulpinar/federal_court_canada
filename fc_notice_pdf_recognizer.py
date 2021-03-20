from pdfminer.high_level import extract_text


class PdfRecognizer:
    def __init__(self):
        self.applicant_list = []
        self.applicant_names = []
        self.applicant_lastnames = []
        self.application_type = None
        self.number_of_applicants = None
        self.file = "App. for Leave.pdf"

    def scan_pdf(self):
        self.__extract_fullnames()
        self.__extract_application_type()

    def __extract_fullnames(self):
        try:
            # EXTRACT THE TEXT OUT OF THE PDF FILE
            text = extract_text(self.file, page_numbers=[0])

            # GET THE SECTION WE WANT - THE UPPER PART
            section = text.split("and")[0]
            chunks = section.split('\n')

            slicer = None
            for idx, val in enumerate(chunks):
                if val.strip() == "And":
                    slicer = idx

            del chunks[slicer:]

            for item in chunks:
                item = item.strip()
                try:
                    if item[0].isalpha():
                        self.applicant_list.append(item)
                except:
                    pass

            del chunks

            # DEFINE THE WORDS THAT YOU WANT TO REMOVE
            redundants = [
                "Registry",
                "FEDERAL",
                "B E T",
                "Applicant",
                "BET",
                "Bet",
                "Court",
            ]

            temp = []
            # IDENTIFY THE INDEXES THAT BEARS THE REDUNDANT WORDS INSIDE
            for idx, val in enumerate(self.applicant_list):
                for item in redundants:
                    if item in val:
                        temp.append(idx)

            counter = 0
            # REMOVE THE IDENTIFIED INDEXES
            for x in temp:
                self.applicant_list.pop(x-counter)
                counter += 1

            del temp

            if len(self.applicant_list) > 6:
                print("\nTHERE MIGHT BE AN ERROR\n")

            # print(applicant_list)
            print(f"\n{len(self.applicant_list)} Applicant(s) in total.\n")
            self.number_of_applicants = len(self.applicant_list)

            for applicant in self.applicant_list:
                full_name = applicant.split(' ')
                self.applicant_lastnames.append(full_name[-1])
                full_name.pop()
                name = ""
                for names in full_name:
                    name += names + " "
                self.applicant_names.append(name.strip())

            for x in range(1, len(self.applicant_list)+1):
                print(f"Applicant{x} Name: {self.applicant_names[x-1]}")
                print(
                    f"Applicant{x} Lastname: {self.applicant_lastnames[x-1]}\n")

        except:
            print("\nEither there is no 'App. for Leave.pdf' file in the directory OR I can not recognize text in the file.\n")

    def __extract_application_type(self):
        try:
            text = extract_text(self.file, page_numbers=[1])
            if "Appeal" in text:
                print("\nPDF scan result: RAD Appeal\n")
                self.application_type = "b"
            elif "Protection Division" in text:
                print("\nPDF scan result: RPD Appeal\n")
                self.application_type = "a"
            elif "PRRA" in text:
                print("\nPDF scan result: PRRA Appeal\n")
                self.application_type = "c"
            elif "H&C" in text:
                print("\nPDF scan result: H&C Appeal\n")
                self.application_type = "d"
        except:
            print("\nSorry, I cannot read the second page.\n")
            pass
