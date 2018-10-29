### View all of my Projectworks - click over here -> [Vivek Vellaiyappan Project Works](https://github.com/vivekVells/VivekVellaiyappanProjectWorks)

# Presentation-Evaluation-Tool
A Progressive Secure Web Application to evaluate the Presenter's presentation skills by peers and professor

### Project Working Demo
- [Video Link](https://drive.google.com/open?id=13AzwiiyqGelA-GXrr3fCDm-0DwkWvvty)
- [Working Demo - GIF](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20App%20Demo%20-%20Version%201.gif)
- [Working Demo - PDF](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool.pdf)
- [Working Demo Files](https://github.com/vivekVells/Presentation-Evaluation-Tool/tree/master/demo)
### Objective
- To reduce professor’s time consumption for his presentation evaluation works
### Issue to solve
- Professor uses the paper to evaluate the presenters' presentation skills. Because of this few issues such as over consumption of time (printing out, distributing and retrieving the feedbacks, etc), resource usage (money to buy paper, printer machine), labor (to manually calculate the total and input them into professor's marksheet maintenance document for grading) was found. - to solve this issue, this web application is used.
### How this application resolved the issue
- Now, peer-to-peer presentation evaluation becomes easy by simply logging into the website and reviewing each other. Also, professor can just retrieve the total scores and analyze the score patterns of the students
### Security Feature
- All the evaluated information will be stored after doing AES encryption using professor's password as key. 
- SHA256 being used for password matching
### Tech Involved  
- Frontend languages, Python, Django, sqllite3, SHA2, AES
### Features
- Root admin is "App Admin" who can register professor's credentials
- Professor can enroll his/her students by using their college email ID
- Students can login and perform either of the following
  - Review Other Peers' presentation
  - Review the received evaluation remarks from others 
### Future Code
- Enhancement tweaks
- Make data visualization features such as Charts and graphs
- Data analysis over the evaluated scores of the students
- To download the scores in files such as image, pdfs,..
### Instructions to run this code in your machine:
#### In console (Tested in Windows using GitBash cmd) - follow the steps
- Step 1: Make sure Python setup is available in your machine (coded when python was on version 3.6.2) & do django version as 2.0.3
- Step 2: Open console command prompt or gitbash (I love git bash. Try this one)
- Step 3: Pull this code to your machine and run it (Install git and use git bash for the followings) (you could also do git clone and proceed from Step 3.4)
  - Step 3.1: Create a folder and do 
    - **git init**
  - Step 3.2: Add this repo as your remote origin 
    - **git remote add origin https://github.com/vivekVells/Presentation-Evaluation-Tool**
  - Step 3.3: Pull the code in this repo to your remote origin 
    - **git pull origin master**   
  - Step 3.4: Move to the directory 'website\django\presenterevaluation'    
  - Step 3.5: Make migrations and migrate
    - **$ python manage.py migrate --run-syncdb**
  - Step 3.6: Run the server 
    - **$ python manage.py runserver**
- Step 4: Create new superuser and login there to view how the data being stored in the db 
    - **$ python manage.py createsuperuser**
    - give username and password
- Step 4: goto port link: http://127.0.0.1:8000/admin - for admin dashboard where you can view/modify the db backend values (username: username_you_gave_above | password: password_you_gave_above)    
- Step 5: goto port link: http://127.0.0.1:8000/appadmin - (values are already added) for appadmin (username: appadmin | password: appadmin)
- Step 6: goto port link: http://127.0.0.1:8000/professorlogin - (values are already added - 'professor' table) for professor login (create new one using step 4 above in 'professor' table above)
- Step 7: goto port link: http://127.0.0.1:8000/studentlogin - (values are already added - 'student' table) 2 students are preadded. v@m.edu with password v123 and k@m.edu with password k123
- Step 8: login using any student login credentials in step 7 and play around. thats' it. you will be able to figure out easily.
## App Working Functionality Previews
### Preview 
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20App%20Demo%20-%20Version%201.gif)
### Images (lots of scrolling ahead - this is available in pdf format in /demo folder. checkout that if you want)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/1.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/2.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/3.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/4.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/5.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/6.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/7.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/8.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/9.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/10.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/11.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/12.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/13.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/14.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/15.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/16.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/17.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/18.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/19.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/20.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/21.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/22.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/23.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/24.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/25.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/26.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/27.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/28.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/29.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/30.JPG)
![](https://github.com/vivekVells/Presentation-Evaluation-Tool/blob/master/demo/Presentation%20Evaluation%20Tool%20-%20PPT%20Images/31.JPG)

Thank you for spending your time! Have a good day!
