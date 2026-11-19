# -*- coding: utf-8 -*-
"""Regroupe et valide les 500 idées de business à lancer en Afrique pour bien finir l'année."""

from ideas_part1 import SECTORS_PART_1
from ideas_part2 import SECTORS_PART_2

ALL_SECTORS = SECTORS_PART_1 + SECTORS_PART_2


def get_numbered_sectors():
    """Retourne les 20 secteurs avec numérotation continue 001..500."""
    idx = 1
    result = []
    for sector in ALL_SECTORS:
        items = []
        for title, desc, budget in sector["ideas"]:
            items.append({
                "id": idx,
                "code": f"{idx:03d}",
                "title": title.strip(),
                "desc": desc.strip(),
                "budget": budget.strip(),
            })
            idx += 1
        result.append({
            "num": sector["num"],
            "title": sector["title"],
            "intro": sector["intro"],
            "start_id": items[0]["id"],
            "end_id": items[-1]["id"],
            "ideas": items,
        })
    return result


if __name__ == "__main__":
    sectors = get_numbered_sectors()
    all_ideas = [item for s in sectors for item in s["ideas"]]
    print(f"Total secteurs : {len(sectors)}")
    print(f"Total idées    : {len(all_ideas)}")
    assert len(sectors) == 20, f"Attendu 20 secteurs, obtenu {len(sectors)}"
    assert len(all_ideas) == 500, f"Attendu 500 idées, obtenu {len(all_ideas)}"

    titles_lower = [i["title"].lower() for i in all_ideas]
    dups = [t for t in set(titles_lower) if titles_lower.count(t) > 1]
    assert not dups, f"Doublons détectés : {dups}"

    from collections import Counter
    budgets = Counter(i["budget"] for i in all_ideas)
    print("Répartition budgets :", dict(budgets))
    assert set(budgets.keys()) == {"Petit", "Moyen", "Structuré"}
    print("VALIDATION OK : 500 idées uniques et conformes !")
