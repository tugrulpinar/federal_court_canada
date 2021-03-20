from pdfminer.high_level import extract_text


class SubmissionRecognizer:
    def __init__(self):
        self.imm = None
        self.lastname = None

    def extract_keys(self, file_path):
        file_path = file_path + ".pdf"
        # EXTRACT THE TEXT OUT OF THE PDF FILE
        text = extract_text(file_path, page_numbers=[0])

        # GET THE SECTION WE WANT - THE UPPER PART
        section = text.split("and")[0]
        trial = section.split('\n')

        words = []

        for item in trial:
            item = item.strip()
            try:
                if item[0].isalpha():
                    words.append(item)
            except:
                pass

        del trial

        redundants = [
            "FEDERAL",
            "B E T",
            "Applicant",
            "BET"
        ]

        temp = []
        for idx, val in enumerate(words):
            for item in redundants:
                if item in val:
                    temp.append(idx)

        counter = 0
        for x in temp:
            words.pop(x-counter)
            counter += 1

        del temp

        imm_no = words[0].split("IMM")[1]
        self.imm = "IMM"+imm_no
        # print(f"\nIMM number: {self.imm}")
        name_chunks = words[1].split(" ")
        self.lastname = name_chunks[-1]
        # print(f"\nApplicant Lastname: {self.lastname}")
