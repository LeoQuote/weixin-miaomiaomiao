# 导入模块
from wxpy import *
import random
# 初始化机器人，扫码登陆

def miaomiaomiao(content):
    print(content)
    emoji_list = ['(゜-゜)','(=`ｪ´=；)ゞ','(;´༎ຶД༎ຶ`)','⁄(⁄⁄•⁄ω⁄•⁄⁄)⁄','(´･_･`)','(｀∀´)','(:3[▓▓▓]','（╯‵□′）╯︵┴─┴','₍•͈˽•͈₎','∠( ᐛ 」∠)＿','(*ﾉωﾉ)','ヾ(*>∀＜*) ','(ฅωฅ*)','<(￣︶￣)/ ','(´⊙ω⊙`)','(๑•̀ω•́๑)','(≧∀≦)♪','(*/∇＼*)','(｡･ω･｡)ﾉ♡','( • ̀ω•́ )✧','(☆ω☆)','╮(￣⊿￣")╭','(′へ`、)','(ﾟﾛ ﾟﾉ)ﾉ','(*｀▽´*)','Ծ‸Ծ']
    if '喵喵' in content or '猫猫' in content:
        sig_choices = ['？','！','~','~~~','？？？','？！','！！！']
        miao_count = random.randrange(3,15)
        reply_list = ['喵'] * miao_count
        sig_count = random.randrange(0,miao_count-2)
        emoji_count = random.randrange(0,2)
        if emoji_count == 0:
            emoji = ''
        else:
            emoji = random.choice(emoji_list)
        reply_list += [emoji]
        for i in range(sig_count+1):
            reply_list += [random.choice(sig_choices)]
        random.shuffle(reply_list)
        return ''.join(reply_list)
 
if __name__ == '__main__':
    bot = Bot(console_qr=True)
    bot.file_helper.send('微信机器人已成功登录')
    listening_group = ensure_one(bot.groups().search('test_group'))
    fans_group = ensure_one(bot.groups().search('同好会'))
    @bot.register(chats=[listening_group,fans_group],except_self=False,msg_types=TEXT)
    def test_group_auto(msg):
        return miaomiaomiao(msg.text)
    embed()
    
