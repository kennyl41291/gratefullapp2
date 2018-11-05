import datetime,random, os, schedule, time

from twilio.rest import Client
from pathlib import Path

class Greatfulapp:

	def hasTheAppRun(self):
		my_file = Path("log.txt")
		if my_file.is_file():
			print('Log file exists')
			# setting time stamp
			todays_date = 'Text message sent on: {:%Y-%b-%d}'.format(datetime.datetime.now())
			#
			with open('log.txt','r') as fread:
				#Reads the last timestamp
				last_line = fread.readlines()[-1]
				if last_line != todays_date:
					with open('log.txt','a') as fappend:
							fappend.write("\n" + todays_date)
					print ('Sending a text now!')
					self.textFunction()
					print ('Sent!')
					os.system("log.txt")
				else:
					print('Your daily gratitude text was already sent today')
		else:
			f= open("log.txt","w")
			todaysDate = 'Text message sent on: {:%Y-%b-%d}'.format(datetime.datetime.now())
			f.write(todaysDate)
			print('Just created a new file')
			print ('Sending a text now!')
			self.textFunction()
			print ('Sent!')

	def textFunction (self):
		# put your own credentials here
		quotes = ['"Ability is what you\'re capable of doing.\nMotivation determines what you do.\nAttitude determines how well you do it."', '"A great attitude becomes a great day, which becomes a great month, which becomes a great year, which becomes a great life."', '"All our dreams can come true - if we have the courage to pursue them."', '"All things are difficult before they are easy."', '"Always be a first-rate version of yourself, instead of a second-rate version of somebody else."', '"Always dream and shoot higher than you know you can do. Don\'t bother just to be better than your contemporaries or predecessors. Try to be better than yourself."', '"Always remember:\nYou\'re braver than you believe,\nstronger than you seem,\nand smarter than you think."', '"A man is but of product of his thought.\nWhat he thinks he becomes."', '"And will you succeed? Yes indeed, yes indeed! Ninety-eight and three-quarters percent guaranteed!"', '"Anyone who has never made a mistake has never tried anything new."', '"A person will only leave their comfort zone once they decide that magic and adventure outweigh complete certainty and security."', '"A problem is a chance for you to do your best."', '"A ship in harbor is safe - but that is not what ships are built for."', '"A strong positive mental attitude will create more miracles than any wonder drug."', '"Beautiful pictures are developed from negatives in a dark room. So if you see darkness in your life be reassured that a beautiful picture is being prepared."', '"BE YOU:\nBE-LIEVE IN\nYOU-RSELF"', '"Change brings opportunity."', '"Confidence is contagious. So is lack of confidence."', '"Courage is very important. Like a muscle, it is strengthened by use."', '"Don\'t be afraid to be amazing."', '"Don\'t be afraid to give your best to what seemingly are small jobs. Every time you conquer one it makes you that much stronger. If you do the little jobs well, the big ones will tend to take care of themselves."', '"Don\'t cry because it\'s over. Smile because it happened."', '"Don\'t give up. I believe in you all.\nA person\'s a person no matter how small."', '"Don\'t let your fear of what could happen make nothing happen."', '"Don\'t lower your expectations to meet your performance. Raise your level of performance to meet your expectations. Expect the best of yourself, and then do what is necessary to make it a reality."', '"Don\'t tell me the sky\'s the limit when there are footprints on the moon."', '"Do you want to play it safe and be good or do you want to take a chance and be great?"', '"Dreams come a size too big so that we can grow into them."', '"Energy and persistence conquer all things."', '"Every great dream begins with a dreamer. Always remember, you have within you the strength, the patience, and the passion to reach for the stars to change the world."', '"Everyone has inside of him a piece of good news. The good news is that you don\'t know how great you can be! How much you can love! What you can accomplish! And what your potential is!"', '"Excellence is not a skill. It is an attitude."', '"Far and away the best prize that life offers is the chance to work hard at work worth doing."', '"Give thanks for unknown blessings already on their way."', '"I can accept failure, everyone fails at something. But I can\'t accept not trying."', '"I can\'t change the direction of the wind, but I can adjust my sails to always reach my destination."', '"If ever there is a tomorrow when we\'re not together, there is something you must always remember: You are braver than you believe, stronger than you seem, and smarter than you think."', '"If things start happening, don\'t worry, don\'t stew, just go right along and you\'ll start happening too."', '"If we did all the things we are capable of, we would literally astound ourselves."', '"If you can dream it, you can do it."', '"If you can imagine it, you can create it. If you can dream it, you can become it."', '"If you have the power to make someone happy, do it. The world needs more of that."', '"If you\'re tired of starting over, stop giving up."', '"If you think you can do a thing, or think you can\'t do a thing; you\'re right."', '"If you try to do your best there is no failure."', '"If you want the best the world has to offer, offer the world your best."', '"I have not failed. I\'ve just found 10,000 ways that won\'t work."', '"I hope when you count the stars you begin with yourself, and may you embrace the moonlight with your dreams."', '"Impossible is a word to be found only in the dictionaries of fools!"', '"In the middle of difficulty lies opportunity."', '"In order to be big, you have to think big.\nIf you think small, you\'re going to be small."', '"In your dreams, anything is possible. It\'s time to wake up and start dreaming."', '"It does not matter how slowly you go as long as you do not stop."', '"It\'s amazing what one can accomplish when one doesn\'t know what one can\'t do."', '"It\'s time to break out of your shell and show the world who you really are and what you\'re really made of! Live your dreams!"', '"I\'ve got a theory that if you give 100 percent all of the time, somehow things will work out in the end."', '"I\'ve heard tell that what you imagine sometimes comes true."', '"Kites rise highest against the wind, not with it."', '"Life begins at the end of your comfort zone."', '"Life shrinks or expands in proportion to one\'s courage."', '"Life\'s problems wouldn\'t be called hurdles if there wasn\'t a way to get over them."', '"Little by little one walks far."', '"Men often become what they believe themselves to be. If I believe I cannot do something, it makes me incapable of doing it. But when I believe I can, then I acquire the ability to do it even if I didn\'t have it in the beginning."', '"Never let the fear of striking out keep you from playing the game."', '"Ninety-nine percent of people believe they can\'t do great things, so they aim for mediocrity."', '"Nothing can add more power to your life than concentrating all your energies on a limited set of targets."', '"Nothing is overly hard if you divide it into small jobs."', '"Now and then it\'s good to pause in our pursuit of happiness and just be happy."', '"Only those who will risk going too far can possibly find out how far one can go."', '"Only you can control your future."', '"Praise, like gold and diamonds, owes its value only to its scarcity."', '"Reach high, for stars lie hidden in your soul. Dream deep, for every dream precedes the goal."', '"Remember that guy that gave up? Neither does anybody else."', '"Shoot for the moon. Even if you miss,\nyou will land among the stars."', '"So be sure when you step, Step with care and great tact. And remember that life\'s a great balancing act. And will you succeed? Yes! You will, indeed! (98 and 3/4 percent guaranteed) Kid, you\'ll move mountains."', 'Success =\nSee your goal.\nUnderstand the obstacles.\nCreate a positive mental picture.\nClear your mind of doubt.\nEmbrace the challenge.\nStay on task.\nShow the world you can do it.', '"Talent is never enough. With few exceptions the best players are the hardest workers."', '"Tears are like rain. They loosen up our soil so we can grow in different directions."', '"That\'s one small step for man, one giant leap for mankind."', '"The best angle from which to approach any problem is the try-angle."', '"The difference between try and triumph is a little umph."', '"The greater danger for most of us lies not in setting our aim too high and falling short; but in setting our aim too low, and achieving our mark."', '"The greatest discovery of all time is that a person can change his future by merely changing his attitude."', '"The man who has no imagination has no wings."', '"The only thing worse than being blind is having sight but no vision."', '"There are no footsteps to follow on your own path ... but that\'s where the fun and adventure live."', '"There is no elevator to success. You have to take the stairs."', '"There is no one giant step that does it. It\'s a lot of little steps."', '"The secret of getting ahead is getting started. The secret of getting started is breaking your complex overwhelming tasks into small manageable tasks, and then starting on the first one."', '"The shell must break before the bird can fly."', '"The way to get started is to quit talking and begin doing."', '"They are able because they think they are able."', '"To climb steep hills requires a slow pace at first."', '"Today I shall behave, as if this is the day I will be remembered."', '"Today is your day, your mountain is waiting. So get on your way."', '"Try and fail, but don\'t fail to try."', '"Twenty years from now you will be more disappointed by the things that you didn\'t do than by the ones you did so. So throw off the bowlines. Sail away from the safe harbor. Catch the trade winds in your sails. Explore. Dream. Discover."', '"Unless you try to do something beyond what you have already mastered, you will never grow."', '"We aim above the mark to hit the mark."', '"What would you attempt to do if you knew you would not fail?"', '"When one door closes, another opens; but we often look so long and so regretfully upon the closed door that we do not see the one which has opened for us."', '"When you think things are bad,\nwhen you feel sour and blue,\nwhen you start to get mad...\nyou should do what I do!\nJust tell yourself, Duckie,\nyou\'re really quite lucky!\nSome people are much more...\noh, ever so much more...\noh, muchly much-much more\nunlucky than you!"', '"You are the only person on earth who can use your ability."', '"You can do it if you believe you can."', '"You cannot be lonely if you like the person you\'re alone with."', '"You have brains in your head. You have feet in your shoes. You can steer yourself in any direction you choose."', '"You may have a fresh start any moment you choose, for this thing we call failure is not the falling down, but the staying down."', '"You must find the place inside yourself where nothing is impossible."', '"You\'re off to Great Places! Today is your day! Your mountain is waiting, so... get on your way!"', '"Your mind is a garden. Your thoughts are the seeds. You can grow flowers or you can grow weeds."', '"Your present circumstances don\'t determine where you can go; they merely determine where you start."']
		account_sid = "AC3d4abd2cf3a83c68211c223d0cce0636"
		auth_token = "47219566f1d56c2e79442358f5ab1d17"
		client = Client(account_sid, auth_token)
		client.messages.create(
		  to="+13475069537",
		  from_="+13479346820",
		  body="\n----------------\n" + random.choice(quotes) + "\n----------------\n" +"Can you please tell me what are the 3 things you are greatful about?")

	def retrieveResponseList (self):
		# Your Account Sid and Auth Token from twilio.com/console
		account_sid = "AC3d4abd2cf3a83c68211c223d0cce0636"
		auth_token = "47219566f1d56c2e79442358f5ab1d17"
		client = Client(account_sid, auth_token)

		messages = client.messages.list()

		# RAW and unfilter list of received txt msgs (incl sent and received tests)
		rawMessages = []
		# Displays complete log for twilio messages
		debuggMessageLog = []
		# Cleaning garbage with the below for loop
		for record in messages:
		    # print(record.body)
		    if 'Sent from your Twilio trial account' not in record.body:
		    	debuggMessageLog.append(record.body)
		    	if 'Really?' not in record.body:
		    		rawMessages.append(record.body)

		# Formatting my list of appreciation
		preRawMessages = ". ".join(rawMessages)
		txtMessages = preRawMessages.split(". ")
		txtMessages.reverse()

		# Clearing up some 
		txtMessages = txtMessages[3:]

		print('The list of things you have been greatful about')
		print('------------------------------------')
		print(*txtMessages, sep = "\n")
		# print (rawMessages)
		# print (txtMessages)


##################################################################################
KennyGreatful = Greatfulapp()
# KennyGreatful.hasTheAppRun()
KennyGreatful.retrieveResponseList()


#End of text application