# UBC-stack-BOT
Welcome to NAVI-BOT, a Discord bot that facilitates UBC's degree navigation!
### PROBLEM STATEMENT
The UBC Academic Calendar has an un-intuitive layout due to:
Its composition from numerous web pages with varying degree of importance
The presentation of information in a verbose manner resulting in slower navigation
A potentially misleading organization of course requirements
This can be confusing for freshman students planning their degree for the first time.
We set out to create a Discord Bot that is user-friendly to anyone who isn’t familiar with the academic calendar so that confusion is minimized. This could empower the students by facilitating their planning process, thereby giving them a stronger idea of the amount of flexibility that their degree allows. 

### INSPIRATION
We wanted to solve a problem that we personally have encountered. During our brainstorming session, we ended up bonding over how confusing the UBC Calendar is, from how hard it is to answer a simple question due to the lengthy pages and our regrets of not knowing how flexible our first year of university could have been. These issues can cause Science Advising queues to be very long and full of small and easily answered questions when wording the UBC Calendar differently. 
We later bonded over how user-friendly Discord’s UI is, from its clean layout to their feature integrations. Discord has grown in popularity to become a common messaging platform and a place where class group chats often emerge. 
With these two issues combined, we made ‘NAVI-BOT’, our solution to make UBC degree navigation easier. 

### TEAM
- Khue Do - UX/UI designer
- Akira Kudo - developer
- Jessica Lescano - project lead & UX/UI designer
- Yu Cheng Li - developer

### OUR SOLUTION: ‘NAVI-BOT’, THE UBC DEGREE NAVIGATION DISCORD BOT
NAVI-BOT displays a simplified, more concise version of the UBC Calendar on the familiar Discord UI. It gives users a clear starting point to help them begin to navigate their degree, condenses the wording of the UBC Calendar to give straightforward answers to simple questions, and encourages flexibility in degrees by changing the headings. We chose to name our pages x00-level courses instead of x year courses to emphasize that the courses just need to be fulfilled at some point in order to graduate rather than giving the impression that 100-level courses must be fulfilled in the first year of university. Ultimately, NAVI-BOT minimizes the intimidation of degree planning. 

### HOW WE BUILT IT
The technologies used for this project were Python, Discord API, Figma, and Replit. For the UX/UI design, the layout of the pages and flow of information was planned on Figma. Replit was used for the developers to collaboratively and simultaneously code the back-end using Python and the Discord API. The back-end design for this project was a tree composed of hard-coded JSON files, with each representing a different page. Below is a link to the Figma file. 
https://www.figma.com/file/tgbu7dXssxT3o8s4OA9D9c/nwHacks?type=design&node-id=0-1&mode=design&t=SUouCGoDgn0OrwmI-0 

### CHALLENGES
For most of us, this was our first hackathon, so we had to navigate how to work together as a team for the first time. The main challenge we faced during collaboration was working with two different devs; we had to reconcile two different ideas from both of our developers. Additionally, the designers had noticeably fewer responsibilities than the developers. The lack of communication between the teams led to time spent inefficiently, as developer responsibilities were not clearly communicated to the designers to help finish the back-end. The process of hard-coding the JSON files could have been automated if we had a JSON reader and writer program, which would further improve efficiency.

### ACCOMPLISHMENTS
Given that most of the team were first time hackers with limited experience, we are proud that we were able to build a functioning product at the end of the hackathon. In addition, a lot of our user testers said that they would use it and add it to their own Discord servers if it became fully developed. In particular, the UBC Computer Science Student Society (CSSS) president said that he would add it to their CSSS Discord once fully developed, as he saw the potential impact it can have for first years. 

### WHAT WE LEARNED
The process gave us some insights beneficial for team working skills. In particular, we learned the interplay between designers and developers, such as the benefit of building a common ground between the two parties for a smooth project progression. We learned the importance of communicating each other’s personal goals to help each other achieve them and efficiently complete the project in time. In addition, we learned what a hackathon looks like, which gives us insight into a situation where a team corporate project has to be completed under a small time crunch. Ultimately, this hackathon gave us valuable experience in how to effectively work in a team with our respective roles. 


### WHAT'S NEXT
The project is very much ongoing. The bot currently operates through the reaction functionality of the Discord API, but replacing this with the newer button functionality which is designed for smoother user experience would help us better achieve our goal to facilitate degree navigation, and would also conform with the functionality of prominent bots used actively in student communities (such as the DankMemer bot). Additionally, as the bot is limited to B.Sc. information about the two majors of Computer Science and Statistics, we are envisioning to gradually add additional majors to widen its reachable audience.
With the ultimate goal to offer a more user-friendly and accessible interface than its official counterpart, our project shall be further solidified by conducting UX research - gathering feedback from active users of the official website as well as our current prototype - in order to determine weaknesses of the Academic Calendar that our bot could complement. Combining such insights with further research on UI tools employable within the Discord API, or possible alternatives if the Discord UI functionality is limiting, would help us achieve our goal for a smoother user experience much more comfortably.





