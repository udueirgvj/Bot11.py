import telebot
bot = telebot.TeleBot('7618720746:AAGMHVkVBkPvKcatWdT7esRO3tcbA2EvIn4')


@bot.message_handler(func=lambda m : True)
def m(m):
	if m.text=="هلو":
		bot.reply_to(m,"ههلا.")
	elif m.text=="باي":
		bot.reply_to(m,"ون.")
	elif m.text=="صباح الخير":
			bot.reply_to(m,".صباඋ النوࢪ 😻")
	elif m.text=="هاي":
			bot.reply_to(m,".هايات يعمࢪي 💖")
	elif m.text=="شلونك":
			bot.reply_to(m,"تمام وانت 🌹")
	elif m.text=="احبك":
			bot.reply_to(m,"جذب تحب عشره عليك")
	elif m.text=="احبج":
			bot.reply_to(m,"امشي لك زاحف 😒")
	elif m.text=="نجب":
			bot.reply_to(m,"نجب انت لك ادبسز")
	elif m.text=="اكلك":
		bot.reply_to(m,"كول عمري ")
	elif m.text=="شوكت تجي":
		bot.reply_to(m,"من تروح انت 😒😒✋،!!¿.")
	elif m.text=="بوت":
		bot.reply_to(m,"اسمي ↫ 𝐒𝐀𝐃𝐑𝐄 افتهم عادد")
	elif "حسابي" in m.text or "حسابج" in m.text or "حساب"in m.text:
		bot.reply_to(m,"شنو طار ؟؟")#جمع الاوامر 

	elif m.text=="السلام عليكم":
		bot.reply_to(m,"عليكم السلام ورحمة الله 😻")
	elif m.text=="مور":
		bot.reply_to(m,"ﻣﻣح")
	elif m.text=="شكرا":
		bot.reply_to(m,"دلࢦـَِ.")
	elif m.text=="🥺":
		bot.reply_to(m,"ڪيوت.")
bot.polling()	