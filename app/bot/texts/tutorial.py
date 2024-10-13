epigraph = """
За пределами пространства и времени, за бесчисленными поворотами и смертельными ловушками темного лабиринта Фанг тебя поджидают неизъяснимые ужасы и опасности. Порожденный дьявольской думой барона Сукумвита, лабиринт населен кровожадными монстрами, встреча с которыми сулит тебе лишь одно - СМЕРТЬ, если только ты недостаточно смел, недостаточно силен, недостаточно искусен и удачлив.\n
Так посмеешь ли ты войти в разверстую пасть страшного лабиринта, чтобы, быть может, остаться там навеки или же, испытав множество захватывающих приключений, получить сказочную награду, за которой кроме тебя охотятся еще пятеро бывалых воинов? И лишь один из вас сможет победить в этой схватке - остальным уготована гибель. Но КТО именно?\n
Множество опасностей поджидает тебя, и непрост будет твой путь к победе и заслуженной награде. Тебе встретятся страшные противники, и зачастую у тебя будет лишь один выбор - УБИТЬ или УМЕРЕТЬ самому!\n
"""

potion_choice = """
Ты отправляешься в путь, имея в распоряжении лишь самое необходимое снаряжение, но в ходе путешествия ты будешь находить разные полезные вещи. Ты вооружен мечом и щитом, одет в кожаную рубаху, за плечами у тебя мешок с провиантом, в который ты будешь складывать добытые сокровища.\n
Кроме того, с собой ты можешь взять бутыль с волшебным напитком, который окажет тебе помощь в странствиях. Ты можешь выбрать одну из трех бутылей:\n
Напиток Мудрых - восстанавливает уровень твоего МАСТЕРСТВА;\n
Напиток Сильных - восстанавливает уровень твоей ВЫНОСЛИВОСТИ;\n
Напиток Удачливых - восстанавливает уровень твоей УДАЧЛИВОСТИ, а ее начальное значение увеличивает на 1.\n
Ты можешь принять напиток в любой момент, только не тогда, когда тебя вызывают на битву. Учти, что каждая бутыль содержит напиток лишь на один прием, т.е. твои МАСТЕРСТВО, ВЫНОСЛИВОСТЬ и УДАЧЛИВОСТЬ могут быть восстановлены лишь один раз за все путешествие!\n
Напоминаем еще раз: в дорогу ты можешь взять лишь одну бутыль из трех, так что хорошенько подумай, перед тем как сделать выбор.\n
"""

prolog = (
"Когда-то Фанг был маленьким захолустным городком в северной провинции Чанг Май. Расположенный на берегу реки Кок, он круглый год служил удобным перевалочным пунктом для речных торговцев и немногочисленных путешественников. К его пристани пришвартовывались плоты, барки, а изредка даже небольшие шхуны. Но все это было давно - еще до постройки Лабиринта Страха, еще когда не было Состязания Великих. Теперь же раз в году вся река перед причалом бывает запружена лодками, привозящими из соседних городов, провинций и даже, говорят, из-за границы, тысячи и тысячи зрителей, желающих во что бы то ни стало стать свидетелями необыкновенного зрелища, которое разыгрывается на ее берегах.",
"Итак, каждый год на майские гуляния бывалые воины и отважные ратники со всех сторон света собираются в Фанг, чтобы заглянуть в лицо Судьбе. Мало кто из них вернется домой, ибо велик риск и ужасна подстерегающая опасность, однако нет отбою от желающих вступить за врата Лабиринта Страха - ведь победителю достанется 10 000 золотом и звание почетного гражданина Чанг Май.",
"А получилось так, что некоторое количество лет назад властительный барон города Фанг, известный под именем Сукумвит, решил принести своему городу великую славу. Призвав самых умелых землекопов, каменотесов, ремесленников и мастеровых, он создал в глуби горы на окраине города огромный лабиринт, из которого был лишь один выход. Затем лабиринт был наполнен хитроумными устройствами и смертельными ловушками, населен кровожадными монстрами. Удовлетворенный содеянным, Сукумвит решил испробовать свое изобретение. Было отобрано десять лучших воинов из его стражи, и вот, полностью вооруженные, они вступили в темные пределы. Больше их никто никогда не видел. Слухи о пропавших воинах стремительно облетели окрестности, и вот тогда Сукумвит объявил о Состязании Великих. Посланники и глашатаи разнесли новость - 10 000 золотом и звание почетного гражданина Чанг Май всякому, кто выйдет из страшного лабиринта живым! В первый же год семнадцать отважных воинов ступили на Стезю Смерти, как позже стали называть этот темный путь в народе. Ни один из них не вернулся. Шли годы, и Состязание Великих обогатило Фанг - все больше и больше участников и зрителей стекалось в город еще задолго до начала Состязания. Начиная с апреля, Фанг преображался - возводились шатры, строились трапезные, их заполняли специально выписанные из метрополии менестрели, плясуны, глотатели огня, фокусники и прочие лицедеи; многочисленные искатели приключений, преисполненные надежд, с нетерпением ожидали своей очереди вступить на Стезю, которая, как знать, могла принести им великое богатство и славу. Последняя неделя апреля превращалась в нескончаемый праздник - все пели, пили, танцевали и веселились вплоть до 1 мая, когда весь город отправлялся к вратам лабиринта, чтобы увидеть первого храбреца, отважившегося в этом году бросить вызов Судьбе.",
"Увидев как-то одну из грамот барона Сукумвита, прибитую к дереву, ты решил, что в этом году непременно попытаешь счастье на Стезе Смерти. Мысль эта уже давно не давала тебе покоя - и не столько благодаря слухам о баснословной награде, которая достанется победителю, сколько из-за того факта, что за многие годы никто еще не вышел из Состязания живым. В этом году лабиринт будет пройден! - решил ты, и не долго думая пустился в дорогу. Два дня пути привели тебя на западное побережье - в проклятый богами Порт Блэксэнд. Решив не задерживаться в этом городе воров и убийц, ты купил билет на отходящую шхуну, которая доставила тебя на север - туда, где река Кок вливает в море свои мутные воды. Пересев на плот, ты уже на исходе четвертого дня прибыл в Фанг!",
"Испытание начинается через три дня, и весь город пребывает в лихорадочном ожидании. Ты регистрируешь свое прибытие и получаешь лиловый шарф, который обвязываешь вокруг руки в знак того, что очень скоро ступишь на Стезю Смерти. Все три дня ты наслаждаешься баснословным гостеприимством Фанга -к тебе относятся как к полубогу. За непрекращающимся весельем ты почти забываешь, зачем прибыл в это, как тебе кажется, сказочное место, однако накануне начала Состязания, когда вечерние сумерки начинают опутывать землю, ожидание предстоящего испытания вытесняет у тебя из головы все остальные мысли. Около полуночи тебя провожают в гостевой дом и показывают твою комнату. Вот и роскошное ложе с атласным покровом, на котором тебе предстоит провести последнюю ночь. Однако на сон остается так мало времени!",
"На рассвете звуки труб вырывают тебя из сна, заполненного видениями пылающей преисподней и гигантскими черными пауками. Спустя минуту раздается стук в дверь и глухой голос произносит: «Испытание начинается! Будь готов через десять минут!». Ты выбираешься из кровати, подходишь к окну и распахиваешь занавеси. Улицы уже запружены людьми, в молчании пробирающимися сквозь утренний туман, -зрителями, спешащими ко входу в лабиринт, чтобы заранее занять самые удобные места в предвкушении того зрелища, которое вскоре предстанет перед их праздным взором. Ты отворачиваешься и подходишь к деревянному столу, на котором лежит твой верный меч. Ты выхватываешь его из ножен и в стремительном выпаде со свистом разрубаешь воздух, пытаясь представить, каких чудовищ вскоре встретит этот добрый клинок. Дверь в коридор медленно отворяется. Косоглазый карлик приветствует тебя в низком поклоне. «Следуй за мной», - произносит он, поворачивает налево и быстро направляется к лестнице в конце коридора.",
"Выйдя из гостевого дома, карлик углубляется в узкие извилистые переулки, и ты едва поспеваешь за ним. Вскоре вы выходите на широкую пыльную дорогу, запруженную оживленно переговаривающимися людьми. При виде лилового шарфа у тебя на руке толпа разражается приветственными криками, в тебя летят цветы. Длинные тени, отбрасываемые собравшимися, постепенно укорачиваются по мере того, как жаркое солнце все выше и выше поднимается в ясном утреннем небе. Стоя перед этой шумной и возбужденной толпой, ты чувствуешь себя страшно одиноким в ожидании предстоящего испытания. Настойчивым подергиванием за рукав карлик выводит тебя из оцепенения и нетерпеливо требует, чтобы ты следовал за ним. Впереди ты видишь склоны высоко вздымающейся горы и темный зев туннеля, исчезающего в ее мрачных глубинах. Подойдя ближе, ты замечаешь две каменные колонны, обозначающие вход в туннель. Колонны испещрены искусной резьбой - надписями на древних языках, магическими заклинаниями, изображениями демонов и богов, которые, мнится тебе, стараются предостеречь тех, кто собирается пройти между ними.",
"Ты видишь- самого барона Сукумвита, стоящего напротив входа в ожидании момента, когда он сможет поприветствовать готовящихся к состязанию смельчаков. Всего их пятеро - лиловые шарфы выделяют их среди разношерстной толпы, волнующейся перед темным входом. Двое из них - Варвары из южных земель. Облаченные в меховые штаны, голые по пояс, они стоят практически без движения, ноги на ширине плеч слегка согнуты, руки покоятся на длинных рукоятках обоюдоострых боевых топоров. Кожаную тунику сияющей красотой эльфийской девы с золотыми струящимися волосами и кошачьими зелеными глазами крест-накрест перепоясывают сверкающие кинжалы. Четвертый с головы до ног закован в броню, пышный плюмаж украшает его шлем, рунический крест - тяжелый щит. Пятый же закутан в черные одежды, лишь глаза холодно блестят в прорези закрывающей его лицо маски. Длинные ножи, гаррота и прочие безмолвные орудия смерти свисают с его перевязи. Пятеро претендентов приветствуют твое появление еле заметными кивками, и в последний раз обращаешь ты свой взор к ликующей толпе. Внезапно зрители затихают - то барон Сукумвит выступает вперед, держа в руке шесть бамбуковых палочек. Вытянув одну, ты читаешь слово «Пятый». Состязание начинается.",
"Первым идет Рыцарь. Поприветствовав толпу прощальным взмахом меча, он скрывается в туннеле; полчаса спустя за ним следует эльфийская дева. Затем в темные глубины спускается Варвар, за ним - черный убийца. Пришел твой черед прощаться с дневным светом. Затянув потуже лиловый шарф, ты полной грудью вдыхаешь свежий утренний воздух и делаешь первый шаг в обрамленные каменными колоннами ворота по проложенной мрачной думой барона Сукумвита стезе, чтобы лицом к лицу столкнуться с неведомыми опасностями за полными неизъяснимого ужаса поворотами Лабиринта Страха.",
)