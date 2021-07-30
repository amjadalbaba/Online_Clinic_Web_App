PROJECT REPORT



   LEBANESE UNIVERSITY
     FACULTY OF TECHNOLOGY
     
Topic:

Online Clinic Portal Web Application Project 

BY:

Amjad El-Baba
DOCTORS:
Dr. Shadi Khawandi



Academic Year(2020-2021)
CONTENTS

1) Project Main Purpose							      
2) Web Applications Frameworks					      
3) Intro to Django Backend Framework 				      
4) Definition of a DBMS			  				      
5) Definition of a Class diagram						    
6) Project Class diagram 							    
7) Database Structure Explanation 					    
8) Application Pages and Functionalities				    
   i. Home Page							    
   ii. Sign-up Pages							    
   iii. Sign-in Pages							    
   iv. Patient dashboard and its components              
   v. Doctor dashboard and its components               

9) Security Restrictions						    
10) Summary									    







Project Main Purpose

As the world moves onto a digital space in a wider aspect, the need for physical presence for consultation will become redundant. From meetings to classes, most interpersonal interactions can take place online through video conferencing. In fact, recently even court hearings have moved online. This sets the stage for adapting a critical aspect of our lives to web portals; healthcare.

At some point in our lives we feel the need to consult a doctor for some ailment or the other. Then comes the hassle of getting an appointment and long waits at the clinic. All that can be avoided with a unique web designing project idea of an online clinic.

The main objective of this project is to build a web application that can potentially match a patient with the particular clinic specialist and can have a virtual consultation with diagnosis and prescription handed over virtually.

The main purpose is to make peopleÕs life easier in a way of transforming our life into a totally digital life and way of living.


Web Applications Frameworks

Starting from the very beginning, we will dive into the subject gradually step-by-step. So the first of such steps is to understand what framework means.

Framework is a tool, which makes developer life much easier. We will explain why. Imagine you have to generate application or software, how are you going to start? You will probably need some structure, tools and components. That is what a framework about.

FrameworkÊis a platform for software and applications development. In other words, with the help of its functions and components framework is aimed to improve new software creation.

Web applications: the access is available through web browser. Web applications are usually written in several languages like CSS, JavaScript and HTML. The main benefits are:

* they are rather light and require little device memory.
* userÕs data is saved on the server and you can access it everywhere if you have internet connection.

All web apps were mainly built around servers. Such apps still exist and are highly secure, since their entire app logic is stored on the backend.
But as web standards began to change, app logic started to shift toward the client, which helped to ensure a smarter interaction between a user and a web app. With the logic on its side, a client can instantly react to user input. WhatÕs more, client-side logic makes apps responsive, so they are easy to navigate on any device.
This way, we now have two groups of web application frameworks: one helps to set up app logic on the server, the other Ð on the client. To create a powerful web app, you can use both of them simultaneously.

There are several server-side web application frameworks such as:

   * Laravel (PHP)
   * Django (Python)
   * ASP.NET (C#)
   * Node.js (JavaScript)
   * 
By using either of these server-side web application frameworks, you let it handle HTTP requests, database control and management, as well as URL mapping. You can also render view data with a server.




Intro to Django Backend Framework

Web development became popular due to the widespread accessibility of the web, especially for commerce. Once businesses quickly realized they could offer their products and services on the web, this created a demand for web development that has never slowed down.

Web development can be divided into three major parts:

* Backend development: This is concerned with business logic, data storage, and processing.
* Frontend development: This is concerned with how the user interacts with the system and mainly includes user experience (UX) and user interface (UI) design.
* API/middleware development: This is concerned with how the backend and frontend apps communicate.

We will explore developing web apps using the Python framework Django. This framework mainly addresses backend and API/middleware development. It is therefore assumed that you have at leastÊintermediateÊlevel knowledge in Python.

Web development in Python picked up to bring the data wrangling and processing power of Python to the web. Some popular sites built on Python/Django include Disqus, Instagram, and Mozilla, among others.

DjangoÊis an open-source framework forÊbackendÊweb applications based on Python Ñ one of the top web development languages. Its main goals are simplicity, flexibility, reliability, and scalability.



Django Essential Components:

* App.py: Where app configurations are defined.
* Admin.py: Where model configurations are defined in relation to the project admin page.
* Models.py: Where database tables are defined as models.
* Views.py: Where Django views are defined. These are objects that define how content is displayed on a web page.
* Urls.py: Where Django routes and URL patterns are defined. 
* Settings.py: Which is the app configuration file.
* Forms.py: Where we assign models and itÕs fields to forms.

Also, Django is one of the frameworks that allows a developer to deal with different kinds of technology other than web apps, for example:
* Machine Learning
* Data Science
* Data Analysis
As a conclusion, Django is one of the most popular frameworks nowadays, since it gives a wide range of services considering different fields.



Definition of a DBMS

A database management system (DBMS) is system software for creating and managingÊdatabases. A DBMS makes it possible for end users to create, protect, read, update and delete data in a database. The most prevalent type ofÊdata managementÊplatform, the DBMS essentially serves as an interface between databases and end users or application programs, ensuring thatÊdata is consistently organized and remains easily accessible.

What does a DMBS do?

The DBMS manages the data; the database engine allows data to be accessed, locked and modified; and the databaseÊschemaÊdefines the database's logical structure. These three foundational elements help provide concurrency, security,Êdata integrityÊand uniform data administration procedures. Typical database administration tasks the DBMS supports includeÊchange management, performance monitoring and tuning, security, and backup andÊrecovery. Most database management systems are also responsible for automatedÊrollbacksÊand restarts as well as loggingÊand auditing of activity in databases and the applications that access them.
The DBMS provides a centralized view of data that can be accessed by multiple users, from multiple locations, in a controlled manner. A DBMS can limit what data the end user sees, as well as how that end user can view the data, providing many views of a single database schema. End users and software programs are free from having to understand where the data is physically located or on what type of storage media it resides because the DBMS handles all requests.
The DBMS can offer both logical and physical data independence. This means it can protect users and applications from needing to know where data is stored or being concerned about changes to the physical structure of data. As long as programs use the application programming interface (API) for the database that the DBMS provides, developers won't have to modify programs just because changes have been made to the database.



Definition of a Class diagram
Class diagram is a static diagram. It represents the static view of an application. Class diagram is not only used for visualizing, describing, and documenting different aspects of a system but also for constructing executable code of the software application.
Class diagram describes the attributes and operations of a class and also the constraints imposed on the system. The class diagrams are widely used in the modeling of object oriented systems because they are the only UML diagrams, which can be mapped directly with object-oriented languages.
Class diagram shows a collection of classes, interfaces, associations, collaborations, and constraints. It is also known as a structural diagram.

What is the purpose of Class Diagrams?


The purpose of class diagram is to model the static view of an application. Class diagrams are the only diagrams which can be directly mapped with object-oriented languages and thus widely used at the time of construction.




Project Class Diagram
This class diagram simplifies the way of how project database structure was built and the type of relationship between each of the tables:




Database Structure Explanation

1. User:
Here we have the common fields between the two doctor and patient models, so we can simplify and create a well, cleaned and organized database.

Plus, this model is a main part of the Django authentication system, so any user have his last login info and when it was created and if the user is active or not.

2. Doctor:
   This model describes each doctor information which  differs from User model such as:
   * DoctorÕs identity number described by: ID
   * Speciality of a doctor which describes his/her major described as: SPECIALITY_NAME(FK on table Speciality).
   * The user for whom the doctor belongs to described as: USER_ID.
3. Patient:
   This model describes each patient information which  differs from User model such as:
   * PatientÕs identity number described by: ID
   * The user for whom the patient belongs to described as: USER_ID.


4. Doctor Schedule:
   In This model, the doctorÕs schedule information of the whole week is defined and it contains:
   * DoctorÕs identity number described by: ID (FK on table Doctor).
   * Starting hour of the day described as: FROM_HOUR.
   * Ending hour of the day described as: TO_HOUR.
   * The week day described as: DayOfWeek.

5. Speciality:
   Here we have the doctorÕs major or speciality of his/her field of study and experience described by:
   * Speciality identity number described by: ID.
   * Name of the speciality described as: SPECIALITY_NAME.
   * The description of a speciality described as: DESCRIPTION.


6. Appointments:
   Here we have the doctor's major or speciality of his/her field of study and experience described by:
   * DoctorÕs identity number described by: ID (FK on table Doctor).
   * PatientÕs identity number described by: ID (FK on table Patient).
   * Starting hour of the taken appointment described as: FROM_HOUR.
   * Ending hour of the taken appointment described as: TO_HOUR.
   * Day  of the appointment described as: DAY.
   * A sign showing if an appointment has been prescribed by a doctor described as: CHECKPRESCRIPT.
   * Lastly a field  showing details regarding the main purpose of the appointment which is the description described as: DESCRIPTION.

7. Consultation:
   In This model,  we have the step just after taking an appointment which is the result of it  described by:
   * Appointment identity number described by: ID (FK on table Appointment).
   * Prescription field  showing details regarding the doctorÕs overview of a taken appointment described as: PRESCRIPTION.
   * The assigned drug(s) by a doctor described as: DRUGNAME.
   * And lastly the price of a prescription described as: PRICE.
   8. NOTICES:
   The main purpose of this model  is to inform a patient or a doctor when they an appointment is been canceled described by:
   * Doctor or Patient identity number described as: DOCTOR_ID (FK on table Doctor) or PATIENT_ID (FK on table Patient).
   * Content field  showing what a notice message contains described as: CONTENT.
   * When a message was sent described as: SENT_AT.








Application Pages and Functionalities

This application contains different pages each having its own functionalities and its own way of dealing with databases models and backend implementations that will be discussed in details.

Django comes with a templates that are called ÒpagesÓ of an application. It lets you handle HTML content in a templates and handles the management of its content in django views in views.py file and a Python API. A page is an object with a URL, title and content.

And every page has its own route that is assigned in urls.py.







Welcome Page

First of all, a welcome page is displayed to the user with a welcome message and 4 different options:

* Sign-In as a doctor: if the user have an existing account.

* Sign-In as a patient: if the user have an existing account. 

* Register as a Doctor: Here when a user donÕt have an account and he is a new doctor. 

* Register as a Patient: Here when a user donÕt have an account and he is a new patient. 


DoctorÕs Sign-Up Page

In the registration page, the doctor should enter his private information such as: 

   * The username
   * First and last names
   * Home address
   * Phone number
   * The Email Address
   * The speciality with respect to his major and field of study
   * Gender (M/F)
   * And lastly the password and confirmation password




If any incorrect entry is written by the user, a message of the error will be displayed.

1. Regarding the email input, the app checks if the email exists and if yes, a message will be displayed else the registration will complete successfully.

2. The same methodology is applied regarding the password and confirm password inputs.

3. The userÕs password is saved in an encrypted way in the database (PBKDF2) by default.
PatientÕs Sign-Up Page

In the registration page of a patient, same fields appears except the speciality field, the patient should enter his private information such as: 
   * The username
   * First and last names
   * Home address
   * Phone number
   * The Email Address
   * Gender (M/F)
   * And lastly the password and confirmation password









Doctor and Patient Sign-In Pages

Regardless the user is a doctor or a patient must enter a correct credentials in order to access the dashboard, which are:
* Email
* Password
A request is sent into the back-end and here is the rule of Django Authentication System which checks the email if it exists and if the existing password in the database matched the entered password after applying the necessary built-in algorithm.





Patient's Dashboard



The following dashboard is composed of 5 main parts:
   * The Welcome message 

   * Alerts to inform the patient if an appointment is canceled

   * Amount of total appointments taken by a patient

   * Amount of prescribed appointments by a doctor taken by a patient

   * The table of appointments showing the day of a certain appointment, the starting hour, ending hour, the doctor name who is responsible for the appointment         prescription and lastly the action, which allows the patient to view his prescription if its available or it will show pending if the appointment is not yet prescribed, also there is a Cancel Appointment Option if a patient wants to remove an appointment, with a confirmation message.



When the patient clicks on the Take Appointment button, a form appears. This form includes the day of the appointment to be chosen, with which doctor the patient wants to make the appointment with, the time of the appointment which will be the free slots filtered for the chosen doctor and a brief description of what the patient is feeling.

After the Add button is pressed a success message will appear to the patient regarding a successful enrollemnt.




When the patient wants to view his appointment info by pressing the View Details button a form will appear to the patient in order to view all the info related as the prescription, drug(s) name and the consultation price.




Doctor's Dashboard



This is the main dashboard setup for each doctor in the clinic.



The following dashboard is composed of 4 main parts:
   * The Welcome message 

   * Alerts to inform the doctor if an appointment is canceled

   * Table containing the weekly schedule of a doctor (this schedule is created for 7 days of a week with a starting and ending time set to 00:00 when the doctor sign-up for the first time)

   * The table of appointments showing the day of a certain appointment, the starting hour, ending hour, the patient name who took the appointment, the description of the current state of this patient and lastly the action, which allows the doctor to assign his prescription, and if the doctor prescribed an appointment a consulted message will appear, so the prescript button will disappear also there is a Cancel Appointment Option if a doctor wants to remove an appointment, with a confirmation message.



When the doctor clicks on the Edit Schedule button, a form appears. This form includes the day (which are from Monday to Sunday) to be filled with the starting and ending hours at a specific day, so the doctor will assign his work range hours in order to allow patients to select an appointment time as mentioned before.






After the Edit button is pressed a success message will appear to the doctor regarding a successful update of his info.

Her itÕs an update because as mentioned above, when the doctorÕs first register, a schedule is created for 7 days of a week with a starting and ending time set to 00:00, so when the doctor edits his info we must update the database from 00:00 to the chosen timestamps.




Lastly, the Prescript button is pressed a form will appear to the doctor in order to allow him to set the prescription details for a certain chosen appointment.



The following form contains:
   * Prescription field: where the doctor will enter his prescription after he overviewed the appointment details and what the patient is feeling

   * Drug Name field: contains the drug(s) that a patient should take in order to feel better and solve his health issues


   * Price field: the pricing of an appointment prescription is in $, so after the doctor check-up, he will assign a suitable price


Security Restrictions

Web application security is a central component of any web-based business. The global nature of the Internet exposes web properties to attack from different locations and various levels of scale and complexity. Web application security deals specifically with the security surrounding websites, web applications and web services such as APIs.

Important steps in protecting web apps from exploitation include using up-to-dateÊencryption, requiring proper authentication, continuously patching discovered vulnerabilities, and having good software development hygiene. The reality is that clever attackers may be able to find vulnerabilities even in a fairly robust security environment, and a holistic security strategy is recommended.

For this reason, and as mentioned before, this application is based on Django Authentication System.

This system is a built-in auth system that deals with every detail considering web app authentication and security, it helps us manage those things easily using its built-in functions and methods.

A main example of a secure navigation in a web app, is when the id of an appointment of a patient being displayed in the url must be only related to this patient so if he change it to one of the appointmentÕs ids not related to him, we must restrict appearing of an appointment related to another patient.

If he chose to view an appointment, the url will appear as follows: http://127.0.0.1:8000/details/13/

The 13 here is the appointment id, and if the patient changes it to another id (20 if we want to say) and this appointment is not set to this patient in the database but related to another patient, an error message will occur: No Such Appointment




Summary

Any company willing to achieve maximum success in its industry should have its own online representation. And healthcare organizations are no exception to this rule.Ê
AÊmedical web resource plays a significant part: it affects the reputation of the clinic, the effectiveness of treatment, and much more.
However, a few questions remain... how to create an appealingÊhospital website design? Can your platform be profitable? How to make your website work in full force? Let's consider these and other issues in order of importance.
More and more people choose a clinic with the help of famous Google or other search engines (in other words, resorting to the Internet). Moreover, before making an appointment with a doctor, your potential patient will definitely visit the site he likes and studies all the information it provides. So aÊhospital web resource is currently one of the most significant channels of sales of medical services and related products.Ê


As you can see, according to statistics,Êmedical information websites rank second on the list of leading sources, which provide specific data about a healthcare condition. And itÕs one more factor pointing that you should build your hospital web resource. And although it seems to be obvious, let's allot out 5 main reasons why your clinic must have a site.








