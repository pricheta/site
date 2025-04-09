import math

from pricheta.recipe_maker.elements import Element


class CraftStep:
    def __init__(
        self,
        crafted_element: Element,
        amount_to_craft: int,
        step_extended_number: list[int],
    ) -> None:
        self.crafted_element = crafted_element
        self.amount_to_craft = amount_to_craft
        self.step_extended_number = step_extended_number

    def __str__(self):
        if self.step_extended_number:
            step_extended_number_list = [str(number) for number in self.step_extended_number]
            step_extended_number = '.'.join(step_extended_number_list)
            step_extended_number += '. '
        else:
            step_extended_number = ''

        if not self.crafted_element.recipe:
            return f'{step_extended_number}Добавляем {self.amount_to_craft} ед. элемента \"{self.crafted_element}\"'

        temperature_str = (
            f" при температуре {self.crafted_element.temperature}"
            if self.crafted_element.temperature
            else ""
        )

        if self.crafted_element.catalyst:
            catalyst_element = self.crafted_element.catalyst[0]
            catalyst_amount = self.crafted_element.catalyst[1]
            catalyst_str = f", катализатор реакции - {catalyst_amount} ед. элемента \"{catalyst_element}\""
        else:
            catalyst_str = ""

        return f"{step_extended_number}Получаем {self.amount_to_craft} ед. элемента \"{self.crafted_element}\"{temperature_str}{catalyst_str}"



def get_element_recipe(
    crafted_element: Element,
    amount_to_craft: int,
    step_extended_number: list[int],
) -> list[CraftStep]:

    recipe: list[CraftStep] = [
        CraftStep(
            crafted_element,
            amount_to_craft,
            step_extended_number,
        )
    ]

    step = 0
    for element, craft_element_ratio in crafted_element.recipe:
        step += 1
        ingredient_amount = craft_element_ratio * amount_to_craft
        ingredient_amount = math.ceil(ingredient_amount)
        recipe += get_element_recipe(element, ingredient_amount, step_extended_number + [step])

    return recipe
