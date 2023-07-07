# UBC NAVI-BOT
Welcome to UBC NAVI-BOT, a Discord bot that facilitates UBC's degree navigation!

*This project started during the NwHacks hackathon that took place at the University of British Columbia (UBC) on January 2023.

## TEAM
- Khue Do - UX/UI designer
- Akira Kudo - developer
- Jessica Lescano - project lead & UX/UI designer
- Yu Cheng Li - developer

## PROBLEM STATEMENT
The UBC Academic Calendar, the official UBC website for degree-related information, provides an un-intuitive browsing experience to new users largely due to:
* Its composition from numerous web pages with varying degree of importance
* The presentation of information in a verbose manner
* A potentially misleading / hard-to-digest organization of course requirements
This can be confusing for freshman students planning their degree for the first time.

To tackle this problem, we set out to create a **Discord Bot** that provides users with crucial degree-related information **concisely** and under a **more user-friendly interface**. This project aims to empower students by offering them an alternative which speeds up and facilitates their degree planning process. 

## INSPIRATION
As a project for the NwHacks hackathon, we wanted to solve a problem we personally experienced as UBC students. During brainstorming, we all agreed on the confusing experience browsing the UBC Academic Calendar; from its verbosity, making it difficult to answer even simple questions, to unclear instructions on course requirements that obfuscated the true flexibility of freshman year planning. 

We believe this experienced is shared by many other students - as we observe the Science Advising queue to be very long at key periods of the year - many questions of which might be answered easily by students if the Academic Calendar were worded more accessibly.

We later also agreed on the user-friendlyness of Discord’s UI, from its clean layout to their feature integrations. Discord has grown in popularity to become a common messaging platform for students, and where class group chats often emerge. Consequently, many students are familiar with the social media and its user interface.

Inspired to make degree navigation painless for new students on a platform already familiar for them, our solution was to create ‘UBC NAVI-BOT’, a Discord Bot which offers a more user-friendly degree navigation experience. 

## OUR SOLUTION: ‘UBC NAVI-BOT’, THE UBC DEGREE NAVIGATION DISCORD BOT
UBC NAVI-BOT offers a simplified and concise version of the UBC Calendar, to be navigated using the Discord UI that students are more familiar with. 

Its goal is to give users a clear starting point to navigate their degree. 
* By condensing information found on the Academic Calendar, it aims to make absorbing information easier and answering arising questions straightforward.
* By modifying the headings from the official ones, it emphasizes the flexibility one has in degree planning.
For example, the wording "first year courses" in the official website had given one group member the impression that such courses were to be fulfilled during the first year of university (while in reality they can be completed at any time before the fourth year). We chose to name our pages x00-level courses instead (e.g. 200-level courses, rather than second year courses) to reflect this fact.

## HOW WE BUILT IT
**Technologies**: Discord API, Figma, Python, Replit.
* For **UX/UI design**, the flow of information and page layouts were planned using **Figma** - link to the file found here[
https://www.figma.com/file/tgbu7dXssxT3o8s4OA9D9c/nwHacks?type=design&node-id=0-1&mode=design&t=SUouCGoDgn0OrwmI-0 ].
* **Replit** allowed collaborative and simultaneous creation of the **back-end code**, which uses **Python** and its **Discord API library** to implement the bot. 
* The bot displays information into single pages at a time, which contain information about a group of similar requirements (such as Science Breadth Requirements). To move from page to page, the bot displays buttons with numbers indicating accessible pages, to be selected by clicking the corresponding reaction.
* For the back-end design, the bot creates a tree-structure that it populates with each nodes representing a single page. Each page information is stored in a JSON file. In order to allow for easy updates and scaling of the structure, the tree is built each time the bot is activated to mimic a folder-hierarchy which holds the JSON files. This way, changing the position of JSON files in the folders is directly reflected as a change to the displayed page structure.

To facilitate navigation, the following additional buttons are added:
1) "Home" button: takes you back to the initial page.
2) "Previous" button: takes you to the previous page visited. This is implemented using a stack.

## CHALLENGES
For most of us, this was our first hackathon, so we had to navigate how to work together as a team for the first time. The main challenge we faced during collaboration was working with two different devs; we had to reconcile two different ideas from both of our developers. Additionally, the designers had noticeably fewer responsibilities than the developers. The lack of communication between the teams led to time spent inefficiently, as developer responsibilities were not clearly communicated to the designers to help finish the back-end. The process of hard-coding the JSON files could have been automated if we had a JSON reader and writer program, which would further improve efficiency.

## ACCOMPLISHMENTS
Given that most of the team were first time hackers with limited experience, we are proud that we were able to build a functioning product at the end of the hackathon. In addition, a lot of our user testers said that they would use it and add it to their own Discord servers if it became fully developed. In particular, the UBC Computer Science Student Society (CSSS) president said that he would add it to their CSSS Discord once fully developed, as he saw the potential impact it can have for first years. 

## WHAT WE LEARNED
The process gave us some insights beneficial for team working skills. In particular, we learned the interplay between designers and developers, such as the benefit of building a common ground between the two parties for a smooth project progression. We learned the importance of communicating each other’s personal goals to help each other achieve them and efficiently complete the project in time. In addition, we learned what a hackathon looks like, which gives us insight into a situation where a team corporate project has to be completed under a small time crunch. Ultimately, this hackathon gave us valuable experience in how to effectively work in a team with our respective roles. 

## WHAT'S NEXT
The project is very much ongoing. The bot currently operates through the reaction functionality of the Discord API, but replacing this with the newer button functionality which is designed for smoother user experience would help us better achieve our goal to facilitate degree navigation, and would also conform with the functionality of prominent bots used actively in student communities (such as the DankMemer bot). 

Additionally, as the bot is limited to B.Sc. information about the two majors of Computer Science and Statistics, we are envisioning to gradually add additional majors to widen its reachable audience.

With the ultimate goal to offer a more user-friendly and accessible interface than its official counterpart, our project shall be further solidified by conducting UX research - gathering feedback from active users of the official website as well as our current prototype - in order to determine weaknesses of the Academic Calendar that our bot could complement. Combining such insights with further research on UI tools employable within the Discord API, or possible alternatives if the Discord UI functionality is limiting, would help us achieve our goal for a smoother user experience much more comfortably.
