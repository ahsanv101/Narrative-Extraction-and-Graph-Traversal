# Narrative Extraction and Graph Traversal

## Abstract
Linked Open Data enables an expressive formal representation of data as stories that can be extracted and re-assembled in the form of a narrative. Having these narratives interconnected would surely enrich the data itself as well as the user consumption of the information. Narratives of cultural heritage data have the potential to unfold incredible stories of humans and societies throughout time.This project will use the vast archived collections of the Netherlands Institute for Sound and Vision (NISV) as a case study to computationally produce data narratives in the form of lists/chains of entities in a meaningful way.

## Introduction
Since the wave of digitization and archiving of cultural heritage, there has been a plethora of data available on the internet which seems to be increasing incrementally (Eberendu, 2016). These datasets follow particular standards, depending on the object that they are describing, and are stored in the form of knowledge graphs. There is vast potential in utilizing these knowledge graphs in creative manners. In particular, exploring unknown datasets to find meaningful stories (e.g. lists of entities that are meaningfully related, data patterns that are not immediate to a consumer) would significantly improve the understanding of our cultural heritage by lay users that cannot manipulate structured data and therefore need some mediation in the consumption. 

This project’s vision is to build such a system that can take multiple cultural heritage datasets and automatically build stories and connections within them. By analyzing these different datasets and connecting them through meaningful patterns, it will give us stories through which we will be able to enrich our understanding of cultural heritage. In particular, results of the project will be leveraged in a related project i.e. Polifonia. The project will focus on the music collection of NISV as a case study which contains more than half a million recordings.

## The software
All the code of the software is available on the jupyter notebook. The code first takes in a dataset as input and trains on that data to produce scores which it also saves locally. Once the training is done then the narratives can be traversed, extracted and visualized.

Note: The MOZ dataset used for this is not publicly available therefore only the output visualizations (text and graphs) have been provided.
