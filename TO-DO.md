### To Do:

* Clean up datatypes for efficiency and accuracy (e.g. 'date' to datetime)

* Address observed data cleanup issues:
    + such as the inconsistency in event placement across the two slots ('event_name_1','event_name2'):
    `agg_1[(agg_1['event_name_1'].isin(['OrthodoxEaster','Easter'])) | (agg_1['event_name_2'].isin(['OrthodoxEaster','Easter']))][['date','event_name_1','event_type_1','event_name_2','event_type_2']].sort_values('date')`

* Batch the 'fatter' aggregations so they can run on weaker machines (make_agg_12 - make_agg_9)
