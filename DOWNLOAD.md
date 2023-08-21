Dataset **UAVOD-10** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/V/R/2h/YX11y28XFtaX3ybrc1dAY0OZWHfPfdv1hGCi3wWR3tuBnLpfa2l16CNeh51Pb4hbik9b8AwEdJw9vcn47YEh5pooM9YH8Eisji5ciZtSFGYNlbHcAvOKCupmXo83.tar)

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