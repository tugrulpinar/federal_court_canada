# federal_court_canada
Automate Judicial Review Applications and Submissions

This project allows user to file different types of documents to the Federal Court of Canada with minimum ease, speed, and of course minimum key strokes.

Once user provides the type of the document to be submitted to the Court, the program will scan the PDF file and identify the information needed to make the submission (i.e. file number, lastname, type of application)
Then browser will open and the program will hanlde everything in the F.C. e-file portal within secons.
Once the submission is confirmed on by the e-filing portal, the program will parse the HTML content of the confirmation page and collect the Confirmation Number. If it can not collect it, it will notify that the file has not been submitted succesfully.
The program then will create an excel file and start logging the details about the submission depending on the type of the same such as, date filed, due date, full name.
Finally, the porgram will create a folder with client's lastname and move documents that are submitted into there.
