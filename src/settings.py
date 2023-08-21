from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "UAVOD-10"
PROJECT_NAME_FULL: str = "UAVOD-10: 10 category UAV Small Weak Object Detection Dataset"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_NC_ND_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [
    Domain.SmallWeakObjectsDetection(),
    Domain.DroneInspection(),
    Research.Geospatial(),
]
CATEGORY: Category = Category.Aerial(extra=Category.Drones(), is_original_dataset=False)

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = "2022-08-20"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = (
    "https://github.com/weihancug/10-category-UAV-small-weak-object-detection-dataset-UAVOD10"
)
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 1545749
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/uav-small-object-detection"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://drive.google.com/file/d/1emLAe7002_syWNxsTO0MgVg4knokFVlQ/view?usp=sharing"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "building": [230, 25, 75],
    "ship": [60, 180, 75],
    "vehicle": [255, 225, 25],
    "prefabricated-house": [0, 130, 200],
    "well": [245, 130, 48],
    "cable-tower": [145, 30, 180],
    "pool": [70, 240, 240],
    "landslide": [240, 50, 230],
    "cultivation-mesh-cage": [210, 245, 60],
    "quarry": [250, 190, 212],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = [
    "https://www.sciencedirect.com/science/article/pii/S1569843222001595",
    "https://ieeexplore.ieee.org/abstract/document/9335501",
    "https://ieeexplore.ieee.org/abstract/document/9281082",
]
CITATION_URL: Optional[str] = None
AUTHORS: Optional[List[str]] = [
    "Wei Han",
    "Jun Li",
    "Sheng Wang",
    "Yi Wang",
    "Jining Yan",
    "Runyu Fan",
    "Xiaohan Zhang",
    "Lizhe Wang",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "China University of Geosciences"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://en.cug.edu.cn/"

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "hide_dataset": HIDE_DATASET,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
