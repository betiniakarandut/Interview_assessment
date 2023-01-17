#**Interview assessment**

# - Question:
*"Question.1:Given a list of maps below. Phrases in the same map are considered synonyms. Eg. {“Dg set”: “Diesel generator”} implies “Dg set” and “Diesel generator” are synonyms.
If a phrase S1 is a synonym of phrase S2 and S3 is a synonym of S2, then S1, S2, S3 are synonyms of each other by associative property. S1,S2,S3 will be part of a “group”.
A group can be of minimum two phrases or more. Task of the question is: Given a Table of synonyms, Find all groups of synonyms.
Input: [ {“Dg set”: “Diesel generator”}, {“Organization”: “Organisation”}, {“Group”: “Organization”}, {“Orange”: “Kinnu”}, {“Orange”: “narangi”} ] Output: [[“Organization”, “Organisation”, “Group”], [“Dg set”, “Diesel generator”], [“Orange”, “Kinnu”, “narangi”]]

