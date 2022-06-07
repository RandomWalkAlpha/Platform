# Data Model

Data model is used to describe factor information, task and data status. Firstly, when initialized, the task status is *pending*, which means the task is waiting for queuing. Secondly, We will transfer the serialized *DataModel* object to the task queue and change its status to *queuing*. When the task is being computed, its status will change to *executing*. The result will be saved to *Redis*. Factor data in *redis* will be recognized by the following forms:

KEY (str) | VALUE (str)
--- | ---
signal:[NAME] | Factor signal expression
signal_data:[NAME] | Corresponding serialized dataframe

When finished execution, the status will convert to *failed* or *finished*, depending on the task result. And this model has a member called *self.info*, which including extra information like the start / end date or cost, etc.

For more implement details please refer to `model.py`.