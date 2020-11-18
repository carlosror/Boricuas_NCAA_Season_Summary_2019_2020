#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
margins = (0, 0, 0, 0)

docs_list = ["Cover.sla", "By_the_numbers.sla", "Map_of_arcs.sla", "NAIA_mugshots.sla", "NAIA_action_shots.sla", "NCAA_DI_mugshots.sla", "NCAA_DI_action_shots.sla", 
             "NCAA_DII_mugshots.sla", "NCAA_DII_action_shots.sla", "NCAA_DIII_mugshots.sla", "NCAA_DIII_action_shots.sla",
             "Top50.sla", "Conf_leaders.sla", "National_tournaments.sla", "All_Conference.sla"]
doc_lengths_dict = {"Cover.sla": 1, "By_the_numbers.sla": 1, "Map_of_arcs.sla": 1, "NAIA_mugshots.sla": 4, "NAIA_action_shots.sla": 3, "NCAA_DI_mugshots.sla": 5, "NCAA_DI_action_shots.sla": 6,
                    "NCAA_DII_mugshots.sla": 5, "NCAA_DII_action_shots.sla": 6, "NCAA_DIII_mugshots.sla": 3, "NCAA_DIII_action_shots.sla": 3,
                    "Top50.sla": 14, "Conf_leaders.sla": 18, "National_tournaments.sla": 10, "All_Conference.sla": 10}

if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):
  for doc in docs_list:
    pages_list = [page for page in range(1, doc_lengths_dict[doc] + 1)]
    pages_tuple = tuple(pages_list) # input to importPage() must be a tuple
    importPage(doc, pages_tuple)
  # importPage("Top50.sla", tuple())
  # importPage("Conf_leaders.sla", tuple([page for page in range(1, doc_lengths_dict["Conf_leaders.sla"] + 1)]))
  # importPage("National_tournaments.sla", tuple([page for page in range(1, doc_lengths_dict["National_tournaments.sla"] + 1)]))
  # importPage("All_Conference.sla", tuple([page for page in range(1, doc_lengths_dict["All_Conference.sla"] + 1)]))