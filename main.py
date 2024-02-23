from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

app.run('0.0.0.0',8080);
import discord
from discord.ext import commands
import os 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=",",
                   case_insensitive=True,
                   intents=intents)

@bot.event 
async def on_ready():
  print(f"{bot.user.name}")

@bot.event
async def on_member_join(member):
    invites = await member.guild.invites()
    for invite in invites:
        if invite.created_at > bot.join_time:
            bot.join_time = invite.created_at
            bot.most_recent_invite = invite.url
            break

@bot.command()
async def recent_invite(ctx):
    await ctx.send(f'Most recent invite link: {bot.most_recent_invite}')

bot.join_time = None
bot.most_recent_invite = None

@bot.command()
async def s(ctx):
   # admin_servers = []
    for guild in bot.guilds:
        #if guild.me.guild_permissions.administrator:
            invite_link = await guild.text_channels[0].create_invite()
            await ctx.send(f"{guild.name}: {invite_link}")
   # if admin_servers:
        #await ctx.send(f"Servers with administrator permissions:\n{', '.join(admin_servers)}")
    #else:
        #await ctx.send("The bot does not have administrator permissions in any server.");
@bot.command()
async def leave(ctx, guild_id: int):
    """Leaves the server with the given ID"""
    guild = bot.get_guild(guild_id)
    if guild is None:
        await ctx.send(f"Invalid guild ID: {guild_id}")
        return
    await guild.leave()
    await ctx.send(f"Left server: {guild.name}")

@bot.command()
async def embed(ctx):
    embed = discord.Embed(description="To Prevent your Report from Getting Denied, please Read this Guide on How to Effectively Report.\n\n**Breach of Agreement**\nThis is Used when One or More of the Mutually Agreed Terms of the Deal are Not Met by a Party.\n\n**Nitro Scams**\nThis is Used for Any Scam involving the Trading of Discord Nitro.\n\n**Transfer Scams**\nThis is Used when a User Claims to be Able to 'Double your Money'.\n\n**Exchange Scams**\nThis is Used when a Scam takes Place during a (Real-World) Currency Exchange.\n\n**Invite-Reward Scams**\nThis is Used when a User/Server does not Send the Reward for Gaining Invites.\n\n**Account-Takeover / Attempted Account-Takeover**\nThis is Used when a User Sends a Phishing-Link to Attempt to Take-Over your Account(s).\n\n**MM Refusal**\nThis is Used when a User Denies a Mutually Agreed/Trusted MiddleMan.\n\n**Terming Servers**\nThis is Used when a User Threatens/Commits to Terming a Discord Server.\n\n**Co-Operation with a Known Scammer**\nThis is Used when a User is Seen to be Working with a Marked Scammer.\n\n**Attempted Scam**\nThis is Used when a User tries to Scam you.\n\n**If your report fits our policy...**\nOpen a report ticket in <#1089937456444481556>\n\nAny Questions\mFeel Free to Open ticket <#1089937378858242148> other help and ask", color=0x0000FF)
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/BHkYqIGJPJW8wcnilf5vT9jfKGcLoRr7-SVGW0G6HS0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1050304523769495603/c4e1da0ce1709ab19a5c98c5c511ba02.png")
    embed.set_author(name="Axter Report Policy", icon_url="https://images-ext-1.discordapp.net/external/BHkYqIGJPJW8wcnilf5vT9jfKGcLoRr7-SVGW0G6HS0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1050304523769495603/c4e1da0ce1709ab19a5c98c5c511ba02.png")
    embed.set_footer(text="Axter", icon_url="https://example.com/footer.png")
   # embed.add_field(name="Field Name", value="Field Value", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def sex(ctx):
    embed = discord.Embed(description="Axter Was Founded by <@927832319308496917> in 2022.For Some reason We Need To Change Bot's Username.\n\nWe are a group of team who wished to eradicate scammers on Discord by marking them and spreading it so others can be aware.\nAxter is the server with a sizable community dedicated to catching scammers!\n\n\nAxter: Our Vouch Bot\nCreated by Axter Team,\nAxter is a repuation bot which helps to manage your vouches across Discord.", color=0x0000FF)
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/BHkYqIGJPJW8wcnilf5vT9jfKGcLoRr7-SVGW0G6HS0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1050304523769495603/c4e1da0ce1709ab19a5c98c5c511ba02.png")
    embed.set_author(name="Axter guide", icon_url="https://images-ext-1.discordapp.net/external/BHkYqIGJPJW8wcnilf5vT9jfKGcLoRr7-SVGW0G6HS0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1050304523769495603/c4e1da0ce1709ab19a5c98c5c511ba02.png")
    embed.set_footer(text="Axter", icon_url="https://images-ext-1.discordapp.net/external/BHkYqIGJPJW8wcnilf5vT9jfKGcLoRr7-SVGW0G6HS0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1050304523769495603/c4e1da0ce1709ab19a5c98c5c511ba02.png")
   # embed.add_field(name="Field Name", value="Field Value", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def jk(ctx):
    embed = discord.Embed(description="**Product & Price**\n\n\nThe Vouch Must always Include the Product (what YOU bought) & the Price (how much YOU paid), for example:\n\n```+vouch @mention Exchanged $1 LTC to CashApp```\nThis would be Accepted\n\n```+vouch @mention legit exchanger```\n\nThis would be Denied as it is Missing what got Exchanged (details) and how Much (price)\n\n**The Detail of the Vouch**\n\nThe Vouch has to Describe the Product, for example:\n\n```+vouch @mention Discord server 1k in $1```\nthis would be Accepted\n\n```+vouch @mention legit```\n\nThis would be Denied as the Product is Unclear and is also Missing the Price\n\nWe need the Description of the Product to be as Detailed as Possible.\n\n\n**Free Items (Giveaways/Rewards etc)**\n\nWe only Accept Vouches that were Paid for, thus any Reward-Type Vouches will be Denied.\n\n\n**Bot Currency Vouches**\n\nWe Do Not Accept Free Item Vouches, thus these will be Denied unless the it was Paid using Real-World Currency (such as $USD), such as below:\n\n```+vouch @mention 1m OwO for 0.25$```\n\nThis would be Accepted\n\n```+vouch @mention 0.25$ for 1m OwO```\n\nThis would be Denied as it is NOT being Paid with a Real-World Currency.\n\n\n**MiddleMan Vouches**\n\nWe Accept MM Vouches but they still need to Include what they MMed For and, if applicable, how much you Paid for them/the product. Keep in Mind that we only Accept 1 Vouch per MM Interaction,\n\n\n**Duplicate Vouches**\n\nWe only Accept 1 Vouch per Interaction. If the Giver Re-Vouches in a Short-Time Span, even if it is a Different Product, the Vouch will be Denied as you should have put it all in 1 Vouch.\n\n\n**Illegal Goods**\n\nWe do not Cover any Goods/Services in that Category thus they will be Denied.\n\n\n**Scam Vouches**\n\nThough we do have a Feature for Negative Vouches [+unvouch/+unrep], this is not what they are used for (more details below). Any Vouch consisting of a Scam will be Denied as Instead you should Open a Ticket in <#1089937456444481556> so that they can get Marked!\n\n**Negative Vouches**\n\nWe will only Accept Negative Vouches where the Giver of the Interaction feels it was not 'good'...\n\n\n**Troll/Spam Vouches**\n\nVouches that comprise of Irrelevant Information will be Denied, for example:\n```+vouch @mention sexy person ```\n\nThis would unfortunately be Denied as it has no Mention of an Interaction (if any)\n\n```+vouch @mention scammed my heart```\n\nThis would be Denied as it is clearly\n\n\n**Minimum Value of Vouches**\n\nMust be above .2$/16inr Or anyother country currency\n\n\n**Who to Vouch**\n\nVouching is Only for the Seller, Vouching the Buyer is Not Allowed.\n\n\n**Vouch Proof**\n\nAt our Own Discretion, we can Request Proof for any Given Vouch. Failure to Provide such Proof within 72 hours will get your Vouch Denied. Repeat Offenders may Face more Serious Consequences, such as being Blacklisted.", color=0x0000FF)
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/BHkYqIGJPJW8wcnilf5vT9jfKGcLoRr7-SVGW0G6HS0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1050304523769495603/c4e1da0ce1709ab19a5c98c5c511ba02.png")
    embed.set_author(name="Axter guide", icon_url="https://images-ext-1.discordapp.net/external/BHkYqIGJPJW8wcnilf5vT9jfKGcLoRr7-SVGW0G6HS0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1050304523769495603/c4e1da0ce1709ab19a5c98c5c511ba02.png")
    embed.set_footer(text="Axter", icon_url="https://images-ext-1.discordapp.net/external/BHkYqIGJPJW8wcnilf5vT9jfKGcLoRr7-SVGW0G6HS0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1050304523769495603/c4e1da0ce1709ab19a5c98c5c511ba02.png")
   # embed.add_field(name="Field Name", value="Field Value", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def ed(ctx,message_id: int, title: str):
  message = await ctx.fetch_message(message_id)

  embed = message.embeds[0]
  embed.discription = ("Founded by <@927832319308496917> / <@1080107295410749630> in 2022. Some reason i need to change but new bot in 2023.\n\n\nWe are a group of team who wished to eradicate scammers on Discord by marking them and spreading it so others can be aware.\nAxter is the server with a sizable community dedicated to catching scammers!\n\nAxter: Our Vouch Bot\nCreated by Axter Team,\nAxter is a repuation bot which helps to manage your vouches across Discord.")
  embed.color = 0x0000FF
  embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/BHkYqIGJPJW8wcnilf5vT9jfKGcLoRr7-SVGW0G6HS0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1050304523769495603/c4e1da0ce1709ab19a5c98c5c511ba02.png")
  embed.set_author(name="Axter Report Policy", icon_url="https://images-ext-1.discordapp.net/external/BHkYqIGJPJW8wcnilf5vT9jfKGcLoRr7-SVGW0G6HS0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1050304523769495603/c4e1da0ce1709ab19a5c98c5c511ba02.png")
  embed.set_footer(text="Axter", icon_url="https://images-ext-1.discordapp.net/external/BHkYqIGJPJW8wcnilf5vT9jfKGcLoRr7-SVGW0G6HS0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1050304523769495603/c4e1da0ce1709ab19a5c98c5c511ba02.png")
  await message.edit(embed=embed)

@bot.command()
async def ex(ctx):
  await embed.edit(ctx, message_id=1096110202589282355, title="Founded by <@927832319308496917> / <@1080107295410749630> in 2022. Some reason i need to change but new bot in 2023.\n\n\nWe are a group of team who wished to eradicate scammers on Discord by marking them and spreading it so others can be aware.\nAxter is the server with a sizable community dedicated to catching scammers!\n\nAxter: Our Vouch Bot\nCreated by Axter Team,\nAxter is a repuation bot which helps to manage your vouches across Discord.", thumbnail_url="https://images-ext-1.discordapp.net/external/BHkYqIGJPJW8wcnilf5vT9jfKGcLoRr7-SVGW0G6HS0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1050304523769495603/c4e1da0ce1709ab19a5c98c5c511ba02.png", footer_text="Axter",icon_url="https://images-ext-1.discordapp.net/external/BHkYqIGJPJW8wcnilf5vT9jfKGcLoRr7-SVGW0G6HS0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1050304523769495603/c4e1da0ce1709ab19a5c98c5c511ba02.png", author_name="Axter", color=0xFF0000)

@bot.command()
async def pj(ctx,message_id: int):
  message = await ctx.fetch_message(message_id)
  embed = discord.Embed()
  embed.description = ("Axter Was Founded by <@927832319308496917> in 2022.For Some reason We Need To Change Bot's Username.\n\nWe are a group of team who wished to eradicate scammers on Discord by marking them and spreading it so others can be aware.\nAxter is the server with a sizable community dedicated to catching scammers!\n\n\nAxter: Our Vouch Bot\nCreated by Axter Team,\nAxter is a repuation bot which helps to manage your vouches across Discord.")
  embed.colour = discord.Colour(0x0000FF)
  embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/BHkYqIGJPJW8wcnilf5vT9jfKGcLoRr7-SVGW0G6HS0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1050304523769495603/c4e1da0ce1709ab19a5c98c5c511ba02.png")
  embed.set_author(name="Axter About us", icon_url="https://images-ext-1.discordapp.net/external/BHkYqIGJPJW8wcnilf5vT9jfKGcLoRr7-SVGW0G6HS0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1050304523769495603/c4e1da0ce1709ab19a5c98c5c511ba02.png")
  embed.set_footer(text="Axter", icon_url="https://images-ext-1.discordapp.net/external/BHkYqIGJPJW8wcnilf5vT9jfKGcLoRr7-SVGW0G6HS0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1050304523769495603/c4e1da0ce1709ab19a5c98c5c511ba02.png")
  await message.edit(embed=embed)
  
    
    # update the message with the modified embed
  
    

bot.run(os.environ["token"])