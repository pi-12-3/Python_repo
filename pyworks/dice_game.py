import dice

choice=int(input('4,6,8,12,20のどれで勝負しますか？：'))

cpu_sai=dice.Dice(choice)
your_sai=dice.Dice(choice)

cpu_ans=cpu_sai.shoot()
your_ans=your_sai.shoot()

print('CPU：{} / あなた：{}'.format(cpu_ans,your_ans))

if cpu_ans > your_ans:
    print('残念。あなたの負けです')
elif cpu_ans < your_ans:
    print('おめでとう。あなたの勝ちです')
else:
    print('引き分けです')
