from setuptools import setup, find_packages

setup(
    name='qd2_orchestrator',
    version='0.2.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    package_data={
        '': ['src/templates/*.j2'],
    },
    install_requires=[
        'click',
        'pyyaml',
        'ansible',
        'ansible_runner',
        'ansible-core'
    ],
    entry_points={
        'console_scripts': [
            'qd2_orchestrator = src.cli:cli',
        ],
    },
)
