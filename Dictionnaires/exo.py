# exo 1 et 2:
dressing = {"pantalons":3, "pulls":4, "tee-shirts":8}
def achat(habit):
    if habit in dressing :
        dressing[habit] += 1
    else :
        dressing[habit] = 1

# exo 3:
lst = ['5717', '1133', '5545', '4031', '6398', '2734', '3070', '1346', '7849', '7288', '7587', '6217', '8240', '5733', '6466', '7972', '7341', '6616', '5061', '2441', '2571', '4496', '4831', '5395', '8584', '3033', '6266', '2452', '6909', '3021', '5404', '3799', '5053', '8096', '2488', '8519', '6896', '7300', '5914', '7464', '5068', '1386', '9898', '8313', '1072', '1441', '7333', '5691', '6987', '5255']
chiffre = {}
for k in range(10):
    chiffre[k] = 0

for k in lst:
    for nb in k:
        if int(nb) in chiffre:
            chiffre[int(nb)] += 1

chiffre_max = 0
for i in chiffre:
    if chiffre[chiffre_max] < chiffre[i]:
        chiffre_max = i
print(chiffre_max, chiffre[chiffre_max])



        
