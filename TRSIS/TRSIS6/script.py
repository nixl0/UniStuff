# coding: utf8

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.add_font('OpenSans', fname='OpenSans-Regular.ttf', uni=True)
        self.set_font('OpenSans', size=24)
        self.set_text_color(255)
        self.set_fill_color(180, 60, 50)
        self.cell(0, 20, self.title, fill=True, align='C')
        self.ln(30)

    def footer(self):
        self.set_y(-15)
        self.set_font('OpenSans', size=10)
        self.cell(0, 10, f'Страница {self.page_no()}/{{nb}}', align='C')

    def par(self, txt):
        self.add_font('NotoSerif', fname='NotoSerif-Regular.ttf', uni=True)
        self.set_font('NotoSerif', size=12)
        self.set_left_margin(20)
        self.multi_cell(w=0, h=7, txt=txt, new_x='LMARGIN', new_y='NEXT')
    
    def write(self, txt):
        self.add_font('NotoSerif', fname='NotoSerif-Regular.ttf', uni=True)
        self.set_font('NotoSerif', size=12)
        self.set_left_margin(20)
        self.write(txt=txt)

    def par_algnr(self, txt):
        self.add_font('NotoSerif', fname='NotoSerif-Regular.ttf', uni=True)
        self.set_font('NotoSerif', size=12)
        self.set_left_margin(20)
        self.multi_cell(w=0, h=5, align='R', txt=txt, new_x='LMARGIN', new_y='NEXT')

    def par_algnc(self, txt):
        self.add_font('NotoSerif', fname='NotoSerif-Regular.ttf', uni=True)
        self.set_font('NotoSerif', size=12)
        self.set_left_margin(20)
        self.multi_cell(w=0, h=10, align='C', txt=txt, new_x='LMARGIN', new_y='NEXT')

    def par_rotate(self, txt):
        self.add_font('NotoSerif', fname='NotoSerif-Regular.ttf', uni=True)
        self.set_font('NotoSerif', size=12)
        self.set_left_margin(20)
        with self.rotation(-90, self.get_x() + 100, self.get_y()):
            self.multi_cell(w=0, h=10, txt=txt)

    def add_image(self, image):
        self.multi_cell(w=0, h=10, align='C', new_x='LMARGIN', new_y='NEXT')
        self.image(image, w=pdf.epw/2)
        self.ln(10)

pdf = PDF()
pdf.set_title('Red panda')
pdf.oversized_images = "DOWNSCALE"

pdf.add_page()
pdf.par('Симпатичный зверь размером с крупного домашнего кота, малая панда полосатым хвостом похожа на енота. За яркую шерсть её называют «огненной лисой», а за повадки — «кошачьим медведем». Последние генетические исследования позволили выделить малую панду в отдельное семейство — пандовые.')
pdf.par('Письменные упоминания об этом звере в Китае относятся к XIII веку, однако открыл его для науки в 1821 году английский генерал и натуралист Томас Хардвик, собиравший материал на территории английских колоний. Он предложил назвать это животное «уа» — одним из его китайских названий, основанном на имитации издаваемых зверьком звуков. Кроме того, сообщил генерал, китайцы называют его «пунья», откуда и произошло современное «панда». Хардвику не удалось стать «крёстным отцом» этого животного — он задержался с возвращением в Англию со своими материалами. Латинское название Ailurus fulgens, что можно перевести как «блистающая кошка», — новому животному успел дать французский натуралист Фредерик Кювье.')
pdf.add_image('https://moscowzoo.ru/upload/iblock/018/018dfce9d60a84f0fa68800df7115f78.jpg')
pdf.par('Все народы, живущие на территориях, где обитает малая панда, по-видимому, активно преследуют её из-за красивого меха, который используется для изготовления шляп и одежды местным населением. В провинции Юньнань шляпы из меха малой панды для новобрачных расцениваются как талисман для счастливой семейной жизни. Малая панда — талисман Международного фестиваля чая в Дарджилинге.')
pdf.par('Туловище малой панды удлинённое, длина его 51–64 см, высота в плечах 25 см, шерсть густая, мягкая, гладкая и очень длинная. От густого и мягкого меха тело кажется толще, чем оно есть на самом деле. Пушистый хвост также длинный, причем его длина у разных зверьков значительно варьирует: от 28 до 48 см. Уши маленькие, округлые, глаза тоже невелики, но из-за большого лба голова приобретает пропорции, свойственные детёнышам и придающие зверю необычайную миловидность. Лапы короткие, крепкие, пальцы снабжены сильно загнутыми полувтяжными когтями, которые помогают панде легко забираться на деревья и спускаться с них. На запястье у панды есть «добавочный палец» — увеличенная часть одной из костей передней лапы. Он противопоставлен другим пальцам, что позволяет панде держать в лапах ветви бамбука.')
pdf.par('Окраска шерсти малой панды рыжая или ореховая, снизу тёмная, рыжевато-коричневая или чёрная. У волос на спине жёлтые кончики. Лапы глянцевито-чёрные, хвост рыжий, с более светлыми узкими кольцами, голова светлая, причём края ушей и мордочка почти белые, а около глаз рисунок в виде маски, как у енотов, причём этот рисунок уникален для каждой отдельной особи. Самцы и самки одинакового размера, животные могут весить от 3,7 до 6, 2 кг.')
pdf.add_image('https://redpandanetwork.org/files/_cache/98639e9677778d08988291f0ba4c1824.jpeg')
pdf.par_algnr('Большую часть жизни панды проводят в одиночестве. Участки самок около 2,5 кв. км, самцов — вдвое больше. Свои участки зверьки метят, используя мочу и секрет анальных желёз и желёз, расположенных на подошвах лап. Этой же цели служат и кучки помёта, которые образуют настоящие «уборные», расположенные обычно по границе территории. Такие метки несут информацию о поле, возрасте и физиологическом состоянии животного.')
pdf.par_algnc('Самец малой панды яростно защищает свою территорию. В случае появления соперника он начинает громко шипеть. Перед атакой противники поднимают головы и выразительно «кивают» ими. Если ни один из них не испугался предупреждения, то происходит яростная схватка. Вне сезона размножения взрослые панды редко общаются друг с другом.')
pdf.add_image('https://preview.redd.it/v8a8i3onj5u21.jpg?auto=webp&s=3697f5f4a28a412c24fdd646502f0fa11f5b72ac')
pdf.par('Всё.')

pdf.par_rotate('этот текст должен отображаться повёрнутым этот текст должен отображаться повёрнутым этот текст должен отображаться повёрнутым этот текст должен отображаться повёрнутым этот текст должен отображаться повёрнутым этот текст должен отображаться повёрнутым этот текст должен отображаться повёрнутым этот текст должен отображаться повёрнутым')

pdf.output('sample1.pdf')

