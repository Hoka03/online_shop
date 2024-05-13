from django.core.management import BaseCommand
from apps.products.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        products = [
            Product(
                sub_category_id=1,
                title_uz=f'Samsung Galaxy Z Flip4',
                slug=f'samsung-galaxy-z-flip4',
                title_ru=f'Телефон',
                short_desc_uz=f'See foldable phone.A hinged cellphone '
                              f'that is more compact when closed. The cover '
                              f'"flips open" to reveal the screen, keypad, '
                              f'speaker and microphone.',
                short_desc_ru=f'См. складной телефон. Мобильный телефон '
                              f'на шарнирах, который в закрытом состоянии более '
                              f'компактен. Крышка «открывается», открывая экран, '
                              f'клавиатуру, динамик и микрофон.',
                long_desc_uz=f'A flip phone, also known as a clamshell phone, '
                             f'is a mobile phone that is designed with a hinge that '
                             f'allows the phone to be folded in half. This design protects '
                             f'the screen and keyboard when the phone is not in use and '
                             f'makes the phone more compact and easier to carry.',
                long_desc_ru=f'Телефон-раскладушка, также известный как телефон-раскладушка, '
                             f'представляет собой мобильный телефон с шарниром, позволяющим '
                             f'складывать его пополам. Такая конструкция защищает экран и клавиатуру, '
                             f'когда телефон не используется, а также делает его более компактным '
                             f'и удобным для переноски.',
            ),
            Product(
                sub_category_id=2,
                title_uz=f'Victus',
                slug=f'victus',
                title_ru=f'виктус',
                short_desc_uz=f'o, should you buy the HP Victus gaming laptop? I would say, yes. Priced at Rs 86,999',
                short_desc_ru=f'о, стоит ли покупать игровой ноутбук HP Victus? Я бы сказал, да. Цена 86 999 рупий.',
                long_desc_uz='The HP Victus 15 (2022) is a 15.6-inch budget gaming laptop. '
                             'Its available with Intel 12th Gen. Core i5 or i7 CPUs and multiple '
                             'NVIDIA discrete GPUs, from a GeForce GTX 1650 to an RTX 3050 Ti. There '
                             'are also multiple 1080p display options with a refresh rate of 60Hz or 144Hz.',
                long_desc_ru=f'HP Victus 15 (2022) — бюджетный игровой ноутбук с экраном 15,6 дюйма. Он доступен с '
                             f'процессорами Intel Core i5 или i7 12-го поколения и несколькими дискретными графическими'
                             f'процессорами NVIDIA, от GeForce GTX 1650 до RTX 3050 Ti. Существует также несколько '
                             f'вариантов отображения 1080p с частотой обновления 60 Гц или 144 Гц.',
            ),
            Product(
                sub_category_id=3,
                title_uz=f'TV LLG',
                slug=f'tv-llg',
                title_ru=f'телевизор LLG',
                short_desc_uz=f'LG was one of the first brands to release TVs with OLED panels',
                short_desc_ru=f'LG была одним из первых брендов, выпустивших телевизоры с OLED-панелями.',
                long_desc_uz='Goldstar first went public in 1970; by 1976, it was producing one million televisions '
                             'annually. In 1982, Goldstar opened its first overseas factory, which was based in '
                             'Huntsville, Alabama.',
                long_desc_ru=f'Goldstar впервые стала публичной в 1970 году; к 1976 году она производила один миллион '
                             f'телевизоров ежегодно. В 1982 году Goldstar открыла свой первый зарубежный завод в '
                             f'Хантсвилле, штат Алабама.',
            ),

            Product(
                sub_category_id=4,
                title_uz='Fitted Hoodie',
                slug='fitted-hoodie',
                title_ru='Приталенная толстовка с капюшоном',
                short_desc_uz=f' hoodie is a type of casual jacket with a hood.',
                short_desc_ru=f'Толстовка – это разновидность повседневной куртки с капюшоном.',
                long_desc_uz='A hoodie is a type of casual jacket with a hood. She wore jeans and a hoodie. '
                             'A hoodie is a young person wearing a hoodie, thought by some people to be badly '
                             'behaved or possibly criminal',
                long_desc_ru=f'Худи – это разновидность повседневной куртки с капюшоном. Она носила джинсы и толстовку.'
                             f' Толстовка — это молодой человек в толстовке, которого некоторые считают человеком с '
                             f'плохим поведением или, возможно, преступником.',
            ),
            Product(
                sub_category_id=5,
                title_uz='Walking shoes',
                slug='walking-shoes',
                title_ru='обувь для ходьбы',
                short_desc_uz=f'light shoe that has a top made of cloth and a bottom made of rubber, worn esp, '
                              f'for sports. ',
                short_desc_ru=f'легкая обувь с тканевым верхом и резиновой подошвой, особенно носившаяся. для спорта.',
                long_desc_uz='A running sneaker can be suitable for walking. This type of comfortable shoe tends to be '
                             'slightly lighter and more flexible than walking shoes.',
                long_desc_ru=f'Беговые кроссовки могут подойти для прогулок. Этот тип удобной обуви, как правило,'
                             f' немного легче и гибче, чем обувь для ходьбы.',
            ),
            Product(
                sub_category_id=6,
                title_uz='Switter West',
                slug='switter-west',
                title_ru='Cвитер запад',
                short_desc_uz=f'The sweater vest, also known as the sleeveless sweater, offers a quirky twist to the '
                              f'traditional sweater. ',
                short_desc_ru=f'Жилет-свитер, также известный как свитер без рукавов, представляет собой необычную'
                              f' альтернативу традиционному свитеру.',
                long_desc_uz='As the crisp fall air transitions into the chill of winter, one fashion item becomes a '
                             'non-negotiable in your wardrobe – the ever-dependable, ever-versatile sweater.',
                long_desc_ru=f'Когда свежий осенний воздух сменяется зимней прохладой, одна модная вещь становится '
                             f'незаменимой в вашем гардеробе — надежный и универсальный свитер.',
            ),

            Product(
                sub_category_id=7,
                title_uz='N.K. Jemisin on the Timeless Power of Fantasy',
                slug='jemisin-on-the-timeless-power-of-fantasy',
                title_ru='Н.К. Джемисин о вневременной силе фантазии',
                short_desc_uz=f'While Lord of the Rings is one of the most important books of the fantasy genre, it '
                              f'all began with The Hobbit',
                short_desc_ru=f'Хотя «Властелин колец» — одна из самых важных книг жанра фэнтези, все началось с '
                              f'«Хоббита».',
                long_desc_uz=' a book that proved to children that magic really does exist and sometimes the most '
                             'unassuming of characters can carry it in their pocket. This enchanting tale will continue'
                             'enchanting for centuries to come',
                long_desc_ru=f'книга, которая доказала детям, что волшебство действительно существует и иногда даже '
                             f'самые скромные персонажи могут носить его в кармане. Эта очаровательная сказка будет '
                             f'очаровывать на протяжении веков.',
            ),
            Product(
                sub_category_id=8,
                title_uz='SPQR: A History of Ancient Rome',
                slug='a-history-of-ancient-rome',
                title_ru='SPQR: История Древнего Рима',
                short_desc_uz=f'In SPQR, an instant classic, Mary Beard narrates the history of Rome "with passion '
                              f'and without technical jargon"',
                short_desc_ru=f'В SPQR, ставшей классикой, Мэри Бирд рассказывает историю Рима «страстно и '
                              f'без технического жаргона»..',
                long_desc_uz=' Hailed by critics as animating "the grand sweep and the intimate details that bring'
                             ' the distant past vividly to life" (Economist) in a way that makes "your hair stand '
                             'on end" (Christian Science Monitor) and spanning nearly a thousand years of history, ',
                long_desc_ru=f'Критики хвалят его за то, что он оживляет «грандиозный размах и интимные детали,'
                             f' которые ярко оживляют далекое прошлое» (Economist) таким образом, что «у вас волосы'
                             f' встают дыбом» (Christian Science Monitor), и охватывает почти тысячу лет истории.',
            ),
            Product(
                sub_category_id=9,
                title_uz='A Village in the Third Reich',
                slug='a-village-in-the-third-reich',
                title_ru='Деревня в Третьем Рейхе',
                short_desc_uz=f'A Village in the Third Reich. Added to basket',
                short_desc_ru=f'Деревня в Третьем Рейхе. Добавлено в корзину',
                long_desc_uz='It is only from studying the past that we can learn about the present and so great '
                             'history books are essential reading for anyone with an interest in the modern world.',
                long_desc_ru=f'Только изучая прошлое, мы можем узнать о настоящем, и поэтому великие книги '
                             f'по истории необходимы для чтения всем, кто интересуется современным миром.'
            ),
        ]
        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS(f'{Product.objects.count()} main_cats created'))
