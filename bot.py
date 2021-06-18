import discord
import random
client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:                                                           #we do not want the bot to reply to itself
        return
    
    if message.content.startswith('!'):                                                         #command's prefix, so the bot knows the message author wants something from him
        msg = message.content                                                                   #Assign the message to a string variable "msg"

        
        #display user's roles
        if "my roles" in msg[:9].lower():
            for i in range(1, len(message.author.roles)):
                await client.send_message(message.channel, message.author.roles[i])

        
        #add role to a user
        elif "add" in msg[:5].lower():
            roleName = msg[5:]                                                                  #extract the role user wants to get
            role = discord.utils.get(message.author.server.roles, name=roleName)                #iterate through server's roles and find the role player wants to get
            alreadyHasRole = False                                                              #bool for checking if the player doesn't already have the role he wants to add

            #itearate through user's roles
            for i in range(1, len(message.author.roles)):
                if message.author.roles[i] == role:
                    alreadyHasRole = True
                    break

            if alreadyHasRole:                                                                  #Inform the user he already has the role he tries to get
                await client.send_message(message.channel, f"You already have the role: {role}")

            if alreadyHasRole == False:                                                         #add role to the user if he doesn't have it      

                #iterate through server's roles
                for i in range (0, len(message.author.server.roles)):
                    if message.author.server.roles[i].name == roleName:                         #check if the role user wants exists
                        try:                                                                    #an error is thrown if the role doesn't exist
                            await client.add_roles(message.author, role)                        #add the role
                            await client.send_message(message.channel, f"Role added: {role}")   #inform that the role was granted
                            break
                        except:
                            await client.send_message(message.channel, f"You don't have permissions for role '{role}'.")
                            break
                    if i == len(message.author.server.roles)-1:                                 #inform the user the role he tries to get doesn't exist
                        await client.send_message(message.channel, f"There is no role named '{roleName}'. Make sure that the role exists, that size of the letters is correct and that there are no multiple spaces. If you are sure that you typed the role correctly and you keep seeing this message, please contact any Admin to get the role, and contact Mano to let him know about the bot issue.")

        
        #display all available roles the user can get
        elif "all roles" in msg[:10].lower():
            for i in range (1, len(message.author.server.roles)):                               #iterate through server's roles
                if message.author.server.roles[i].name == "Worker" or message.author.server.roles[i].name == "Member" or message.author.server.roles[i].name == "Bloodflags Project" or message.author.server.roles[i].name == "Sia's Projects" or  message.author.server.roles[i].name == "new role" or message.author.server.roles[i].name == "Navy Seal" or message.author.server.roles[i].name == "Rythm" or message.author.server.roles[i].name.lower() == "the horde's last hope" or message.author.server.roles[i].name == "Testify" or message.author.server.roles[i].name == "Dark Music Bot" or message.author.server.roles[i].name == "Bot" or message.author.server.roles[i].name == "Admin" or message.author.server.roles[i].name == "Sia":
                    continue
                await client.send_message(message.channel, message.author.server.roles[i].name)


        #display all available commands
        elif "help" in msg[:6].lower():
            await client.send_message(message.channel, "Use '!' at the beginning to call me. Commands: \n!all roles - display all available roles you can get \n!my roles - display your current roles \n!add [role name] - add a role to yourself \n!remove [role name] - remove one of your roles \n!help - display this message \n")


        #remove a role from user
        elif "remove" in msg[:8].lower():
            roleName = msg[8:]                                                                  #extract the role user wants to remove
            role = discord.utils.get(message.author.server.roles, name=roleName)                #iterate through server's roles and find the role user wants to remove
            isRole = False                                                                      #bool for determing if the user has the role he wants to remove

            #itearate through user's roles
            for i in range(1, len(message.author.roles)):
                if message.author.roles[i] == role:
                    isRole = True
                    break
            
            if isRole == False:                                                                 
                if role == None:                                                                #Inform the user the role he want to remove doesn't exist
                    await client.send_message(message.channel, f"Role '{roleName}' doesn't exist")
                else:                                                                           #Inform the user he doesn't have the role he wants to remove
                    await client.send_message(message.channel, f"You don't have a role named: {role}")
                
            if isRole:                                                                          #Perform removal if the user has the role he tries to remove
                
                #iterate through server's roles
                for i in range (0, len(message.author.server.roles)):                           #check if the role player wants exists
                    if message.author.server.roles[i].name == roleName:
                        if roleName == "Admin" or roleName == "Sia's Projects" or roleName == "Sia":
                            await client.send_message(message.channel, f"You can't remove role: {role}")
                            break
                        try:
                            await client.remove_roles(message.author, role)                     #remove the role
                            await client.send_message(message.channel, f"Role removed: {role}") #inform that the role was removed
                            break
                        except:                                                                 #Inform the user the role he tries to remove doesn't exist
                            await client.send_message(message.channel, f"There is no role named '{role}'.") 
                
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')