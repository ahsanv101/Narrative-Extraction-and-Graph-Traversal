# from SPARQLWrapper import SPARQLWrapper, JSON
# import ssl
#
# # if you have mac and you run this locally, uncomment
# # ssl._create_default_https_context = ssl._create_unverified_context
#
# # get the endpoint API
# wikidata_endpoint = "https://cat.apis.beeldengeluid.nl/sparql"
#
# # prepare the query : 10 random triples
# my_SPARQL_query = """
# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX sdo: <https://schema.org/>
# PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
#
# SELECT  ?programUri ?programName ?programLic ?programPub ?programMed ?programDate ?programCon ?programURL ?programLoc ?programRec ?programCre ?programArt
# ?programLocLab
# WHERE
# {
#  # Filter for programmes belonging to the series "Muziekopnamen Zendgemachtigden (MOZ)", using its ID
#  ?programUri sdo:partOfSeason/sdo:partOfSeries <http://data.beeldengeluid.nl/id/series/2101608030025711131> ;
#       sdo:name ?programName ;
#       sdo:license ?programLic;
#       sdo:publisher ?programPub;
#       sdo:associatedMedia ?programMed;
#       sdo:datePublished ?programDate;
#       sdo:conditionsOfAccess ?programCon;
#       sdo:url ?programURL;
#       sdo:locationCreated ?programLoc.
#
#     optional
#   {
#     ?programUri sdo:creator ?programCre;
#                 sdo:byArtist ?programArt;
#                 sdo:recordedAt ?programRec.
#
#     ?programLoc skos:prefLabel ?programLocLab.
#
#
#   }
#
#
# }
# limit 10
# """
#
# #  set the endpoint
# sparql_wd = SPARQLWrapper(wikidata_endpoint)
# # set the query
# sparql_wd.setQuery(my_SPARQL_query)
# #  set the returned format
# sparql_wd.setReturnFormat(JSON)
# # get the results
# results = sparql_wd.query().convert()
#
# # manipulate the result
# for result in results["results"]["bindings"]:
#     if 'programCre' not in result and 'programArt' not in result and 'programRec' not in result:
#         #         print(result)
#         print('URI:', '\n', result["programUri"]["value"], '\n', 'Program Name:', '\n', result["programName"]["value"],
#               '\n', 'Program License:', '\n', result["programLic"]["value"], '\n', 'Program Publisher:', '\n',
#               result["programPub"]["value"], '\n', 'Associated Media:', '\n', result["programMed"]["value"], '\n',
#               'Program Date:', '\n', result["programDate"]["value"], '\n', 'Program Conditions of Access:', '\n',
#               result["programCon"]["value"], '\n', 'Program URL:', '\n', result["programURL"]["value"], '\n',
#               'Program Location:', '\n', result["programLoc"]["value"])
#         print('\n')
#
#     if 'programCre' in result and 'programArt' not in result and 'programRec' not in result:
#         print('URI:', '\n', result["programUri"]["value"], '\n', 'Program Name:', '\n', result["programName"]["value"],
#               '\n', 'Program License:', '\n', result["programLic"]["value"], '\n', 'Program Publisher:', '\n',
#               result["programPub"]["value"], '\n', 'Associated Media:', '\n', result["programMed"]["value"], '\n',
#               'Program Date:', '\n', result["programDate"]["value"], '\n', 'Program Conditions of Access:', '\n',
#               result["programCon"]["value"], '\n', 'Program URL:', '\n', result["programURL"]["value"], '\n',
#               'Program Location:', '\n', result["programLoc"]["value"], 'Program Creator:', '\n',
#               result["programCre"]["value"])
#         print('\n')
#
#     if 'programCre' in result and 'programArt' in result and 'programRec' not in result:
#         print('URI:', '\n', result["programUri"]["value"], '\n', 'Program Name:', '\n', result["programName"]["value"],
#               '\n', 'Program License:', '\n', result["programLic"]["value"], '\n', 'Program Publisher:', '\n',
#               result["programPub"]["value"], '\n', 'Associated Media:', '\n', result["programMed"]["value"], '\n',
#               'Program Date:', '\n', result["programDate"]["value"], '\n', 'Program Conditions of Access:', '\n',
#               result["programCon"]["value"], '\n', 'Program URL:', '\n', result["programURL"]["value"], '\n',
#               'Program Location:', '\n', result["programLoc"]["value"], 'Program Creator:', '\n',
#               result["programCre"]["value"], 'Program Artist:', '\n', result["programArt"]["value"])
#         print('\n')
#
#     if 'programCre' in result and 'programArt' not in result and 'programRec' in result:
#         print('URI:', '\n', result["programUri"]["value"], '\n', 'Program Name:', '\n', result["programName"]["value"],
#               '\n', 'Program License:', '\n', result["programLic"]["value"], '\n', 'Program Publisher:', '\n',
#               result["programPub"]["value"], '\n', 'Associated Media:', '\n', result["programMed"]["value"], '\n',
#               'Program Date:', '\n', result["programDate"]["value"], '\n', 'Program Conditions of Access:', '\n',
#               result["programCon"]["value"], '\n', 'Program URL:', '\n', result["programURL"]["value"], '\n',
#               'Program Location:', '\n', result["programLoc"]["value"], 'Program Creator:', '\n',
#               result["programCre"]["value"], 'Program Artist:', '\n', result["programArt"]["value"],
#               'Program Recorded at:', '\n', result["programRec"]["value"])
#         print('\n')
#
#
#
#
# lst=[]
# with open('./data/nisv_cat_daan_sdo_20230504.ttl',encoding="utf8") as f:
#     for line in f:
#         lst.append(line.strip())
#
#
# countDic={}
# for i in range(6,len(lst)):
#     subLst=lst[i].split(' ')
#     for j in subLst:
#         j = j.strip(',')
#         if 'sdo' == j[0:3] or 'skos' == j[0:4] or 'rdfs' == j[0:4]:
# #             print(j)
#             if j in countDic:
#                 countDic[j]+=1
#             else:
#                 countDic[j]=1
#
# # countDic
#
# sortedDic = sorted(countDic.items(), key=lambda x:x[1],reverse=True)
#
# # top=sortedDic[0:11]
# for i in sortedDic:
# #     print(i[0])
#     if 'sdo' == i[0][0:3]:
# #         print(i[4])
#         if i[0][4].islower():
#             print(i)
#     if 'skos' == i[0][0:4]:
# #         print(i[4])
#         if i[0][5].islower():
#             print(i)
#     if 'rdfs' == i[0][0:4]:
# #         print(i[4])
#         if i[0][5].islower():
#             print(i)
#
# lst2=[]
# with open('./data/nisv_cat_daan_sdo_20230504.ttl',encoding="utf8") as f:
#     for line in f:
#         lst2.append(line.strip())
#
# import re
#
# lst22 = []
# for i in range(0, len(lst2)):
#     new = lst2[i].strip()
#     sub = re.split('\s\.', new)
#     if sub[-1] == '':
#         sub = sub[0:len(sub) - 1]
#
#     #     print(sub)
#
#     if len(sub) > 1:
#
#         for j in range(0, len(sub)):
#             if len(sub[j]) != 0:
#
#                 if j == 0:
#                     lst22.append(sub[j] + ' .')
#
#                 if sub[j][-1] != ';' and sub[j][-1] != ',':
#                     lst22.append(sub[j] + ' .')
#
#                 else:
#                     lst22.append(sub[j])
#     else:
#         #         print(sub)
#         if len(sub) > 0:
#             #             lst22.append(sub[0])
#             #             print(sub[0][-1])
#             if sub[0][-1] != ';' and sub[0][-1] != ',':
#                 lst22.append(sub[0] + ' .')
#             else:
#                 lst22.append(sub[0])
#
# lst3 = []
# for i in range(6, len(lst22)):
#
#     if i == 6:
#         first = lst22[i].split(' ')[0]
#
#     if lst22[i].split(' ')[0] == first:
#         lst3.append(lst22[i])
#     else:
#         lst3.append(first + ' ' + lst22[i])
#
#     if (lst22[i][-1] == '.' and i != len(lst22) - 1):
#         first = lst22[i + 1].split(' ')[0]
#
#
#
# lst4=[]
# for i in range(len(lst3)):
#     if '[' in lst3[i]:
#         lst4.append(lst3[i]+' '+lst3[i+1])
#     else:
#         lst4.append(lst3[i])
#
#
# # file = open('items.txt','w', encoding="utf-8")
# # file.writelines(lst3)
# # file.close()
# # print(lst3[0:10])
# with open('items.txt', 'w', encoding="utf-8") as f:
#     for line in lst4:
#         f.write(line+'\n')
#
# with open('items.txt', encoding="utf-8") as f:
#     lines = f.readlines()
#
# lst5 = []
# com = 0
# for i in range(0, len(lines)):
#
#     if lines[i].strip('\n')[-1] == ',' and i + 1 != com:
#         n = lines[i].strip('\n')
#
#         for j in range(i + 1, len(lines)):
#             n = n + ' ' + lines[j].strip('\n')
#             if lines[j].strip('\n')[-1] == ';':
#                 lst5.append(n)
#                 com = j
#
#                 break
#     else:
#         n = lines[i].strip('\n')
#         lst5.append(n)

#             print(lines[i+1].strip('\n'))
#         print(var)


with open('items2.txt', 'w', encoding="utf-8") as f:
    for line in lst5:
        f.write(line+'\n')

with open('items2.txt', encoding="utf-8") as f:
    lines = f.readlines()


ddic={}
for i in lines:
    i=i.strip('\n')
    sub=i.split(' ')[0].strip()
#     print(sub)
    if sub not in ddic:
        ddic[sub]=[' '.join(i.split(' ')[1:])]
    else:
        ddic[sub].append(' '.join(i.split(' ')[1:]))

