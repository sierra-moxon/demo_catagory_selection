"""Main python file."""

from bmt import Toolkit
from oaklib import get_adapter


def demo():
    """
    navigate phenio and biolink together

    """

    tk = Toolkit()
    adapter = get_adapter("sqlite:obo:pato")

    for entity in adapter.entities():
        entity_parents = adapter.hierarchical_parents(entity, isa_only=True)
        if entity_parents:
            for parent in entity_parents:
                bl_category = get_biolink_category(parent, tk)
                if bl_category:


def get_biolink_category(entity, tk):
    """
    get biolink category for entity

    """

    if tk.get_element_by_mapping(identifier=str(entity)) is not None:
        print("found category for entity", entity, tk.get_element_by_mapping(identifier=str(entity)))
        return tk.get_element_by_mapping(identifier=str(entity))


if __name__ == "__main__":
    demo()
