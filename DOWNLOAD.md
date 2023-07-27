Dataset **UAV Small Object Detection (UAVOD-10)** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/M/E/nQ/cWw9MTtjg4vdxWVn3z4MqTemT8ERsGzikHgIrd1hNd2mZIN94QcS3uoJmO7IOFxaBLZfGY8CfHo9UGurgy5LtlOSO5oNJmY96yC99uJzrC38aRBSbtim3RdJPZaY.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='UAV Small Object Detection (UAVOD-10)', dst_path='~/dtools/datasets/UAV Small Object Detection (UAVOD-10).tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/sovitrath/uav-small-object-detection-dataset/download?datasetVersionNumber=1)