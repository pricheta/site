from enum import StrEnum


class ElementGroup(StrEnum):
    MECHANIC = "Механический"
    PHYSIC = "Физический"
    TOXIN = "Токсины"
    GASP = "Нехватка воздуха"
    CELLULAR = "Клеточный"
    CRIO = "Крио"
    OTHER = "Остальное"
    HIDDEN = "Скрытые"


class Element:
    available_elements: list["Element"] = []

    def __init__(
        self,
        name: str,
        recipe: list[tuple["Element", float]] = [],
        group: ElementGroup = ElementGroup.HIDDEN,
        temperature: str = "",
        catalyst: tuple["Element", int] | tuple = (),
    ) -> None:
        self.name = name
        self.recipe = recipe
        self.group = group
        self.temperature = temperature
        self.catalyst = catalyst
        if self.group != ElementGroup.HIDDEN:
            Element.available_elements.append(self)

    def __str__(self) -> str:
        return self.name


oxygen = Element("Кислород")
hydrogen = Element("Водород")
carbon = Element("Углерод")
sugar = Element("Сахар")
lithium = Element("Литий")
silicon = Element("Кремний")
phosphorus = Element("Фосфор")
iron = Element("Железо")
copper = Element("Медь")
plasma = Element("Плазма")
water = Element("Вода")
sodium = Element("Натрий")
chlorine = Element("Хлор")
potassium = Element("Калий")
nitrogen = Element("Азот")
radium = Element("Радий")
ethanol = Element("Этанол")
welding_fuel = Element("Сварочное топливо")
zombie_blood = Element("Кровь зомби")
iodine = Element("Йод")
omnisin = Element("Омнизин")
blood = Element("Кровь")
aloe = Element("Алоэ")


oil = Element(
    "Масло",
    [
        (hydrogen, 1/3),
        (carbon, 1/3),
        (welding_fuel, 1/3),
    ],
)
ammonia = Element(
    "Аммиак",
    [
        (hydrogen, 3/4),
        (nitrogen, 1/4),
    ],
)
diethylamine = Element(
    "Диэтиламин",
    [
        (ethanol, 1/2),
        (ammonia, 1/2),
    ],
)
inaprovaline = Element(
    "Инапровалин",
    [
        (oxygen, 1 / 3),
        (sugar, 1 / 3),
        (carbon, 1 / 3),
    ],
)
hydroxide = Element(
    "Гидроксид",
    [
        (oxygen, 1 / 2),
        (hydrogen, 1 / 2),
    ],
    temperature="выше 310К",
)
bensole = Element(
    "Бензол",
    [
        (hydrogen, 1),
        (carbon, 1),
    ],
    temperature="выше 310К",
)
celotane = Element(
    "Келотан",
    [
        (silicon, 1 / 2),
        (carbon, 1 / 2),
    ],
)
iron_silicide = Element(
    "Силицид железа",
    [
        (silicon, 1 / 2),
        (iron, 1 / 2),
    ],
    temperature="выше 310К",
)
salt = Element(
    "Столовая соль",
    [
        (sodium, 1 / 2),
        (chlorine, 1 / 2),
    ],
    temperature="выше 370К",
)
sodium_carbonate = Element(
    "Карбонат натрия",
    [
        (oxygen, 1 / 4),
        (ammonia, 1 / 4),
        (carbon, 1 / 4),
        (salt, 1 / 4),
    ],
)
sodium_hydroxide = Element(
    "Гидроксид натрия",
    [
        (sodium, 1 / 2),
        (hydroxide, 1 / 2),
    ],
)
dexolyne = Element(
    "Дексалин",
    [
        (oxygen, 2 / 3),
    ],
    catalyst=(plasma, 1),
    group=ElementGroup.GASP,
)
unstable_mutagen = Element(
    "Нестабильный мутаген",
    [
        (chlorine, 1 / 3),
        (phosphorus, 1 / 3),
        (radium, 1 / 3),
    ],
    group=ElementGroup.OTHER,
)
bicaridine = Element(
    "Бикаридин",
    [
        (carbon, 1 / 2),
        (inaprovaline, 1 / 2),
    ],
    group=ElementGroup.MECHANIC,
)
bruisine = Element(
    "Бруизин",
    [
        (lithium, 0.9 / 2),
        (bicaridine, 1 / 2),
        (sugar, 1 / 2),
    ],
    group=ElementGroup.MECHANIC,
)
puncturase = Element(
    "Пунктураз",
    [
        (hydroxide, 1 / 2),
        (bicaridine, 1 / 2),
    ],
    group=ElementGroup.MECHANIC,
    temperature="выше 325К",
)
lacerinole = Element(
    "Лацеринол",
    [
        (bensole, 1 / 2),
        (bicaridine, 1 / 2),
    ],
    group=ElementGroup.MECHANIC,
    temperature="выше 335К",
)
dermaline = Element(
    "Дермалин",
    [
        (celotane, 1 / 3),
        (oxygen, 1 / 3),
        (phosphorus, 1 / 3),
    ],
    group=ElementGroup.PHYSIC,
)
leporasine = Element(
    "Лепоразин",
    [
        (iron_silicide, 1 / 2),
        (copper, 1 / 2),
    ],
    group=ElementGroup.PHYSIC,
    catalyst=(plasma, 1),
)
pirasine = Element(
    "Пиразин",
    [
        (leporasine, 1 / 3),
        (dermaline, 1 / 3),
        (carbon, 1 / 3),
    ],
    group=ElementGroup.PHYSIC,
    temperature="выше 540К",
)
insusine = Element(
    "Инсузин",
    [
        (leporasine, 1 / 3),
        (silicon, 1 / 3),
        (celotane, 1 / 3),
    ],
    group=ElementGroup.PHYSIC,
    temperature="выше 433К",
)
siginate = Element(
    "Сигинат",
    [
        (water, 1 / 4),
        (sugar, 1 / 4),
        (sodium_carbonate, 1 / 4),
        (celotane, 1 / 4),
        (sodium_hydroxide, 1 / 4),
    ],
    group=ElementGroup.PHYSIC,
    temperature="выше 370К",
)
diloven = Element(
    "Диловен",
    [
        (potassium, 1 / 3),
        (silicon, 1 / 3),
        (nitrogen, 1 / 3),
    ],
    group=ElementGroup.TOXIN,
)
diphenhydramine = Element(
    "Дифенгидрамин",
    [
        (oil, 1 / 3),
        (ethanol, 1 / 3),
        (carbon, 1 / 3),
        (diethylamine, 1 / 3),
        (salt, 1 / 3),
    ],
    group=ElementGroup.TOXIN,
    temperature="выше 378К",
)
ethylredoxazine = Element(
    "Этилредоксразин",
    [
        (oxygen, 1 / 3),
        (diloven, 1 / 3),
        (carbon, 1 / 3),
    ],
    group=ElementGroup.TOXIN,
)
hyronalyne = Element(
    "Хироналин",
    [
        (diloven, 1 / 2),
        (radium, 1 / 2),
    ],
)
aritrazine = Element(
    "Аритразин",
    [
        (hyronalyne, 1 / 2),
        (hydrogen, 1 / 2),
    ],
    group=ElementGroup.TOXIN,
)
dexolyne_plus = Element(
    "Дексалин Плюс",
    [
        (iron, 1 / 3),
        (dexolyne, 1 / 3),
        (carbon, 1 / 3),
    ],
    group=ElementGroup.GASP,
)
saline_solution = Element(
    "Физраствор",
    [
        (water, 4 / 5),
        (salt, 1 / 5),
    ],
    group=ElementGroup.OTHER,
)
falanhymyne = Element(
    "Фалангимин",
    [
        (unstable_mutagen, 1 / 3),
        (hyronalyne, 1 / 3),
        (ethanol, 1 / 3),
    ],
    group=ElementGroup.CELLULAR,
)
cryoxadon = Element(
    "Криоксадон",
    [
        (water, 1 / 3),
        (dexolyne, 1 / 3),
        (oxygen, 1 / 3),
    ],
    group=ElementGroup.CRIO,
)
doxarubixadone = Element(
    "Доксарубиксадон",
    [
        (cryoxadon, 1 / 2),
        (unstable_mutagen, 1 / 2),
    ],
    group=ElementGroup.CRIO,
)
necrosol = Element(
    "Некрозол",
    [
        (omnisin, 1 / 2),
        (cryoxadon, 2 / 2),
        (blood, 3 / 2),
    ],
    group=ElementGroup.CRIO,
    temperature="выше 370К",
)
aloxadon = Element(
    "Алоксадон",
    [
        (siginate, 2 / 4),
        (cryoxadon, 1 / 4),
        (aloe, 2 / 4),
    ],
    group=ElementGroup.CRIO,
)
space_cleaner = Element(
    "Космический очиститель",
    [
        (water, 1 / 2),
        (ammonia, 1 / 2),
    ],
    group=ElementGroup.OTHER,
)
ambuzol = Element(
    "Амбузол",
    [
        (diloven, 1 / 4),
        (ammonia, 1 / 4),
        (zombie_blood, 2 / 4),
    ],
    group=ElementGroup.OTHER,
)
ephedrine = Element(
    "Эфедрин",
    [
        (oil, 1 / 4),
        (sugar, 1 / 4),
        (diethylamine, 1 / 4),
        (hydrogen, 1 / 4),
    ],
)
deoxyephedrine = Element(
    "Дезоксиэфедрин",
    [
        (phosphorus, 1 / 4),
        (iodine, 1 / 4),
        (ephedrine, 1 / 4),
        (carbon, 1 / 4),
    ],
    temperature="выше 370К",
)
dilometh = Element(
    "Диломет",
    [
        (deoxyephedrine, 1 / 2),
        (diloven, 1 / 2),
    ],
    group=ElementGroup.OTHER,
)
