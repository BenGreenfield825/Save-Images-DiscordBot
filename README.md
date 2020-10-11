# Save Images with a DiscordBot
 A simple bot that shows how to save an image from discord chat 
 
 ## Usage
 When uploading an image to discord, add ```.save``` in the comment box to tell the bot to save the image.\
 **This program does not check for having multiple images.**\
 **_This will not check to make sure the attachment is actually an image!!! This is a possible security issue - be careful!_**
 
 ## Update
 After doing more work on a project I realized that there is actually a built in method to save attachments (definitely a facepalm moment). If you want to use the built in method you should use something like this:\
 ```await ctx.message.attachments[0].save('image.jpg')```\
 You would use this instead of what's inside the else block on the example code I posted (you would probably want to change that whole setup too, but you get the idea). My code still works fine, but this is just the built in and probably more official/efficient way of doing things. ***Still be careful of possible security issues if using either of these methods on a public server or any server.***\
 **-Added another example file to show this method**
 
 ## Info
 I'm currently working on a project where I wanted to be able to have a bot save an image from chat and do some processing to it (Object-Detection). I couldn't find any great examples that showed how to do this (especially in python), but I managed to find a simple example from stackoverflow that I fixed up and edited (shout out and original credit goes to here -> https://stackoverflow.com/questions/55886443/bot-saving-every-image-gif-or-video-sent-in-a-specific-channel-on-discord).
 
 A lot of this was new to me also, so I added some comments giving quick descriptions of what was happening as I learned. Hopefully this helps out anyone else who is interested like I was. 
 
 I now also have a YouTube video on this topic! Watch it here: https://www.youtube.com/watch?v=pgmUBOV3IIs
