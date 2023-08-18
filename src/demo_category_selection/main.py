"""Main python file."""

from bmt import Toolkit
from oaklib import get_adapter


def demo():
    """
    navigate pato and biolink together

    """

    tk = Toolkit()
    adapter = get_adapter("sqlite:obo:upheno")
    test_entities = ["PATO:0000001", "PATO:0000002", "UPHENO:0075852", "UPHENO:0001002"]
    for entity in test_entities:
        entity_parents = adapter.hierarchical_parents(entity, isa_only=True)
        for aroot in adapter.roots():
            print(entity, aroot)
        print("parents of", entity, entity_parents)
        if entity_parents:
            for parent in entity_parents:
                bl_category = get_biolink_category(parent, tk)
                if bl_category:
                    return bl_category


def get_biolink_category(entity, tk):
    """
    get biolink category for entity

    """

    bl_element = tk.get_element_by_mapping(identifier=str(entity))
    if tk.get_element_by_mapping(identifier=str(entity)) is not None:
        print("found category for entity", entity, tk.get_element_by_mapping(identifier=str(entity)))
        return bl_element


if __name__ == "__main__":
    demo()
