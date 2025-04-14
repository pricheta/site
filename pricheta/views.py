from django.shortcuts import render

from pricheta.recipe_maker.craft_step import get_element_recipe
from pricheta.recipe_maker.elements import ElementGroup, Element


AVAILABLE_ELEMENT_GROUPS = [
    ElementGroup.MECHANIC,
    ElementGroup.PHYSIC,
    ElementGroup.TOXIN,
    ElementGroup.GASP,
    ElementGroup.CELLULAR,
    ElementGroup.BOTANIC,
    ElementGroup.OTHER,
]


AVAILABLE_ELEMENTS_DICT: dict[str, Element] = {
    element.name: element for element in Element.available_elements
}


GROUPED_ELEMENTS: dict[ElementGroup, list[Element]] = {group: [] for group in ElementGroup if group in AVAILABLE_ELEMENT_GROUPS}
for element in  Element.available_elements:
    if element.group not in AVAILABLE_ELEMENT_GROUPS:
        continue
    if element.group not in GROUPED_ELEMENTS:
        GROUPED_ELEMENTS[element.group] = []
    GROUPED_ELEMENTS[element.group].append(element)


def index(request):
    element_name:str = request.GET.get('element_name', '')
    element_amount: int = int(request.GET.get('element_amount', 180))

    element = AVAILABLE_ELEMENTS_DICT.get(element_name)

    if element and element_amount:
        raw_recipe = get_element_recipe(element, element_amount, [])
        recipe = []
        for step in raw_recipe:
            spaces = " " * 4 * len(step.step_extended_number)
            recipe.append(f"{spaces}{step}")
    else:
        recipe = None


    return render(
        request,
        "pricheta/content.html",
        {
            "grouped_elements": GROUPED_ELEMENTS,
            "recipe": recipe,
            "element_name": element_name,
            "element_amount": element_amount,
        },
    )

