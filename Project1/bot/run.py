from booking.booking import Booking
import random
word = ["我喜歡你","哈哈屁眼","早上好中國","你要吃冰機林嗎","我是gay","這是機器人","西我下面","我是機器人","我好帥","我超級大隻"]
with Booking() as bot:
    bot.login()


    bot.findpeople("丁茂峰")
    for i in range(1):
        bot.sendmessage(random.choice(word))
    print('Exiting ...')
    






