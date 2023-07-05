Dataset **UAV Small Object Detection** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/G/W/YT/g6AW1ahZe0imEGkALndtk4aXGRokNC1Q3okoGcjKWzn7KnPepVbrbzOcSvEVctznPE8rqye8jsItvUqAD0Zzo1Ds09aC1hFSEG9s1hirUzg5Vy5ueBLNSPfqrnhg.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='UAV Small Object Detection', dst_path='~/dtools/datasets/UAV Small Object Detection.tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/sovitrath/uav-small-object-detection-dataset/download?datasetVersionNumber=1)