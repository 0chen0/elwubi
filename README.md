# EL Wubi EL五笔输入法
自己定制一款五笔输入法。

之前不怎么在意输入法，也默认要用就下载极点五笔。

<br />

换到win10，系统有五笔输入法，也就‘原生派’地直接用系统五笔了。

win10刚出现时输入法不太好用，会有硬生生的延迟，网上也有说删除字库文件之类来“解决”的办法，看到评论回馈说有的可以有的不行，自己也没去试就放弃了使用。

之所以再用回来，是因为用系统的五笔的话，我就只需要一种语言一种输入法（也即是中文的五笔）就行了，但是用安装的输入法，必须得再添加多一个系统输入法放那（貌似当时是这样的情形）。强迫症，在一段时间的补丁后，我又用回系统的五笔。到这时其实系统五笔已经算可以正常用的阶段了。

然而，有两点小毛病在时间积累下还是让我产生了有没更好的选择的想法：

一个是shift键切换中英的反应非常恼人，有时极其敏感，稍微轻碰了下就给我切换了；有时却又不得不被它逼得慢下来：按了shift键切换后不能马上按其他键盘输入。想像一下，我打着中文临时想打英文词句，按shift键然后接着按其他字母键，发现没切换成功，于是又按一下shift键然后按其他字母键，发现又没切换成功，我再次按shift键然后按其他字母键：还未切换成功！！！我只好‘郑重其事地’按一下shift键，等上一秒时间，甚至再看一下状态栏右下角确认切换了，才开始按其他字母键。

这种情形经常发生，而且发生时经常是出现上面描述的那样，两三次都这样，没有夸张。

另一个还是shift键，玩某款全屏游戏，在游戏内聊天框打完字发送后，发现它会给我自动“按”着shift键，然后我按的其他按键，比如放技能按r键,按w键，就会变成按shift+r，按shift+w，我需要轻按一下shift键，它才会变回正常。

这两种情况都上网找过有没好的解决办法，前一种找不着，后一种有人也是这种情况，但也无法解决，只能“安装其他五笔输入法，就不会有这种情况”。 无奈

另外再吐槽一下：win10系统五笔的码表lex文件，想查看或转换成txt形式都难，找不到，github上找的转码表的软件都转不了。用了挺长一段时间字库文件有11MB了，结果却不能将这些自己平时输入积累下的习惯词库拿来用。

<br />

有段时间用谷歌拼音输入法来打五笔，跟系统五笔比起来，体验好多了。然而我不是拿它和系统五笔对比，是和RIME。

当时是在折腾RIME（windows平台的中文名叫小狼毫)，一款许多人赞叹的输入法。

应该挺多五笔输入者在用它，我也觉得它是一款很好的五笔输入法，而且希望它越来越好。

然而还是没有用它。

我用过它两次，一次是很早期（不记得多早）的时候，当时就谷歌到它了，但是使用时感觉会时不时随机性……崩溃？一个输入法会崩溃，这个在XP时经历过……

再一次还是被网上的安利吸引到去下载来用时，已经很好了，反应极好，输入舒适，智能，还有可设置选项多，界面还美观，bili blah……

我觉的这样先扬后抑不好，有坏心眼的感觉。但是下面说的事情其实对“rime是款好输入法”不太有影响，正常人看一下应该都知道是我的强迫症心理作祟，活受罪。

RIME的可定制选项多，我想真地可以掳获许多喜欢折腾人士的芳心，其实也是为什么自己想制作EL五笔：大概谁都会希望有一款感觉上像是属于自己的输入法。

RIME其实默认安装，选好输入类型，就可以用了。但是要让它相似于自己以往的输入环境的话，就得再作些设置。于是，我在间间断断折腾半天再加半天而无法在自己这个系统环境下解决下面这个问题后放弃：“实现在中文输入状态下，自由地打 ~ @ # % * 这几个符号时能直接上屏，偶尔想输入这些符号的各种变体或类似变体（即特殊符号）时又能用组合快捷键方便地打出来”

是的，我看了官方教程（没说详细看是因为官方教程没多少信息），又详细看了网上大部分人抄来抄去的通用教程，各种搜索另外找到的两位大神的两篇文章，然后近于“小心翼翼”地安装，修改设置，部署……

要实现上面的功能，初初想需要的设置是非常简单的。

然而总是不能如愿。烦的是出的问题不知道原因，无法应对解决。

一个短期时间段内重复装卸超过10次，RIME是当前为止我折腾时间最长的一款输入法。 我想也许是我的系统环境的问题，用不上它。

回到谷歌拼音输入法打五笔，相比较下，谷歌拼音当时给我的感觉真是太省心了，安装好马上用，似乎所有的设置都是自己习惯的设置，反应也一样快。只不过要用它来打五笔，得将五笔码表当成造词列表来导入，而且这样它对于五笔也就没有智能造词一说了；还有个谷歌账号同步的功能也不能用，，感到惋惜。

没有用谷歌是因为当时我没有去或者说不会去制作词表多一些的五笔码表，导致很多情况只能单字单字打。

<br />

谷歌拼音和极点貌似都是在win10出来之前就停止更新，虽然在win10上可以用。

QQ百度搜狗这些，不管功能怎么好，都不会考虑。然而词库有需要的话还是会下载。

<br />

说了一大通，好像要做个很牛逼的五笔输入法似的。 
不是的，上面说到的输入法，都是非常好用的输入法，甚至还有许多其他的也很好用；只是想说为什么有这么多好的五笔输入法，还要再折腾。想想自己某些方面的强迫症，应该会理解。

EL五笔只是一个自己做了自己用的五笔输入法，功能非常少；然而重要的是对我而言，够用，快速，契合自己的输入习惯，不为此烦心。

## 功能/特点
- 五笔 和 五笔+拼音反查
- 智能排序
- 个人造词
- 暂定
