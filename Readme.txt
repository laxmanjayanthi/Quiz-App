Tools and Technologies:

Platform				-	Django
Programming Language			-	Python
Frontend 				-	HTML, CSS, JS
Database				-	SQLite 
BackgroundImage refernces		-	From Google images

------------------------------------------------------------------------------------------------------

User side - 

	Home/Welcome page : 	http://127.0.0.1:8000/

	This quiz consists of 10 questions (Python mcq's).
	Instructions for the quiz are available in home page 
	By clicking on attempt quiz on home page the page will redirect the user to quiz page

	Quiz page : 		http://127.0.0.1:8000/quiz

	User have to click submit question after choosing an option for every question and then click next. 
	After submitting the quiz score will be displayed. 

	Result page: 		http://127.0.0.1:8000/result

	I have considered the good mark as 6 and above in this quiz .
	If a student is awarded with a total of 7 or above "Hurray!! You've passed the test" message will get displayed with two happy emojis ahead of the meassage.
	In all other cases "Better luck next time" message will get displayed with a neutral face emoji ahead of the message.
	A link for accessing all the answers is available in the result page as "click here for the answers".

	Answers page: 		http://127.0.0.1:8000/answers
  

Adminitrator side - 

	Admin page: 		http://127.0.0.1:8000/admin

	A model named "Questions" is available in the admin page where we can add the question and 4 choices and we have to specify the answer in the answer column.

	Snapshot of the tables from the database (pgAdmin 4) has been attatched in the submission.
