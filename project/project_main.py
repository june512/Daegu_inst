import function as f

f.MariaDb.create(0,'대구')

list_all=f.Array.value(0,'대구카페추천','대구공방추천','대구호텔추천','instafood')


for i in range(len(list_all)):
    f.MariaDb.insert_all(0,'대구',tuple(list_all[i]))
