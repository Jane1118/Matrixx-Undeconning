# Matrixx-Undeconning



DO NOT DECONNE

Pour lancer :

hadoop fs -rm -r /user/damien.menigaux/data
hadoop fs -mkdir /user/damien.menigaux/data

hadoop fs -put A.txt /user/damien.menigaux/data
hadoop fs -put B.txt /user/damien.menigaux/data


Premier job

hadoop jar /opt/hadoop/hadoop-2.7.3_master/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /user/damien.menigaux/data \
-output /user/damien.menigaux/output \
-file /home/damien.menigaux/projet/code/python/join/mapper.py \
-file /home/damien.menigaux/projet/code/python/join/combiner.py \
-mapper /home/damien.menigaux/projet/code/python/join/mapper.py \
-reducer /home/damien.menigaux/projet/code/python/join/combiner.py



Deuxieme job
hadoop jar /opt/hadoop/hadoop-2.7.3_master/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /user/damien.menigaux/output/part-00000 \
-output /user/damien.menigaux/output1 \
-file /home/damien.menigaux/projet/code/python/join/reducer.py \
-mapper /home/damien.menigaux/projet/code/python/join/reducer.py

