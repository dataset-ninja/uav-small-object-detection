Dataset **UAVOD-10** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzE1NzhfVUFWT0QtMTAvdWF2b2QtMTAtRGF0YXNldE5pbmphLnRhciIsICJzaWciOiAiazI3NWs4d3Z4RXRTS3Rzc05PQ2FoNzBjeXROZ29JQ0hwd1JzRkJ5bU5xND0ifQ==)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='UAVOD-10', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://drive.google.com/file/d/1emLAe7002_syWNxsTO0MgVg4knokFVlQ/view?usp=sharing).