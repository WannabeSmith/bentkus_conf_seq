from setuptools import setup

setup(
    name="bentkus_conf_seq",
    version="0.1",
    description="Bentkus confidence sequences",
    url="http://github.com/enosair/bentkus_conf_seq",
    author="Qingqing Zheng",
    author_email="",
    license="MIT",
    packages=["bentkus_conf_seq"],
    install_requires=[
        "numpy",
        "scipy",
        "confseq"
    ],
    zip_safe=False,
)
