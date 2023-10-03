# autoForPhotoStudio
A script that manages folders for photo studios

This script creates folders under two main folders. One of those main folders is DAILY, under daily folders photographers upload their pictures according to month, day, and place information and if they have a special photoshoot they have a folder called by the photographer's name under the day folder. The other main folder is PRINT, under the PRINT file there is a month folder, and under that folder with date information. When a cashier sells some pictures he/she creates a new folder called the customer's room number under the date folder and puts the pics that have been sold to that customer in a folder.

Photographers' cameras have different name tags for saving so end of the day/month every photographer can check by simply searching for their name tag in a PRINT folder and comparing it with paper records. for example, Hugo's camera is saving pics as HUG_XXXX_XX or Eray's camera saving as ERY_XXXX_XX

Setup is pretty easy just put the .bat file in one of the server's harddisk and create a shortcut. press the Windows logo key + R, type shell:startup, then select OK. This opens the Startup folder. Move your shortcut there.

I'm a uni student and in the summertime, I started to work in this studio as a cashier. The cashier's main job is managing files, doing Photoshop, helping customers, and taking money of course. Managing files was time-consuming so I wanted to automate it somehow. The main difficulty for me I was not allowed to plug in any USB or download any program to the server so this is why I wrote in bash because the server is running on Windows and I only had windows's notepad. The first design in my head is pretty different I think I will create an example folder structure and script just copy and rename the dates. whit that style stido will have more freedom they can change the older structure by changing the example folder structure as they want without calling me.
