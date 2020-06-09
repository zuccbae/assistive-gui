 
The Ongoing Quest for Accessibility in the 21st Century
A REPORT ON THE CREATION OF THE VERTIGO ASSISTIVE EYE; A NEW TECHNOLOGY TO SUPPORT THOSE WITH MOTOR SKILL PROBLEMS
 

  
Abstract
This project aims to demonstrate the creation of a software, which is a self-contained GUI that includes the use of a keyboard, mouse and research resources, which are in part gaze controlled. This technology is aimed at those who are students and would need assistance when doing e-learning. This is through the use of OpenCV and machine learning, tkinter and the language Python. The aim of the project would be so that students who struggle because of certain conditions, such as paralysis, limited movement and motor-skill disorders can use computers and learning resources. The goal of this dissertation is not only to demonstrate the end product but also to educate about those who in the technological era are normally left behind, generally due to technological faults and also social-economic factors which could hinder many from access to assistive technology.
The entire software is based on the user’s web camera, it is used as a means to track eye direction and movement.
The software comes with many parts and will also be built into a single GUI. Although, this project demonstrates understanding, I would hope that in the future this GUI would have more dynamic movement of the mouse to increase the possibility of a smoother experience when using it.



















Contents
Abstract	1
Introduction	3
Methodologies	4
Planning	5
Waterfall Charts	6
Risk Analysis and Contingency Planning	6
Literature Review	8
Target Audience	8
Background Research	9
Requirements	11
Design and Development of the Vertigo Assistive Eye	17
Product Description	20
Legality and Ethics	46
Evaluation and Testing	47
Critical Review	48
Conclusion & Future Developments	49
References	49
Appendix	51
Meetings	52
Video Learning/E-learning (YouTube)	53
Figures	54
Abbreviations	59










Introduction
With the quick advancements of technology come the inevitability of certain groups not being able to catch up. This is especially true for specific marginalised groups who generally need more support when it comes to technology. There is a problem with accessibility in the modern technological era. Technology for people who suffer with paralysis, struggle to use technology due to old age and those who have learning difficulties is generally extremely expensive and outdated. Adding to this, Assistive technology has an abandonment rate of 50% (Lauer, 2020). One factor of this high rate is due to the poor consideration that creators have on development and design when it comes to human limitations in disability. This rate of discontinuance proves that there is a problem with software development, despite the movement to more inclusive technology. Unfortunately, due to their low socioeconomic statuses the majority of people who need to use assistive technology where only 1 in 10 have access to it due to this reason (WHO, 2018). The unmet need for assistive technology does not only stop at software but for websites, as of 2018 less than 10% of websites are accessible (Christopherson, 2018). 
The aim of assistive technology is to enhance the physical capabilities of the user. Already, we have seen inclusive technology encroach on general technology such as auto-correct, auto-capitalise and auto complete features, when sending text messages and even now with writing emails on the desktop with Grammarly. We are now seeing the necessity of such applications as according to the World Literacy Foundation, as many as 60% of adults in the United States alone suffer from an undiagnosed LD (WLF, 2020). This demonstrates the need for wider use of assistive technology as some people may not even know that they need it.
My technology and all of the future developments of it will ensure that the users who suffer from extreme physical debilitating conditions would not be neglected when it comes to having a similar user experience to their peers who are able-bodied, it would increase independence as they would be able to use the software alone. Also, it will ensure that those who sincerely struggle with illiteracy get the support they need when it comes to learning and e-learning. 
I have taken into consideration the complexity of many different disabilities and ailments and I have created a diagram of the things that could be grouped together (Figure 1). I have decided it is best to create a catch all situation or a utilitarian approach where most of the common needs will be met in a single GUI. There are many contingencies with this approach as it is important to heavily compensate for certain disabilities over others. This will also mean that my software is both accessible and assistive (PeatWorks, 2020).
I have called the name of my software the Vertigo Assistive Eye, I have created this project to be based on multiple separate projects. I have brought together a splash screen with a start, instructions and quit buttons. Keyboard and output on an A4 size page, created my own eye tracker from another project, brought in web viewers and also incorporated a first person view to keep the user in frame (Figure 2). Incorporating all of these individual projects into one project would create the perfect software for a person has certain disabilities. Everything needed for e-learning is all in the same place while all having a simplistic design for all people to use. This software could be for those who have LIS and can only use their eyes (NORD, 2020) to those who have arthritis and struggle to use the computer for long periods of time. Essentially it has all the required needs for a student in this position as with development it will be good for long writing tasks (Dystonia Canada, 2015). 
This project also aims to help those who could potentially have LD’s and who also need a simple learning environments to help them progress, for example, autism sufferers need simplistic routines to follow (National Autistic Society, 2017). It is also one of the ten design heuristics for UID ‘consistency and standards’ (Nielsen, 1994), to have a technology which demonstrates that the user has some form of prior knowledge of the software to make it overall easier to use.
I based this project on a module I did last year on image processing in MATLAB. They are both similar languages having similar areas of being functional languages. Overall, this would result in a project which is technically moderate.
I will evaluate my project against the future considerations that I have for it, the deliverables versus the requirements. 
The key objectives of the Vertigo Assistive Eye are:
•	Support the daily life of a paralysis victim through allowing them to surf the internet and perform long writing tasks
•	Increase the quality of life of the sufferers of paralysis 
•	Increase independence and reduce reliance on others to make searches for them
•	Allow them to explore the basic human right of using the internet
•	Increase their wellbeing
•	Having an equal living experience
•	Receive additional support when using the internet and a computer in general
•	Gives them an open option to explore education and leisure activities online
This would also reduce the amount of strain that was once on their caregivers and or family members as the users will now be able to: 
•	Allow the person in care to have more privacy and be independent when shopping and searching for themselves
•	Reducing the reliance needed on the caregiver or the family member
•	Allows for the caregiver to have more free time on other duties for the user
There would be a combination of two or more interfaces in the final product, this is because there would be different levels of support needed when it comes to dealing with different types of paralysis and disabilities.
The aim of the Vertigo Assistive Eye is to be a stable environment for continuous long writing tasks and web-surfing and even e-commerce and use in the classroom for the future.
Methodologies
The methodology I decided to implement was the waterfall methodology, this is a linear type of creation where tasks are done one after the other. The reason why waterfall why waterfall is effective is because you can finish whole tasks and make sure they are in working order before moving on to the next task. Waterfall is not as dynamic as agile, and as someone who does multiple tasks at once but never finishes any individual task; a believed that this would be the best method for me as I can produce some parts of a completed deliverable if I cannot produce the whole thing. The GUI came with four tasks, the eye tracker mouse, the keyboard, the camera and the web viewers. Creating the individual items was easy, however their implementation into a single GUI is what I heavily underestimated as incorporating Tkinter/tkinter and OpenCV into the same GUI takes a lot of practise. The waterfall has another positive which would be to allow for anyone to join at any point of the project as documentation is being done at one given time. Waterfall was perfect for this project as it ensured that I had all my individual elements completed before I incorporated them together.
There are some small areas in my work where I believe that agile could have been a better approach. Agile takes into consideration that a project is dynamic, which is how it normally is in the real world, and that the stakeholders could have new ideas to implement at any given time. Demands are constantly changing, and it is important for them to be met. I saw the importance to outline all my requirements in a table before working on my deliverable to ensure that areas of my project will be met. Agile is much more efficient in a team; small groups of people can work on specific things however I am only one person. I would have to work on all my bug fixes alone therefore it would be better to finish a part of the program and debug it before moving on to the next part of the deliverable.
The scrum methodology is one which can be properly integrated into my chosen waterfall technique. It contains a more detailed version of all the tasks that have to be done. It also includes the hours spent on those tasks. Each sprint for me lasted around three weeks and longer. They would allow for the developer to be reflective on their work. At the end, and all the challenges that were faced during that time would be reflected on.
I have decided to use the waterfall method and also, I have decided to incorporate some detailed sprints for each subtask. This should have the best outcome for me as I can finish one task at a time so even though it may be possible that I do not have a complete deliverable I have individual parts of the project completed. 
Planning 
Now that I have all the information that I needed I could create sprints. The evaluation of my previous steps would allow me to create a GUI which would rarely leave out important detail which is necessary to make assistive technology effective. I have included images of the Waterfall chart that included all my tasks that I had to follow in order to get the project completed. I have provided the full waterfall chart in the chapter called Waterfall Charts. 
Honestly, it was difficult to stick to the original chart that I had planned to. Unfortunately, there were many family and life events that hindered my progress in my modules in university. I also have a weakened immune system and I felt unwell during the pandemic, also I could not work for two weeks as a flood in my house had destroyed my computer. The code was saved however due to the different aspect ratio of the new computer, which was given to me, some areas of my code found it difficult to adjust which lead to me having to do it again. I suffered a fall early in the year and it meant that I could not see my supervisors. There were many reasons why the progress of my work was hindered, and I couldn’t foresee many things. In total This is why it is important to have contingency planning.
My expected finish time among other things because of this became somewhat unrealistic. Luckily, I had some things put in place so that I wouldn’t be completely rushing at the last moment for example getting my literature review, my methodology and requirements dome in January so I will not be rushing at the last moment.  I found myself, due to a compilation of other things to be very behind and constantly going over my estimated times. Although the majority of what I wanted to do was successful there was a large difficulty when placing everything into the GUI. Although I am confident in my waterfall approach, I see where it could have clearly come with a different result this would be because without outlining the requirements prior to the software creation it would the depth of study into the software would not be demonstrated.
I have demonstrated my entire waterfall method; in this I have included the length for certain tasks. I have also left a small description for the user story which is important for planning. I have also included an honest completion date for the deliverables and the user story. As you can see it has large differences compared to what was planned. This would be because of poor oversight from the risk analysis and contingency planning, in the future I would know how to better implement the contingencies and risks in order to have a project which would be finished without stress.
Waterfall Charts
 
Risk Analysis and Contingency Planning
Throughout the course of this project, it is fair to say I fell into many holes when it came to the risks. Every potential risk which could have possibly happened did happen, and it caused me to struggle a lot in my final year. I have added an extra column to this table below to show if the risk did happen and how it affected my work.
Risk	Possibility of happening (1-5)	Contingency	Did this happen? (Y/N)	How it impacted my work.
Work loss	2	If I lose my work, I will be behind on my project. I will make save files for every update and advancement of work that I would do.	Y	A flood destroyed all of my save files and left me without a computer for a few weeks, because of this I was behind on my work.  I had lost the whole optical aspect of my dissertation.
Illness	3	I have a weakened immune system and therefore I am more prone to sicknesses, I did the bulk of my work in December to avoid missing work	Y	During November and May I caught the flu, in May it was more difficult as it was closer to the deadline. I missed another 4 weeks of work in total.
Personal Circumstances	2	Unplanned family events would cause a disruption to my work as I would have to take time to mediate for my family.	Y	I had to mediate and support my mother during an ongoing situation which started in December. Because of this I made limited progress on my project. My other modules were affected too.
Travel	1	Having back-ups at home could be useful due to hardware failures in the university. It would be better to save all work at home in the case I couldn’t travel to the university.	Y	COVID-19 lead to travel to the university not being allowed. I was lucky to have backups at home, but they were destroyed.
Hardware and server failures in Brighton University	1	The system could be down, and it would be difficult for me to upload any of the work that I wanted to.	N	This has not impacted my work.
Copyright	3	Using pieces of code could translate into copyright issues from the university, making some parts of code by myself is hard as I felt as if I did not know enough.	N	I researched enough and was able to use different pieces of code to make my own GUI!



Literature Review
Target Audience
The main target audience for this application would be students with motor skill issues, LDs and paralysis. It limits and reduces the difficulty for prolonged computer use and has a very simple interface that people who have LDs can use easily.
The GUI encourages use for long writing tasks and helps to remove the hinderance of a disability when it comes to a traditional schooling environment. With the use of innovative computer vision computer usage can be dynamic without being straining.
My software aims to benefit more people than its target, however. Others who can benefit are those with limited muscle movement, for example, arthritis. Sufferers generally struggle to comfortably use a computer for prolonged period of time. Quadriplegics and also those with LIS could also benefit. LIS is on the more extreme end of those who suffer with paralysis, not only do they have limited to no control over their limbs, they also have limited control over their features however they can only move and have full control over their eyes.
Certain features of the Vertigo Assistive Eye would be perfect for those who suffer from LIS, this software has gaze control which could allow the user to perform long writing tasks with an output into a console. The webcam is trained to find and track the pupil’s location in relation to the screen. Which would mean it would be easy to select a specific key that a person is looking at without the use of a keyboard or a mouse in the physical world. 
Although it is not completely gaze control is not perfectly developed this is the first of many features which could be helpful for those with this ailment. Future developments of this software would show that it would have capabilities such as surfing the web and watching videos with only the movement of the eye. This would be more helpful and an bring the users closer to the initial aim, which is to ensure that the users have a living experience which is as close and as similar to their able-bodied peers as possible.
Good assistive technology research is essential for the development for future technologies, so it is necessary to gain a in depth understanding when it comes to engagement with this issue. I imagine that there is a large gap in the literature when it comes to the exploration of free eye tracking software  I would be combining and developing previous technologies further, I believe that there are multiple good merits with many types of assistive technology in this field however there are some areas which are lacking and others which are unnecessary. I believe with the creation of the Vertigo Assistive Eye the gaps that previous assistive technologies have left will be filled. Overall, I hope that a new understanding of this topic will soon be reached, and that would be the creation of a better catch all system that recognizes people with more extreme paralysis and disabilities and would also force companies to implement better assistive technologies to help such people. As everyone deserves to be supported in their life journeys no matter the point that they start at.
The Vertigo Assistive Eye is assistive technology therefore the target audience is clear. However, this is not to say that all people including those who do not suffer from physical paralysis should be restricted from using this product. Assistive technology is for people who struggle, this would mean extra help for people who have learning difficulties, old people who generally need extra assistance when using the internet, young people and people who generally need extra assistance when it comes to using technology. The Vertigo Assistive Eye aims to help all people.
Background Research
My main research into the subject area has shown me that there is a large problem when it comes to creating stable assistive technology. The 50% abandonment rate along with low production and the lack of accessibility in the internet all shows that there is potentially a lack in education in how to make effective assistive technology. All of the software that I have taken inspiration from exists independently, I therefore found the desire to compile them in order to create the self-contained GUI, for the intended purpose of being assistive technology for research. Therefore, I saw the need to educate myself in how to create effective technology, python libraries and previous code examples to make them into a single application, so I could bring my final project together. A successful joining of these individual applications would demonstrate the possibility of an effective assistive software.
I first wanted to see what constitutes for a good user design for assistive technology. It would be one that considers all types of learners, audio; which should have a sound output on click, visual; which should have colour changes on click, kinaesthetic; a way to actively practise on the product and readers/writer; a way to read information and to have an output for it (Fleming, 1987). From this I can plan out the types of outputs I would have which would benefit my software. For example, have the key make a typing noise when it has been clicked to demonstrate it has been struck, have a key change a different colour to show it has been selected, have a dynamic mouse movement and keyboard method which would allow for active practise of the application and lastly a way which would allow for the long writing and reading tasks done by the user. Respectively all of these satisfy the types of learners available. 
I had to then gain understanding of the types of people who would generally need assistive technology. These would be people who have disabilities, those who are aging and would therefore have functional decline, those who have mental health conditions and learning difficulties (WHO, 2018). 
These people would greatly benefit from assistive technology as close the gulf in the development of technology could lead to the health, wellbeing and socio-economic benefits for the user. For example, access to a GUI for students could lead to better results in education and employment for the user. Hearing aids, predictive text and auto-capitalisation could all lead to the improvement of language skills (WHO, 2018).
	However, there are studies to demonstrate that the increase in predictive material could lead to over-reliance and that through the use of machine learning, there would be a movement towards having your conversations become automatic (Selinger, 2015). This could potentially hinder learning. Despite this I see the benefits of having more assistive technology.
The investigation of more assistive technology led me to the NHS, the NRAS, the CDRF and the GBC. All of which explore the necessary conversation around paralysis, motor skill, disorders and the attempt of normalisation on the life of a person who had been affected suddenly with these conditions.
Assistive technology would help to bridge the gap especially for those who require independence. Despite the reliance on the machine, assistive technology could provide an experience which is as suited to a regular living experience as possible. When done correctly assistive technology will not only help but fully enhance the life of the user from injury to independence. This is important as the CDRF reports that the risk of suicides within the first five years of injury is high because of difficulty to adjust. Having assistive technology which can be used universally for all devices before and after paralysis would be helpful for any potential transitions (CDRF, 2020).
Paralysis is an umbrella term which describes the loss of a certain function or functions. Many conditions fall under the umbrella of paralysis and it can range from conditions such as arthritis to more extreme conditions such as LIS, which is where a user loses total control of their body – are quadriplegic- and only have complete use of their eyes. Paralysis can also be early onset and late onset. It could be caused from childhood falls, auto immune disorders and nerve diseases (Cyclone, 2018). 
For those with general motor skill disorders, many find it difficult to complete many tasks as they cave limited or decreasing mobility while doing those tasks (Perlstein, 2019). For example, arthritis is a leading cause of work disability which because of constant computer use, continuous use of the joins will lead to pain inflammation and tenderness. It is important to include assistive technologies on a computer so there will not be a human limitation to a workplace (Wiley-Blackwell, 2009).
Access the internet is considered to be a basic human right, it’s because of the “freedom to connect” rule. The UN declared that nothing should stop the exploration of “key trends, to seek and impart information ideas and kinds of media”. Therefore, it is a limitation of websites and software to be inaccessible as it is limiting the human rights of people who have access to technology, more should be done in order for technology to be effective for the majority of people, internet access disruption should ultimately be condemned (Sandle, 2016).
My GUI would be a steppingstone in the type of self-contained technology which would be good for those with condition which limit their technological usage.
One last problem that I have is that it is proven that gaze trackers can be done cheaply or even for free, this is demonstrated by Abner Araujo, this is an ingenious idea which uses the concepts that I am using however this code is in C++, he has complete control of the mouse and he has created an eye tracker using just the webcam as well. (Araujo, 2017). Understandably people would want to benefit from this, and these passion projects just do not have the same outreach as technology such as mainstream technology does. It is unfair that in order to have the same living experiences there is a clear level of discrimination present. This demonstrates the disregard of people in a lower socioeconomic group when it comes to access of assistive technology. 
According to imotions, eye trackers cost anywhere from $100 for a low-end tracker to $10,000 for a high-end one (Farnsworth, 2019). This is not affordable for everyone, and it is discriminatory as not everyone with disability has or is claiming an extra allowance which would be used to pay for a tracker. With rising rent and bills it would be even more difficult for people to buy commodity such as an eye tracker.






Requirements
Before I had begun to outline my requirements. I did this in my research when producing a product for my deliverable. This all comes down to what the GUI should look like, the type of fonts that it should have and the necessary functionality of the GUI.
I have done this so that can consider all potential factors before making my GUI.
I did this through requirements analysis. This is done in order to collate the information which is used to design, build and test a piece of software. I would have to gather the requirements, analyse the code for them, model the requirement around my view for the GUI and then review the creation. 
I had to consider the functional and non-functional requirements of my software. Functional requirements would be user specific and would be exclusive to the users and their experiences, while non-requirements would be for the final look of the software. 
I used MoSCoW, to show me what the product really needs, the requirements which would be nice to have and those that could be done without because they are excessive and would be done in maybe a future development.
Functional Requirements:
Key: 10, signifies the most important while 1, signifies the least important item to have in the software.
MoSCoW: M – Must have, these are the vital things that it would be difficult to live without.
S – Should have, these are the things that are important but not vital.
C – Could have, these would be the parts of the application that would be nice to have
W – Won’t have, these are the things that although listed would be unnecessary to put in.

Requirements	Description	Significance	MoSCoW	How did my system respond to justify the requirements?
The application should be controllable by eye-gaze	The Vertigo Assistive Eye is an eye-gazing keyboard, it is necessary to have this feature as the point of the keyboard is to provide technological access to those living with paralysis and in particular Locked-In Syndrome  and those that need extra assistance, for example, those with arthritis	10	M	The system is gaze controlled, I can use my eyes to move the mouse either left or right. I can also perform the mouse movements along the x-axis, and I can perform mouse clicks and double mouse clicks.
The application should already be launched and running in the background on computer start	On activation of the computer, the user would need complete usage of all functions, for example, the mouse and the keyboard if the computer has password protection software installed, allowing the Vertigo Assistive Eye to be already running in the background would allow for full functionality to be possible	6	S	This should be active in the future developments of the GUI; the target audience is more specifically for those who have motor skill issues and paralysis and therefore cannot have free and open movement of their bodies because of their conditions.
There would have to be a compromise between the product and the legal issues when it comes to the collection of biometric data and this future aspect of the GUI.
The application should be large enough to be visible but not obtrusive to not cover the entire screen	This is so that the webpage would not be obscured, and readability of the web pages would still be allowed, while also being big enough to comfortably utilise. Reading and writing simultaneously should be possible	9	M	The GUI has covered the entire screen. The widgets fit comfortably into the screen and none of them are intrusive or obstructing the other ones, this is because of the grid layout by tkinter grid manager. 
The application must be a UK-QWERTY keyboard layout	This layout is ideal for UK Users which is where it is produced, it is also the standardised keyboard format for most of the world, however, accents and other symbols would be available	8	M	The applications layout uses a standard QWERTY keyboard
The application must have numbers and letters available	This is part of the standardised keyboard format keyboards must have letters and numbers before any symbols and currency are added	8	M	The application has both letters and numbers available.
The application must have punctuation symbols and numbers in an easily reachable area	This is part of the standardised keyboard format keyboards must have letters and numbers before any symbols and currency are added	8	M	The application has not only letters and numbers but symbols as well in a good area which is in the same area that the symbols usually are. This is generally the first row of the keyboard.
The application must have an auto-correct feature	This is in the case where keyword-specific search terms are necessary, to find the results that you need	7	S	The application does not have this feature; however, it will make it more accessible in the future developments. I will add this feature to the critical review.
The application must have an autocomplete feature	This would provide ease and speed of typing if a word is left incomplete it would be easier to finish the sentences and incomplete words to make more coherent writing	7	S	The application does not have this feature; however, it will make it more accessible in the future developments. I will add this feature to the critical review.
The application must have an autosuggestion feature
	This would be a way to have a clear, coherent and concise writing with added speed if there are suggested or frequently used words. This would be a movement towards normalising this technology to modern standards	7	S	The application does not have this feature; however, it will make it more accessible in the future developments. I will add this feature to the critical review.
The application must have a read-aloud feature	This would be reading aloud the letters which could potentially be irritating or necessary when something needs to be read back to the user	3	W	The application does not have this feature; however, it will make it more accessible in the future developments. I will add this feature to the critical review.
The application should be able to move the mouse using just the eye gaze	The functionality of the mouse is important as the control with the eye gaze would allow for the functionality of the entire desktop space to be able to time and to browse are both very important things	9	M	The application does this successfully, however the overall movement of the mouse is not completely fluid. For future developments it should be possible to evaluate all areas of the eye in order to create a freer moving mouse.
The application should be able to be given carer access for admin issues	This would be for the first-time setup of this application	4	C	The application does not have this feature; however, it will make it more accessible in the future developments. I will add this feature to the critical review.
The application should comfortably be able to control web pages with full functionality	This would be through the implementation of both the mouse scroll feature, the mouse and the eye gaze keyboard	6	C	This application does control webpages in its own window pretty well, the double clicks and the scroll functions do very well.
The application should have a hover mechanism to access letters with accents on them	A hover and expand mechanism would be interesting to have as it would be like a quick view to all other letters with accents and numbers associated with that letter on a regular phone keyboard	6	C	The application does not have this feature; however, it will make it more accessible in the future developments. I will add this feature to the critical review.
There should be a minigame to teach users how to effectively use the Vertigo Assistive Eye and to calibrate it if need be	This game would not only be for calibration but for practice on how to concentrate on certain areas of the game screen which would also be like focusing on the letters of the keyboard which has to be for a specific amount of time for it to register as a letterpress. With more use of this game, it would move towards better use of the keyboard as the person would have had more practice	4	W	The application does not have this feature; however, it will make it more accessible in the future developments. I will add this feature to the critical review.
(Table 2)
Non-functional requirements:
Requirement	Description	Significance	MoSCoW	How did my system respond to justify the requirements?
The application should be easy to navigate	Fast movement between the letters would be ideal, moving between letters, punctuation and numbers should be quick and simple	9	M	The mouse speed could be adjusted in the main menu screen in the settings.
There should also be volume control in the settings as well.
The application should have nice colours, with a clear contrast of the letter to background key colour	The colours need to have good contrast, for example, black and white or white on black to make typing a lot clearer. And not yellow and white whose colours are too close together that it would be extremely difficult to differentiate them. This would help those who are hard of sight to easily detect and differentiate between the selected letter and the background.	8	M	I followed the WIA on accessibility for websites and I found multiple ways in which it I s possible to improve my application to fit those accessibility options
The application should be easy to use, as straightforward as possible, to minimise stress	It needs to be a simple program which is straightforward and quick and easy to use, it should not be complex as the only aims of the Vertigo Assistive Eye is to type and move the mouse	7	M	The application barely has anything which is too confusing that can confusing to the user.
Everything is explained in the instructions and in the read me files.  
Application should be able to be moved around and be placed in a way that is neither intrusive nor obstructive to the user.	The keyboard needs to be on the place of the screen which is most comfortable to the user. In order to ensure this, it should be easy to move around the screen and adjust in size	6	M	The GUI has covered the entire screen. This is because I decided that the application should be self-contained.
The widgets fit comfortably into the screen and none of them are intrusive or obstructing the other ones, this is because of the grid layout by tkinter grid manager.
Buttons should be labelled	Buttons on the keyboard must be labelled with the appropriate letters	5	S	Buttons are labelled as appropriate keys.
(Table 3)


















Design and Development of the Vertigo Assistive Eye
Seeing as I was to make an accessible, assistive technology I had to find all things that make a piece of technology both accessible and assistive. I had to research many libraries and open source material to see what I could do to integrate them into an accessible GUI. I knew that I wanted to use OpenCV with Python, but I didn’t know that to make an attractive app, I would need a good structure called Tkinter/tkinter. OpenCV are difficult to integrate however it is through these structures that I was able to create the basis of this app.
Firstly, I had to research colour. According to the WAI, colour affects perception and more accessible colours would be those who have good contrasts (WAI, 2019). This also fulfils one of my later points under Nielsen’s 10 User Usability Heuristics for User Interface Design. Under one of the points ‘aesthetic and minimalist design’, there needs to be a good signal to noise ratio to avoid cluttering the screen. This can be used by using a standard colour set so as to not put on too many contrasts on the page so the content is easy to see and use, this would be helpful for those with poor vision and also colour blindness (Nielsen, 1994). I have avoided colours that clash for this reason and I have also avoided using the colours red and green together to benefit those with red green colour blindness (Colblindor, 2006). In order to ensure my application was accessible I used a colour contrast checker which takes all of these factors into consideration.
When using the colour contrast checker, it is important to select a colour contrast which has the highest ratio, with the minimum ratio being 7:1 for normal text and 4.5:1 for large text according to the WCAG. For this reason, I have chosen, black and white for the keyboard which has a contrast of 21:1 (Figure 3) see how it has been displayed on the keyboard (Figure 4), and 7.24:1 when it is selected (Figure 5) and the way it is displayed onto the keyboard (Figure 6).
I had to then research the python libraries that I would be using in depth. I will be using a mixture of different libraries as my application covers many different bases.
Another aspect of this program is that it has a moving key which is used to highlight which key to select, this may be difficult when it comes to implementing accessibility as the software uses a free movement mouse. I needed to find a balance between the demonstration of selecting a key without being inaccessible and distracting. The speed at which some people process information is much different from others and having content disappear is something that would be inappropriate for some users. I decided to cycle flashing one time, I also did not want to violate other guidelines such as being too bright, flashing in a large area, and flashing multiple times without long intervals, which could cause seizures (WAI, 2020).
I decided to also have a large font size of 16pt, I will give the option to resize the text to make it more visible for more people to use. Also, the implementation of vertical scrolling would be of better use than horizontal scrolling for accessibility. However, this may be inconvenient for other types of user, therefore I had to compromise. To make a sheet wide enough for sentences while also having a horizontal scroll for other users as it is supposed to be for long writing tasks for students (WAI, 2020).
I also chose website links that have passed accessibility guidelines (WAI, 2020) these are generally Chromium widgets which are the most commonly used in the world (Hoffman, 2014).



The open- source libraries that I took into consideration were: 
PYTHON 
LIBRARY                 VERSION   INSTALLED                                     COMMENTS
MouseInfo	0.1.3	0.1.3	Displays X, Y coordinate the mouse is on and RGB
Pillow	7.1.2	7.1.2	Opening and manipulating file formats
PyAutoGUI	0.9.50	0.9.50	Used to control mouse and keyboard
PyGetWindow	0.0.8	0.0.8	Control the object window
PyMsgBox	1.0.8	1.0.8	Displays a message box
PyQt5	5.14.2	5.14.2	Create an API/ Widget on a Chrome base web browser
PyQt5-sip	12.7.2	12.7.2	Create an API/ Widget on a Chrome base web browser
PyQt5-stubs	5.14.2.2	5.14.2.2	Create an API/ Widget on a Chrome base web browser
PyQtWebKit	5.13.1	5.13.1	Create an API/ Widget on a Chrome base web browser
dlib	19.8.1	19.19.0	Works in conjunction with the dataset, which was fed in, when used for facial landmark detection it will locate the 68 landmark points on a face. It has machine learning algorithms which also help to solve real calculations.
imutils	0.5.3	0.5.3	This is used for images. It is an image utility library which helps to resize images
NumPy	1.18.4	1.18.4	This is the computation aspect of my project as a lot of maths to calculate midpoints are here.
opencv-python	4.2.0.34	4.2.0.34	This is for the main image processing.

(Table 1)
There was pre-installed library but the only one which is worth mentioning is the Tkinter/tkinter library, this is a way to lay the final GUI main window onto a canvas and lay on buttons, and a proper structure to the layout. Tkinter has geometry management which is a way to space things onto the GUI in any way you want. With a little bit of manipulation these libraries tend to work well with each other.
Another thing that I had to consider is using a dataset. When using OpenCV it is expected that machine learning was to be a part of it. Training software which would recognise the points on any face would require the use of a trained machine. Training my software to be able to detect the points on a moving image on multiple faces would be extremely difficult. I would then decide that it would be best to use a dataset which would have done this already. I used shape_predictor_68_landmarks.dat which is a dataset which has been pre trained to sync the facial landmarks with a moving image, in my case a live video camera.
I also used a lot of OS code which I changed and developed in order for me to find a balance between a code that I would evaluate and use for my own final project.
For they keyboard used two different types. Firstly, I studied the documentation and output of a keyboard which used OpenCV. This keyboard to me was very ugly (Figure 7), it did not have the traditional look of a keyboard, the colour that was displayed when the key was struck was clear and could potentially be good for functionality and accessibility (Figure 8). However, it was in two colours which made accessibility easy. The output of text in OpenCV was not traditional, it was hard to read, and it didn’t scroll, two keyboards would be needed as it had no function to make uppercase or lowercase, the punctuation was also hard to see. This although useful was not the type of layout that I would want to use as there needs to be some semblance of similarity to a writing outlet such as Microsoft Word.
The second keyboard was created using the Tkinter/tkinter library. This keyboard had the overall standard look that I wanted and it, it was easier to place the buttons on the screens using arrays unlike OpenCV which would require the use of you placing the buttons down on a frame using coordinates. The output looked like a fully typed page of writing and it has a better form and structure and output when used in conjunction with the keyboard (Figure 9). It is large enough to be accessible for more than one type of person while having the utilitarian approach.
Overall, I preferred Tkinter/tkinter library It has the structure that I think would be appropriate, changing the colours to be more accessible and having a larger and smaller font where necessary would be appropriate. I tried adding scroll bars so that there would be a visual cue to be able to scroll down, view the work as a whole and check it while its being done. I also thought of coding in a print feature and a text to speech option and a save feature for the work. This more standardised layout would allow for this to be clearer. 
The next thing I wanted to see was the selection of the eye in OpenCV which would lead to detecting if the eye is looking either left or right on the screen. There are multiple ways that this can be done. 
The first would be through using Haar Cascades this is a feature in OpenCV. The feature uses a trained function which detects objects in other images. A Haar Cascade is optimal for face and eye detection. OpenCV already can track the face and eyes with a lot of precision. Detecting the eye because of such a simple algorithm is very easy (OpenCV, 2013). I decided that this approach was optimal. I could use this in conjunction with a background mask to isolate the eye itself.
Another way would be to find the points of the eye using OpenCV and then applying a mask to all the areas around the mask. This is a very long-winded approach by PySource. It was not effective as sometimes my eye would jump below or above the mask while the mask would keep the eye shape. This is because the mask is cut to the entire frame of a person rather than the selected part which is the eye (Pysource, 2019).
I would then have to have to produce a camera display which would demonstrate to the user where they should be sitting in relation to the screen. This was relatively as the same code which can be used to read in an image will also be used to read in video.
OpenCV was the part that took the longest to learn because although I have heard of it and was able to make sense of the code as it was similar to MATLAB, these were obvious hinderances to me as I had to spend a lot of time changing my code in order to suit the computer I was using. I faced a lot of trouble converting my old work into my new computer due to a flood. The change in aspect ratio from my laptop to computer meant that my old code didn’t work on my new computer. Which would mean I would have to re write it. All of the libraries and technologies where easy to implement however very difficult to canvas. Due to this I had to do extra learning to develop my GUI further.





Product Description
•	Tkinter/tkinter
•	Dlib
•	NumPy
•	OpenCV
•	PyPt5
•	PyAutoGUI
The project was difficult for me, the majority of the aims of this product have been met and I am comfortable to say that the eye tracker is somewhat complete. I have had a lot of fun creating this project, but it was through many uncontrollable circumstances that the project has not been seen to fruition. I have seen myself grow as a coder, fixing complex problems that my friends have asked me to solve and I am grateful to show you what I have so far.
Building the GUI was really helpful at it showed me the step by step process of making a product. In order to have a working project it is important to nurture every part individually otherwise the project will struggle to grow and develop as a whole. There are some parts of the project which have not been completed but they would definitely be good for the future developments of the code. 
My GUI consists of an introduction screen, a keyboard, an eye tracker which is working in the background, a live front camera and a web browser which has chrome plug ins. I found it necessary to do these all as simply as possible, I had to do a lot of research and manipulation of lots of prior code in order to get the results that I wanted. And also, I found it easy to write some bits of the code myself. I have also learned the structure of python pretty well from this project and nearing to the final tasks the work was coming with much fluidity.
Within the comments of the code “##” there are full explanations of how the code works, they will be detailed, and the final result will be shown for each part of the code at the end of the code explanation.
THE KEYBOARD
The first thing I needed to do was to create the keyboard itself, this was one of the easier tasks as I wanted to make a standard black and white keyboard, with a plain ‘white paper’ like output. The objective of the keyboard was simple. To create a clear interface where the user could type using an online keyboard that the user can interact with and on top of that, have a colour changing input when a particular key is selected, in this case it is white to green.
The development of the keyboard was relatively straight forward. The only thing that was difficult was using a lambda function to give some of the keys a specific functionality, for example the shift and the Caps Lock and the Backspace keys. However, the Enter Key and the Tab Key work perfectly. I struggled with the type of input box that I needed, I settled with using an entry box as there can be a large amount of characters that can be used there. Before I had an input box active, this is wrong as input boxes are for the entering of small information such as first and last names and email addresses.
When I created the keyboard I learned how to make functions in python, this would be useful for the rest of my project especially for the Web Browser, it showed be that the perfect way to display information would be to put them into functions. I wanted to make the GUI as straight forward as possible, so I have indicated flashing keys, this would lead to the user to click them out of curiosity, that is if they’ve never used a keyboard before.
I generally find arrays difficult and I found myself playing around with the arrays I used for my buttons for a long time, this is because I found it difficult to fit all of my buttons neatly on a screen into a structure that made sense. It took a lot of trial and error. This issue was resolved through me rearranging my keyboard and adding numbers so that the keyboard had more structure as before the letters on the top row would mix into the middle row and that would not be a standard QWERTY layout.
CODE:
import tkinter as tk
from tkinter import *
import tkinter

##THESE ARE ALL IMPORTS FOR THE GUI TOOLKIT TKINTER, THIS CONTAINS THE MAIN PYTHON MODULES FOR ENTRY BOXES, BUTTONS AND WIDGET POSITIONING.

##THIS IS TO INITIALISE THE HIGHER LEVEL WIDGET, IT IS INITIALISED WITH NO ARGUMENTS

Keyboard = tk.Tk()
Keyboard.geometry("1600x958+455+30")

##(XxY+X+Y)THIS IS TO RESIZE THE GUI IN THE X Y RESOLUTION ‘X+Y’ INDICATES THE POSITION ON THE SCREEN

##THIS IS THE FIRST FUNCTION IT IS FOR THE BUTTONS WHICH ARE OF SPECIAL VALUE, THESE BUTTONS WOULD HELP TO ADD FORMATTING OF THE WIDGETS TO THE SCREEN.

def select(value):
    if value == "     Space     ":
        entry.insert(tkinter.END, ' ')
    elif value == "Tab":
        entry.insert(tkinter.END, '       ')
    elif value == "Shift":
        entry.insert(tkinter.END, )
    elif value == "Caps":
        entry.insert(tkinter.END, )
    elif value == "Bkspace":
        entry.insert(tkinter.END, '')
    elif value == "Enter":
        entry.insert(tkinter.END, '\n')
    else:
        entry.insert(tkinter.END, value)

##FAILED CODE
# def autocapitalize(*arg):
# var.set(var.get().capitalize())

# var.trace("Caps", autocapitalize)
##FAILED CODE

Keyboard.title("Vertigo Assistive Eye: Keyboard and Mouse") ##TITLES THE WINDOW
Keyboard['bg'] = 'black’	##THIS COLOURS THE CANVAS THE TARGET COLOUR
##DOES NOT WORK##
label1 = Label(Keyboard, text="Vertigo Assistive Eye: Keyboard and Mouse", font=('times new roman', 16, 'normal'),
               bg='black', fg="#000000").grid(row=1, columnspan=40) 
##PLACES TITLE ON THE SCREEN OF THE KEYBOARD
entry = Text(Keyboard, wrap=WORD,  #textvariable=var, #yscrollcommand=scrollBar.set,
             width=100, height=32, font=('times new roman', 16, 'normal'))
entry.grid(row=1, columnspan=60) ##THIS DISPLAYS THE TEXT INTO THEW TERMINAL ON THE SCREEN
# entry.pack(side=LEFT, fill=BOTH) ##FAILED SCROLLBAR CODE,
# scrollBar.config(command=entry.yview)

buttons = ['!', '"', '£', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', 'Bkspace', '/', '7', '8', '9',
           'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '{', '}', '[', ']', 'Enter', '4', '5', '6',
           'Caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', ':', '@', '''''', '#', '~', '1', '2', '3',
           'Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<', '>', ',', '.', '?', '|', '\'', '¬', '`', '0', '',

           '     Space     '

           ] ##THIS LISTS ALL THE KNOWN BUTTONS THAT ARE NEEDED FOR THE KEYBOARD
varRow = 2 ##THIS IS A VARIABLE TO INITIALISE THE AMOUNT OF ROWS
varColumn = 0 ##THIS IS A VARIABLE FOR THE NUMBER OF COLOUMNS


##THIS IS TO GIVE FUNCTIONALITY TO THE BUTTONS LIST IN THE CODE, THIS TURNS THE BUTTON GREEN ON CLICK, GIVES IT PADDING IN THE X AND Y DIRECTION OF THE BUTTON AND GIVES IT A LIFTED OR ‘RAISED’ BUTTON LIKE LOOK. THE FINAL LOOK IS A 3D LIKE BUTTON ON THE SCREEN
for button in buttons:
    command = lambda x=button: select(x)
    if button != "     Space     ":
        tkinter.Button(Keyboard, text=button, width=6, padx=0.5, pady=0.5, bd=9,
                       font=('times new roman', 12, 'normal'), bg='white',
                       activebackground='green', activeforeground='#FFFFFF', relief='raised',
                       command=command).grid(row=varRow, column=varColumn)
    if button == "     Space     ":
        tkinter.Button(Keyboard, text=button, width= 100, padx=1, pady=1, bd=2,
                       font=('times new roman', 12, 'normal'), bg='white',
                       activebackground='green', activeforeground='#FFFFFF', relief='raised',
                       command=command).grid(row=7, columnspan=20)
    varColumn += 1 ##THIS IS TO DEMONSTRATE THE ARRAY OF HOW THE BUTTONS ARE ARRANGED INTO THE GUI 

    if varColumn > 18 and varRow == 2: ##THE BUTTONS ARE ARRANGED INTO 4 ROWS OF 18 STARTING ON THE ‘2ND’ ROW WHICH HAS BEEN INITIALISED PRIOR.
        varColumn = 0
        varRow += 1
    if varColumn > 18 and varRow == 3:
        varColumn = 0
        varRow += 1
    if varColumn > 18 and varRow == 4:
        varColumn = 0
        varRow += 1

Keyboard.mainloop() ##THIS CLOSES THE LOOP AND ENABLES WINDOW TO CLOSE 


RESULT:
 















RESULT ON CLICK:
 

THE EYE TRACKER
The eye tracker was the most difficult task on the whole program, I did this by using OpenCV. I feel as if I completely underestimated the scope of the project however I have managed to make the mouse movement possible.
 I had successfully completed the face detection, then the detection of the eyes themselves, it was easy to isolate the eye. I did this by putting a binary mask on the eye after converting it to grayscale. Putting a binary mask does a very cool thing, it makes only two colours to be clearly available so that further detection can happen. The only two colours that are then available are black and white. From this I was able to select the iris of the eye and begin plotting my tracker to the screen. This was also easy, as I made the eye tracker detect what is left, centre and right when looking at the screen. I also was able to return coordinates of the gaze on the screen. The last step that has not been done is to apply PyAutoGUI. PyAutoGUI is a way for the computer to control your mouse movements, all the mouse movements can then be coded. 
CODE:
import cv2
import numpy as np
import dlib
from math import hypot
import pyautogui as pag


## PYAUTOGUI IS THE LIBRARY WHICH CONTROLLS ALL MOUSE AND KEYBOARD MOVEMENTS, YOU CAN SET KEYS TO DO SPECIFIC FUNCTIONS AND YOU CAN ALSO SET THE MOUSE TO DO SPECIFIC FUNCTIONS AS WELL I USED THIS TO AUTOMATE THE CONTROLL OF THE MOUSE AND LINK IT TO THE EYE MOVEMENT

pag.FAILSAFE = False
##FAILSAFE IS SET AS FALSE, THIS MEANS THAT THE MOUSE WILL NOT TERMINATE WHEN IT MOVES TO THE TOP CORNER OF THE SCREEN. WHEN THE MOUSE MOVES TO POSITION 0,0 ON THE SCREEN IT WOULD NORMALLY RELEASE THE ACTION OF THE AUTOMATION OF THE MOUSE

## This launches the camera, 0 is the position of my first camera any other additional cameras are listed 1,
## 2, 3, etc, etc.
cap = cv2.VideoCapture(0)

## this is a pre-trained data set, this is for the facial landmarks of any face, it has a total of 68 pre-recognised
## points in a face
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

Below is a figure which lists all the landmarks which are used by the frontal face detector in order to pinpoint all of the points on the face, these points are later detected for the eyes themselves. I have used the average of the two eyes to show that the blink has been produced
 



## my first function, this is for finding the midpoint of two points, this useful when finding the absolute centre of the
## eyes, THIS FIRST TAKES ALL THE SURROUNDING POINTS OF THE EYE, POINTS 37 TO 46 IN THE IMAGE ABOVE AND FINDS THE CROSS SECTION THIS THEN FINDS THE CENTER POINT OF THE EYE HOWEVER THIS CENTER POINT DOES NOT FOLLOW THE PUPIL TRACKING
def midpoint(p1, p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)
    return midpoint()

## the font that is displayed is clear enough to be properly seen
font = cv2.FONT_HERSHEY_TRIPLEX
##THIS SHOWS ALL THE POINTS AROUND THE EYE, FACIAL LANDMARKS IS F_LANDMARKS, THIS AND POINTS ARE POINTS 37 TO 46 OF THE POINTS AROUNT THE LEFT EYE. 
def ratio(points, f_landmarks):
    left_point = (f_landmarks.part(points[0]).x, f_landmarks.part(points[0]).y)
    right_point = (f_landmarks.part(points[3]).x, f_landmarks.part(points[3]).y)
    center_top = midpoint(f_landmarks.part(points[1]), f_landmarks.part(points[2]))
    center_bottom = midpoint(f_landmarks.part(points[5]), f_landmarks.part(points[4]))

    # hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 1)
    # ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 1)

    hor_line_length = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_length = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

    blink = hor_line_length / ver_line_length

    return blink

 
def get_gaze_ratio(points, f_landmarks):
    region_left = np.array([(f_landmarks.part(points[0]).x, f_landmarks.part(points[0]).y),
                            (f_landmarks.part(points[1]).x, f_landmarks.part(points[1]).y),
                            (f_landmarks.part(points[2]).x, f_landmarks.part(points[2]).y),
                            (f_landmarks.part(points[3]).x, f_landmarks.part(points[3]).y),
                            (f_landmarks.part(points[4]).x, f_landmarks.part(points[4]).y),
                            (f_landmarks.part(points[5]).x, f_landmarks.part(points[5]).y)], np.int32)

    height, width, _ = frame.shape
    mask = np.zeros((height, width), np.uint8)

    cv2.polylines(mask, [region_left], True, (255, 255, 255), 1)
    cv2.fillPoly(mask, [region_left], 255)

# shows eye in the mask to eye-solate it
    eye = cv2.bitwise_and(gray, gray, mask=mask)
    # cv2.imshow("eye", eye)

    min_x = np.min(region_left[:, 0])
    max_x = np.max(region_left[:, 0])
    min_y = np.min(region_left[:, 1])
    max_y = np.max(region_left[:, 1])

    gray_eye = eye[min_y: max_y, min_x: max_x]
    _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY_INV)
    threshold_eye = cv2.resize(threshold_eye, None, fx=5, fy=5)
    cv2.imshow("T", threshold_eye)

    masked_eye = cv2.resize(gray_eye, None, fx=5, fy=5)

    cv2.imshow("Masked Eye", masked_eye)

    height, width = threshold_eye.shape
    left_thresh = threshold_eye[0: height, 0: int(width / 2)]
    left_thresh_black = cv2.countNonZero(left_thresh)

    right_thresh = threshold_eye[0: height, 0: int(width / 2): width]
    right_thresh_black = cv2.countNonZero(right_thresh)

    if left_thresh_black == 0:
        determination = 1
    elif right_thresh_black == 0:
        determination = 10
    else:
        determination = left_thresh_black / right_thresh_black

    return determination



while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 255), 2)

        landmarks = predictor(gray, face)

        # Blink Detection Ratio

        if landmarks != predictor(gray, face):
            cv2.putText(frame, "Face Detection Ready.", (400, 400), font, 0.5, (0, 0, 255), 0)
        else:
            cv2.putText(frame, "Face NOT Detected, Please Come Into The Frame", (0, 100), font, 0.5, (0, 0, 255), 0)
# BLINK
        ler = ratio([36, 37, 38, 39, 40, 41], landmarks)
        rer = ratio([42, 43, 44, 45, 46, 47], landmarks)
        b_ratio = ((ler + rer)/2)

        if b_ratio > 5:
            cv2.putText(frame, "Blink Detected", (0, 100), font, 0.5, (0, 0, 255), 0)
            #pag.click() ##left click
            #pag.click(clicks=2, interval=0.225)##doubleclick
            #pag.scroll(-60, x=200, y=420)
 
        # Gaze Detection

        gaze_ratio_left = get_gaze_ratio([36, 37, 38, 39, 40, 41], landmarks)
        gaze_ratio_right = get_gaze_ratio([42, 43, 44, 45, 46, 47], landmarks)

        determination = ((gaze_ratio_left + gaze_ratio_right)/2)

 
 
 

 
 
 


        if determination < 72:
            cv2.putText(frame, "Left", (200, 100), font, 2, (0, 0, 255), 2)
            pag.moveTo(200, 420, duration=0.2)
        elif 73 < determination < 85:
            cv2.putText(frame, "Right", (200, 100), font, 2, (0, 0, 255), 2)
            pag.moveTo(1600, 420, duration=0.2)
        elif determination >= 86:
            cv2.putText(frame, "Center", (200, 100), font, 2, (0, 0, 255), 2)
        else:
            cv2.putText(frame, "Undetected", (200, 100), font, 2, (0, 0, 255), 2)

        cv2.putText(frame, str(determination), (300, 100), font, 2, (126, 221, 106), 2)

    cv2.imshow("Front Camera", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

 
THE FRONT CAMERA
The front camera was another thing which was very easy to display. I did this by using OpenCV and displayed it within a tkinter window, I used this as a way to display the face and to tell the user to come into frame when the face is not detected.
CODE:
import PIL
from PIL import Image, ImageTk
import cv2
from tkinter import *

cap = cv2.VideoCapture(0)

root = Tk()
video = Label(root)
video.pack()


def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    cap1 = ImageTk.PhotoImage(image=img)
    video.cap1 = cap1
    video.configure(image=cap1)
    video.after(10, show_frame)


root.geometry("350x470+1575+30")
show_frame()
root.mainloop()

RESULT:
 
THE WEB VIEWER
I created a Web Browser using PyQt5 this is a library which is used to control websites. I managed to display some websites in the window to demonstrate the usage of the GUI. I also gave these windows tabs so that they can be switched between easily. I put in all the tabs that a student could possibly need. These are for example, Bing, Email, Student Central, Harvard APA cite this for me and YouTube. These are all hard coded into the system and the webpages are completely interactive mini displays.
In the future this can be improved by:
•	Giving the web viewer a layout, which is more like the chrome, have a way to store passwords and to access the settings and the history
CODE:
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTabWidget, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtCore import *


class TabWidget(QDialog):
    def __init__(self):
        super(). __init__()

        self.setWindowTitle("Chrome")
        self.setWindowIcon(QIcon())
        self.resize(455, 950)
        self.move(0, 0)

        tabWidget = QTabWidget()

        tabWidget.addTab(Scholar(), "Scholar")
        tabWidget.addTab(Email(), "Email")
        tabWidget.addTab(YouTube(), "YouTube")
        tabWidget.addTab(BBL(), "Student Central")
        tabWidget.addTab(Cite(), "Harvard")
        tabWidget.addTab(Bing(), "Search")

        vBox = QVBoxLayout()
        vBox.addWidget(tabWidget)

        self.setLayout(vBox)


class Scholar(QWidget):
    def __init__(self):
        super().__init__()

        web = QWebView()
        web.load(QUrl("http://scholar.google.com"))

        layout = QVBoxLayout()
        layout.addWidget(web)
        self.setLayout(layout)


class Bing(QWidget):
    def __init__(self):
        super().__init__()

        web = QWebView()
        web.load(QUrl("http://www.bing.com"))

        layout = QVBoxLayout()
        layout.addWidget(web)
        self.setLayout(layout)


class Cite(QWidget):
    def __init__(self):
        super().__init__()

        web = QWebView()
        web.load(QUrl("http://www.citethisforme.com"))

        layout = QVBoxLayout()
        layout.addWidget(web)
        self.setLayout(layout)


class Email(QWidget):
    def __init__(self):
        super().__init__()

        web = QWebView()
        web.load(QUrl("http://mail.google.com"))

        layout = QVBoxLayout()
        layout.addWidget(web)
        self.setLayout(layout)


class YouTube(QWidget):
    def __init__(self):
        super().__init__()

        web = QWebView()
        web.load(QUrl("http://www.youtube.com"))

        layout = QVBoxLayout()
        layout.addWidget(web)
        self.setLayout(layout)


class BBL(QWidget):
    def __init__(self):
        super().__init__()

        web = QWebView()
        web.load(QUrl("https://studentcentral.brighton.ac.uk/"))

        layout = QVBoxLayout()
        layout.addWidget(web)
        self.setLayout(layout)


App = QApplication(sys.argv)
tabWidget = TabWidget()
tabWidget.show()
App.exec()


RESULT:
 
 
THE INTRODUCTION SCREEN/THE MAIN MENU
I wanted to make a small introduction screen so I could add the instructions before opening the project. This would be helpful. However, I have to be aware that when adding an introduction screen the eye tracker will most likely not be active. This could potentially cause problems with accessibility of the application only making it partially accessible.
•	Create a way for the eye tracker to be active from the point of opening the app
•	Make an indication of what the mouse should look like when the eye tracker is active for example have the logo of the eye is green when the eye is tracking or changing the shape of the mouse into a blinking eye to show that it is tracking
CODE:
import os
from tkinter import *
from PIL import Image, ImageTk
global image

class SplashScreen(Frame):
    def __init__(self, master=None, width=0.4, height=0.3, useFactor=True):
        Frame.__init__(self, master)
        self.pack(side=TOP, fill=BOTH, expand=YES)

        # get screen width and height
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        w = (useFactor and ws * width) or width
        h = (useFactor and ws * height) or height
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.master.overrideredirect(True)
        self.lift()


if __name__ == '__main__':
    root = Tk() #

    photo = Image.open("VertigoIndustries.png") #   Parsing name of photo.
    photo = photo.resize((150, 150), Image.ANTIALIAS) #     Resizing photo.
    photo = ImageTk.PhotoImage(photo)   #   Photo Added.


    label = Label(root, image=photo)
    label.pack(side=TOP, expand=YES)

    sp = SplashScreen(root)
    sp.config(bg="#af2a2f")

    m = Label(sp,
              text="Now booting, Vertigo Assistive Eye: Keyboard & Mouse!"
                   "\n\n Select your options below: ")


    m.pack(side=TOP, expand=YES)
    m.config(bg="#af2a2f", justify=CENTER, font=("calibri", 18))

    def Start():
        root.destroy()
        os.system("python GUIWindow.py")

    def Instructions():
        root.destroy()
        os.system("python Instructions.py")

    def Settings():
        root.destroy()
        os.system("python Settings.py")

    def Destroy():
        root.destroy()

    Button(sp, text="Exit", bg='blue', command=Destroy).pack(side=BOTTOM, fill=X)
    Button(sp, text="Settings", bg='blue', command=Start).pack(side=BOTTOM, fill=X)
    Button(sp, text="Instructions", bg='blue', command=Instructions).pack(side=BOTTOM, fill=X)
    Button(sp, text="Start", bg='blue', command=Start).pack(side=BOTTOM, fill=X)
    root.mainloop()

RESULT:
 
INSTRUCTIONS AND SETTINGS MENUS
CODE:
import os
from tkinter import *
from PIL import Image, ImageTk
global image

class Instructions(Frame):
    def __init__(self, master=None, width=0.4, height=0.3, useFactor=True):
        Frame.__init__(self, master)
        self.pack(side=TOP, fill=BOTH, expand=YES)

        # get screen width and height
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        w = (useFactor and ws * width) or width
        h = (useFactor and ws * height) or height
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.master.overrideredirect(True)
        self.lift()


if __name__ == '__main__':
    root = Tk() #

    sp = Instructions(root)
    sp.config(bg="#af2a2f")

    m = Label(sp,
              text="Vertigo Assistive Eye: Keyboard & Mouse! - Instructions!"
              "\n\n This is the Vertigo Assistive Eye!"
              "\n\n This is a GUI for disabled students. "
              "\n\n Use the keyboard by looking at any specific key and blink to select it."
              "\n\n The key when selected will turn green that shows you that you have done it! "
              "\n\n Stay in frame by using the active front camera. Keep your face within the frame at all times."
              "\n\n For one left click, blink once, "
              "\n\n For a double click, blink twice."
              "\n\n I hope you enjoy using this application.")


    m.pack(side=TOP, expand=YES)
    m.config(bg="#af2a2f", justify=CENTER, font=("calibri", 15))

    def Return(): # Returns to splash screen
        root.destroy()
        os.system("python SplashScreen.py")

    Button(sp, text="Return", bg='blue', command=Return).pack(side=BOTTOM, fill=X)
    root.mainloop()
RESULT:
 

 

THE GUI
Placing all the items in the GUI together was difficult, this is because even though they are in the same language, the imports and extensions could mean that extra manipulation would be necessary in order to pull these items together. In total I used around 6 different libraries. All of these would need to be brought together in some way to make the final window. I used absolute positioning when placing the coloured widgets on the screen I used this to indicate the positioning of the final GUI.
CODE:
from tkinter import *
import tkinter as tk
import sys


class Application(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.grid()

        self.initUI()

    def initUI(self, master=None):
        self.master.title("Vertigo Assistive Eye: Keyboard & Mouse")

        for r in range(6):
            self.master.rowconfigure(r, weight=1)
        for c in range(12):
            self.master.columnconfigure(c, weight=1)

            Button(master, text="Back".format(c)).grid(row=6, column=0, sticky=E+W)
            Button(master, text="Save".format(c)).grid(row=6, column=5, sticky=E+W)
            Button(master, text="Print".format(c)).grid(row=6, column=6, sticky=E+W)
            Button(master, text="Instructions".format(c)).grid(row=6, column=7, sticky=E+W)
            Button(master, text="Settings".format(c)).grid(row=6, column=11, sticky=E+W)

        Frame1 = Frame(master, bg="pink")
        Frame3 = Frame(master, bg="light blue")
        Frame2 = Frame(master, bg="light coral")
        Frame4 = Frame(master, bg="bisque")

        LABEL1 = Label(Frame1, text="CHROME APP").pack()
        LABEL3 =Label(Frame3, text="KEYBOARD").pack()
        LABEL2 =Label(Frame2, text="FRONT CAMERA").pack()

        Frame1.grid(row=0, column=0, rowspan=6, columnspan=3, sticky=W + E + N + S)
        Frame3.grid(row=0, column=3, rowspan=6, columnspan=11, sticky=W + E + N + S)
        Frame2.grid(row=0, column=10, rowspan=3, columnspan=2, sticky=W + E + N + S)
        Frame4.grid(row = 3, column = 10, rowspan = 3, columnspan = 2, sticky = W+E+N+S)
def main():
    root = tk.Tk()
    root.geometry("1910x1008+0+0")
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()










RESULT:
 
FINAL RESULT:
 
Legality and Ethics
I made a few considerations when making my project.
Firstly, I considered the effect of the Data Protection Act, 2018 in my work. This act states that biometric data when used as a means of identification is classified as a piece of personal information and therefore should be handled carefully. Because of this the data should be destroyed after its use. I believe that my application is in agreement with the Data Protection Act and follows the ‘data protection principles’ as it says  that data should be used ‘in a way that is adequate, relevant, and limited to only what is necessary’ and that it should be ‘kept for no longer than necessary’ (GOV, 2018). Although my application uses biometrics in some regard, it is not keeping or recording the data. In the event the application is closed the eye movement stops and is no longer being recorded. There is no need for the collection of the biometric data of a person. These actions would definitely keep the user of my application safe.
Protection of Biometric Information of Children in Schools, 2013, the ultimate aim for my application would be to be used in a school for children and university students to have a means of continuing their education in an enclosed GUI which would make research and essay writing easier for them. Children deserve special protections when it comes to using any biometric device. Express consent needs to be given from both the carer and the child themselves in order to use the application. This act also aligns with the Data Protection Act. This also means that the information after the child has done their tasks should be destroyed too (GOV, 2013).
Equality Act, 2010, which replaced the Disability Discrimination Act, 1995 this is to make sure that there are opportunities for people of all living situations to have an equal living experience with their peers. This is the act which encourages the equality, accessibility and the assistance of my technology. Due to the multiple rules as aforementioned by W3C, all the little steps to make applications more accessible have been set out however it is up to companies to take them into stride (GOV, 2010). Ethically, I have decided to take a utilitarian approach. Applying many methods of accessibility would help my application reach a larger amount of people. Taking this approach makes my application more accessible.
I am not allowed to have anyone test my application, as it Breaks Brighton University’s convention on collecting biometric data. Because of COVID-19, I was not able to give formal sit-down interviews. However, I would have maintained professionalism by keeping interview structure. (University of Bristol, 2020)
Evaluation and Testing
The testing period for this application spanned the entire length of the creation process. Testing came in the form of continuously debugging my code. This would be through adjusting the
Another thing that I had to consider was Nielsen’s 10 Usability Heuristics for User Interface Design.
Brighton University’s policy on the collection of sensitive data, I am not able to directly collect biometric data from participants. Seeing as I am only able to use my own data, I will use the 10 principles to evaluate and apply the necessities of a user interface and apply them to my own work. From the list of ten, I will select four of the heuristics and demonstrate how I will tweak my software in order to fit the principles, as these are.
‘Consistency and standards’, this is important for ensuring that the software is easy to learn and predictable. This would mean that I would have the same colours, fonts and usages for a specific task. For example, I have kept the font consistent for the keyboard and the output. The keys on the keyboard have a specific output, ‘K’ key produces a ‘k’. These conventions should be consistent and produce predictable results, and this would increase the reusability and decrease the discontinuance of my product. This is because the result that the user is expecting has always been produced. Creating too many complex scenarios would cause the cognitive load of the user to increase making the software too complicated to learn and reuse. The aim is to minimise the new learning, which would be the eye-gazing and maximise predictability.
‘Help users recognise, diagnose, and recover from errors’ Staying in view is very important when using an eye-gazing keyboard. I have decided to blur the image of the user and create a pop up which tells the user to come back into view, so they can continue to use the keyboard.
‘Aesthetic and minimalist design’ I have ensured that my software has a very minimalist outlook, this is so that it has a high signal to noise ratio. On the screen there are only things that are necessary. For example, the output box, the search bar and the keyboard. This communicates to the user the point of the program; it is a research tool for long writing tasks. This is to avoid the user being overloaded with unnecessary overly decorative information. 
‘Error prevention’ is critical this refers to the potential design errors of my system. The aim is to avoid the user from making errors when using my software. For example, I need to be aware of the colours of the software (Nielsen, 1994).
Critical Review
Successes	Failures
•	Each GUI is completely automated
•	The grid layout of the GUI is fits everything in the screen nicely	For the overall look of the GUI:
•	The areas of my code that are unlinked for example the widgets in the GUI. The program would look a lot smoother if all of the items were packed into the same window.
For the Eye tracker:
•	The movement of the mouse is not dynamic enough, at this point it only moves along the x axis to either the left defined point or the right defined point of the screen. This is because I define the entire screen using the determination function as either right or left. If I had divided the screen into  more areas like a mosaic it would have been possible to have the mouse movement move pixel by pixel which would be more accurate to the location that the user is looking at on the screen.
•	The eye movement should be defined using a better equation, I used the suggestion of isolating the black ant the white area of the eye, because of this, the mouse either only moves from right to left. Using the same code, I could segment the eye into smaller parts. Segmenting the eye into more areas could allow for more calculations about the pupil’s location in relation to the eye and then I can use PyAutoGUI to move the mouse to more accurate positions
•	Ensure that the eye tracker is completely dependent on the mean of the movement of the two pupils this would include the development of an equation e.g. left eye for left click and right eye for right click
•	Create a screen where it is possible to have complete control over the speed of the eye tracker.
•	Make the eye tracker mode dynamic with further testing
For the keyboard:
•	Make sure all of the keys flash at least one time in succession to demonstrate the usage of the keyboard
•	I will make sure to program the parts I left out, in this case the Caps lock, Backspace and Shift keys
•	I should add ways for a person to have auto-capitalise, auto correct, auto suggest means on my keyboard to bring them up to the modern standard of typing especially on a mobile phone
•	Include a way for the key to give a sound output when clicked so it can be more accessible to other users
•	

Conclusion & Future Developments
I believe that I have set the wheels in motion for a good project to be made. I do see a product such as this going far! I am optimistic for its future. 
The main future development that needs to happen with this project is that it needs to be tested with a wider audience! When there are tests it is much easier for the code to be adjusted in such a way that it could either be personalised for a particular person or adjusted for the wider group of people.
I believe that with further development this GUI would be one which can be marketed to schools as a way for students who are disabled, have motor skill issues and have LDs to use a computer in class with the other students! The eye tracker itself could be helpful inside of a learning interface such as Blackboard Learn for Student Central too. The best thing about the GUI is that it has an extra tab for searching which ensures that the user can use it for any other purpose for example for shopping and e-commerce. eLearning can also be helpful on this GUI, as it can ensure that even during a pandemic such as COVID-19, students with disabilities would not be left behind and can still receive the same amount of education as their peers do.
There have been amazing developments using PyGame and PyGaze which are used as eye tracking games, these use an extra device which generally costs money. It would be amazing to apply the same concepts that I learned here to online gaming.
The eye tracker and GUI layout could be use in the future on phones, laptops and tablets. In the classroom, in school and for active learning it would be interesting to see the use of an eye tracker on the interactive whiteboard for students who cannot have direct interaction with it.
I hope to continuously work towards the development of this product in the future as I do believe in its ability to effectively help students with disabilities in their education. They deserve the right to a university education as well!
If there are any other developers who would like to use the code, I hope that they keep the original structure of the GUI and leave it for its intended purposes. Feel free to develop the code however you wish, this would be through making the mouse more dynamic and able to move to any point of the screen by gaze also improving the scroll functions and the looks of the main menus, instructions and settings menu.
References
Image on cover page Copyright Cavendish Press
Advancement Courses' Teacher Resources. 2020. 4 Types of Learners in Education | Advancement Courses. [online] Available at: <https://blog.advancementcourses.com/articles/4-types-of-learners-in-education/> [Accessed 31 May 2020].
Araujo, A., 2017. Eye Tracking for Mouse Control in OpenCV - Tango with Code. [online] Abnerrjo.github.io. Available at: <https://abnerrjo.github.io/blog/2017/01/28/eyeball-tracking-for-mouse-control-in-opencv/> [Accessed 6 June 2020].
Autism.org.uk. 2017. Classroom - National Autistic Society. [online] Available at: <https://www.autism.org.uk/professionals/teachers/classroom.aspx> [Accessed 31 May 2020].
Bristol.ac.uk. 2020. Interview Technique - The Structured Interview | Human Resources | University of Bristol. [online] Available at: <http://www.bristol.ac.uk/hr/resourcing/practicalguidance/selection/interviewtechnique.html> [Accessed 2 June 2020].
Christopherson, R., 2020. ‘Web Accessibility Guidelines’ Turn 10 But Still Less Than 10% Of Sites Are Accessible | Abilitynet. [online] Abilitynet.org.uk. Available at: <https://abilitynet.org.uk/news-blogs/web-accessibility-guidelines-turn-10-still-less-10-sites-are-accessible> [Accessed 31 May 2020].
Color-blindness.com. 2006. Deuteranopia – Red Green Color Blindness – Colblindor. [online] Available at: <https://www.color-blindness.com/deuteranopia-red-green-color-blindness/> [Accessed 31 May 2020].
Cyclone Mobility. 2018. Understanding the Types and Cause of Paralysis | Cyclone Mobility. [online] Available at: <https://www.cyclonemobility.com/understanding-the-types-and-cause-of-paralysis/> [Accessed 1 June 2020].
Dystoniacanada.org. 2015. Writer’S Cramp (Hand Dystonia) | Dystonia Medical Research Foundation Canada. [online] Available at: <https://dystoniacanada.org/about-dystonia/focal-dystonias/writer%E2%80%99s-cramp> [Accessed 31 May 2020].
Farnsworth, B., 2019. Eye Tracker Prices - An Overview Of 20+ Eye Trackers - Imotions. [online] imotions. Available at: <https://imotions.com/blog/eye-tracker-prices/> [Accessed 6 June 2020].
Fleming, N., 1987. Are You A Visual, Auditory, Reading/Writing, Or Tactile Learner? [online] Verywell Mind. Available at: <https://www.verywellmind.com/vark-learning-styles-2795156> [Accessed 31 May 2020].
GOV.UK. 2010. Equality Act 2010: Guidance. [online] Available at: <https://www.gov.uk/guidance/equality-act-2010-guidance> [Accessed 6 June 2020].
GOV.UK. 2013. Protection of Children's Biometric Information in Schools. [online] Available at: <https://www.gov.uk/government/publications/protection-of-biometric-information-of-children-in-schools> [Accessed 6 June 2020].
GOV.UK. 2018. Data Protection. [online] Available at: <https://www.gov.uk/data-protection#:~:text=The%20Data%20Protection%20Act%202018,Data%20Protection%20Regulation%20(GDPR).&text=They%20must%20make%20sure%20the,used%20fairly%2C%20lawfully%20and%20transparently> [Accessed 6 June 2020].
Hoffman, C., 2014. Why Third-Party Browsers Will Always Be Inferior to Safari on iPhone and iPad. [online] How-To Geek. Available at: <https://www.howtogeek.com/184283/why-third-party-browsers-will-always-be-inferior-to-safari-on-iphone-and-ipad/> [Accessed 2 June 2020].
Lauer, A., 2020. Factors in Assistive Technology Device Abandonment: Replacing “Abandonment” With “Discontinuance” - ATOMS Project. [online] R2d2.uwm.edu. Available at: <http://www.r2d2.uwm.edu/atoms/archive/technicalreports/tr-discontinuance.html> [Accessed 31 May 2020].
Nielsen, J., 1994. 10 Heuristics for User Interface Design: Article by Jakob Nielsen. [online] Nielsen Norman Group. Available at: <https://www.nngroup.com/articles/ten-usability-heuristics/> [Accessed 31 May 2020].
NORD (National Organization for Rare Disorders). 2020. Locked in Syndrome - NORD (National Organization for Rare Disorders). [online] Available at: <https://rarediseases.org/rare-diseases/locked-in-syndrome/> [Accessed 31 May 2020].
Opencv-python-tutroals.readthedocs.io. 2013. Face Detection Using Haar Cascades — Opencv-Python Tutorials 1 Documentation. [online] Available at: <https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html> [Accessed 2 June 2020].
Partnership on Employment & Accessible Technology (PEAT). 2020. Accessible Technology Vs. Assistive Technology. [online] Available at: <https://www.peatworks.org/talentworks/resources/accessible-vs-assistive> [Accessed 31 May 2020].
Perlstein, D., 2019. Motor Skills Disorder Interventions in Children & Adults. [online] eMedicineHealth. Available at: <https://www.emedicinehealth.com/motor_skills_disorder/article_em.htm> [Accessed 2 June 2020].
Pysource. 2019. Virtual Keyboard 3 - Gaze Controlled Keyboard with Python and Opencv P.7 - Pysource. [online] Available at: <https://pysource.com/2019/01/29/virtual-keyboard-3-gaze-controlled-keyboard-with-python-and-opencv-p-7/> [Accessed 2 June 2020].
Reeve Foundation. 2020. Depression. [online] Available at: <https://www.christopherreeve.org/living-with-paralysis/health/depression> [Accessed 1 June 2020].
Sandle, T., 2016. UN Thinks Internet Access Is A Human Right. [online] Business Insider. Available at: <https://www.businessinsider.com/un-says-internet-access-is-a-human-right-2016-7?r=US&IR=T> [Accessed 2 June 2020].
ScienceDaily. 2009. Computer Use Significantly Affected by Arthritis. [online] Available at: <https://www.sciencedaily.com/releases/2009/04/090430144733.htm> [Accessed 2 June 2020].
Selinger, E., 2015. Will Autocomplete Make You Too Predictable? [online] Bbc.com. Available at: <https://www.bbc.com/future/article/20150115-is-autocorrect-making-you-boring> [Accessed 1 June 2020].
Web Accessibility Initiative (WAI). 2019. Colors With Good Contrast. [online] Available at: <https://www.w3.org/WAI/perspective-videos/contrast/> [Accessed 31 May 2020].
Web Accessibility Initiative (WAI). 2020. Easy Checks – A First Review of Web Accessibility. [online] Available at: <https://www.w3.org/WAI/test-evaluate/preliminary> [Accessed 2 June 2020].
Who.int. 2018. Assistive Technology. [online] Available at: <https://www.who.int/news-room/fact-sheets/detail/assistive-technology> [Accessed 31 May 2020].
WLF. 2020. Undiagnosed Learning Disabilities and Low Literacy Rates in The U.S. - WLF. [online] Available at: <https://worldliteracyfoundation.org/undiagnosed-learning-disabilities-low-literacy-rates-us/> [Accessed 31 May 2020].
Appendix
Source Code: https://github.com/zuccbae/assistive-gui/tree/master
Project Presentation: https://web.microsoftstream.com/video/73bdaf85-d3a7-43bc-8830-c5a06d96ce3f
Meetings
Date	Main Comment	Checklist for the week	Done? (Y/N)
11/10/2019	You need to work some more on your resources for your literature review	1.	Journals
2.	Papers
3.	Conferences
4.	All from the last 5 years 
5.	Must have at least 20 resources to demonstrate deep study	1.	Y
2.	Y
3.	Y
4.	Y5.	Y
22/10/2019	Work on your literature review and explain why all of the medical study is relevant	6.	Link your research to your literature review and vice versa this would be good for comparison and contrasting	6.	Y
03/12/2019	Work on the structure of your report (VIVA)	7.	Place Abstract at the top when all work is done
8.	Move all of your images to the appendix and label them
9.	Label your tales
10.	Move all charts to the appendix
11.	Tables can stay
12.	Add the URL of your project in the abstract	7.	Y
8.	Y
9.	Y
10.	Y11.	Y12.	y
21/01/2020	Don’t forget to do contingency planning when you are writing your report	13.	Contingency planning	13. Y


05/02/2020	Think about testing when it comes to your project	14.	Blackbox testing
15.	Whitebox testing
16.	Error handling
17.	Population of charts
18.	User testing	14.Y
15. Y
16.Y
17. Y
18. N

19/03/2020	Think clearly about the future developments of your project and where it can be used	19.	E-learning
20.	Ecommerce
21.	Shopping and general browsing
22.	Blackboard Learn 
23.	Whiteboard interaction
24.	Converting the aspect ratio to work on tablets and phones.	19.Y
20.Y
21.Y
22.Y
23.Y
24.Y
17/04/2020	Think more deeply about the requirements you have written and make the significance of your requirements significant	25.	Usability requirements
26.	Feature requirements
27.	Add an extra column for the justification and verification for your requirements
28.	Evaluate against the requirements	25. N
26.N
27. Y
28. Y/N
11/05/2020	Explain your IED	29.	What IED?
30.	Explain the implication of the ethics
31.	Characteristics of improvements
32.	Explain how features were developed
33.	Future tests with people when the ethical reviews are successful.	29.Y
30. Y
31.N
32.Y
33.Y
Video Learning/E-learning (YouTube)
DJ OAMEN	https://www.youtube.com/watch?v=3PXfTTcLXqA&t=788s
(Keyboard)
PYSOURCE	https://www.youtube.com/watch?v=VWUgkcX_KoY&list=PL6Yc5OUgcoTlvHb5OfFLUJ90ofBuoU5g8 (Gaze Control)

THE NEW BOSTON	https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d (Tkinter positioning)

TWO BIT ARCADE	https://www.youtube.com/watch?v=D5nsMh2zmXk (Web Browser)

INFORMANIA	https://www.youtube.com/watch?v=cONDuZeYdzc (Video Stream)














Figures
Figure 1 – This is an image of a word cloud which demonstrates the common needs of people who suffer with disabilities and struggle from the effects of old age and learning difficulties. I have taken all these needs and created a requirement for such need which I can fit in the GUI. See Requirements.
 
















Figure 2 – This is a screenshot of the final product; it shows the layout of the final product in a single GUI window. There are two screens one of the splash screen (left) and one for the main window (bottom) 
 







Figure 3 – This shows the colour contrast of the keys on the keyboard, it passes the WCAG guidelines

Figure 4 – A demonstration of how the black texts looks on a white background on the keyboard
 

Figure 5 - This shows the colour contrast of the keys on the keyboard, when struck it passes the WCAG guidelines
 
Figure 6 – A demonstration of how the key looks like when it is struck
 


Figure 7 – OpenCV keyboard and output
 

Figure 8 – OpenCV keyboard
 



Figure 9 – Tkinter/tkinter keyboard and output
 
Abbreviations
LD	Learning Difficulty
OpenCV	Open Source Computer Vision
GUI	Graphical User interface
LIS	Locked-in Syndrome
UID	User Interface Design
WAI	Web Accessibility Initiative
WCAG	Web Content Accessibility Guidelines
OS	Open Source
CDRF	Christopher and Dana Reeve Foundation
NRAS	National Rheumatoid Arthritis Society
GBC	Gulf Bend Centre
UN	United Nations
IDE	Integrated Development Environment
	

